#!/usr/bin/env python3
"""
Test script for LSP client functionality.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from pynote.lsp_client import LSPClient

def test_lsp_client():
    """Test LSP client initialization and basic functionality."""
    print("Testing LSP client...")

    # Test with Python LSP server
    try:
        client = LSPClient(['pylsp'])
        print("LSP client initialized successfully.")
        root_uri = f'file://{os.getcwd()}'
        client.initialize(root_uri)
        print("LSP server initialized.")

        # Test document open
        uri = f'file://{os.getcwd()}/test_file.py'
        content = "def hello():\n    print('Hello, World!')\n"
        client.text_document_did_open(uri, 'python', content, 1)
        print("Document opened.")

        # Test completion
        response = client.text_document_completion(uri, 1, 4)  # After 'def '
        print(f"Completion response: {response}")

        client.shutdown()
        print("LSP client shut down.")
    except Exception as e:
        print(f"LSP client test failed: {e}")

if __name__ == '__main__':
    test_lsp_client()
