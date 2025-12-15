"""
Mini Language Server Client for PyNote.
Basic LSP client using JSON-RPC over stdin/stdout.
"""

import json
import subprocess
import threading
import queue
import os


class LSPClient:
    """
    Basic LSP client for communicating with a language server.
    """

    def __init__(self, server_command):
        """
        Initialize the LSP client with a server command.

        Args:
            server_command: List of command arguments to start the language server.
        """
        self.process = subprocess.Popen(
            server_command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=os.getcwd()
        )
        self.request_id = 0
        self.responses = {}
        self.response_queue = queue.Queue()
        self.thread = threading.Thread(target=self._read_responses, daemon=True)
        self.thread.start()

    def _read_responses(self):
        """Read responses from the language server."""
        while True:
            line = self.process.stdout.readline()
            if not line:
                break
            try:
                response = json.loads(line.strip())
                if 'id' in response:
                    self.responses[response['id']] = response
            except json.JSONDecodeError:
                pass  # Ignore invalid JSON

    def send_request(self, method, params):
        """
        Send a request to the language server.

        Args:
            method: LSP method name.
            params: Parameters for the method.

        Returns:
            Request ID.
        """
        self.request_id += 1
        request = {
            'jsonrpc': '2.0',
            'id': self.request_id,
            'method': method,
            'params': params
        }
        self.process.stdin.write(json.dumps(request) + '\n')
        self.process.stdin.flush()
        return self.request_id

    def get_response(self, request_id, timeout=5):
        """
        Get the response for a request ID.

        Args:
            request_id: The request ID.
            timeout: Timeout in seconds.

        Returns:
            Response dict or None if timeout.
        """
        import time
        start_time = time.time()
        while request_id not in self.responses and (time.time() - start_time) < timeout:
            time.sleep(0.01)
        return self.responses.pop(request_id, None)

    def initialize(self, root_uri):
        """
        Initialize the language server.

        Args:
            root_uri: Root URI of the project.
        """
        params = {
            'processId': os.getpid(),
            'rootUri': root_uri,
            'capabilities': {
                'textDocument': {
                    'completion': {
                        'dynamicRegistration': False,
                        'completionItem': {
                            'snippetSupport': False,
                            'commitCharactersSupport': False,
                            'documentationFormat': ['plaintext'],
                            'deprecatedSupport': False,
                            'preselectSupport': False
                        }
                    }
                }
            }
        }
        req_id = self.send_request('initialize', params)
        response = self.get_response(req_id)
        if response:
            self.send_request('initialized', {})

    def text_document_did_open(self, uri, language_id, text, version=1):
        """
        Notify the server that a text document was opened.

        Args:
            uri: Document URI.
            language_id: Language ID (e.g., 'python').
            text: Document text.
            version: Document version.
        """
        params = {
            'textDocument': {
                'uri': uri,
                'languageId': language_id,
                'version': version,
                'text': text
            }
        }
        self.send_request('textDocument/didOpen', params)

    def text_document_did_change(self, uri, text, version=1):
        """
        Notify the server that a text document changed.

        Args:
            uri: Document URI.
            text: New document text.
            version: Document version.
        """
        params = {
            'textDocument': {
                'uri': uri,
                'version': version
            },
            'contentChanges': [
                {
                    'text': text
                }
            ]
        }
        self.send_request('textDocument/didChange', params)

    def text_document_completion(self, uri, line, character):
        """
        Request completion at a position.

        Args:
            uri: Document URI.
            line: Line number (0-based).
            character: Character position (0-based).

        Returns:
            Completion response.
        """
        params = {
            'textDocument': {
                'uri': uri
            },
            'position': {
                'line': line,
                'character': character
            }
        }
        req_id = self.send_request('textDocument/completion', params)
        return self.get_response(req_id)

    def shutdown(self):
        """Shutdown the language server."""
        self.send_request('shutdown', {})
        self.process.terminate()
        self.thread.join()
