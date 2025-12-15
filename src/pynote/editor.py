# src/pynote/editor.py
"""
Editor widget wrapper for PyNote.
"""

import tkinter as tk
from tkinter import ttk
from .lsp_client import LSPClient
import os
import urllib.parse


class EditorWidget:
    """
    Wrapper around Tkinter Text widget with additional functionality.
    """

    def __init__(self, parent, language='python', **kwargs):
        """
        Initialize editor widget.

        Args:
            parent: Parent widget
            language: Language for LSP (e.g., 'python', 'javascript', 'html')
            **kwargs: Additional arguments for Text widget
        """
        self.parent = parent
        self.language = language
        self.text = tk.Text(parent, wrap='word', undo=True, **kwargs)
        self.scrollbar = ttk.Scrollbar(parent, orient='vertical', command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        # LSP client
        self.lsp_client = None
        self.document_uri = f'file://{os.getcwd()}/temp_file'  # Placeholder URI
        self.document_version = 1

        # Autocomplete variables
        self.autocomplete_listbox = None
        self.autocomplete_suggestions = []
        self.autocomplete_index = -1

        # Bind autocomplete events
        self.text.bind('<KeyRelease>', self._on_key_release)
        self.text.bind('<Tab>', self._on_tab)

    def pack(self, **kwargs):
        """Pack the editor widgets."""
        self.scrollbar.pack(side='right', fill='y')
        self.text.pack(side='left', fill='both', expand=True, **kwargs)

    def get_content(self):
        """Get all text content."""
        return self.text.get('1.0', tk.END)

    def set_content(self, content):
        """Set text content."""
        self.text.delete('1.0', tk.END)
        self.text.insert('1.0', content)
        # Notify LSP client of document change
        if self.lsp_client:
            self.document_version += 1
            self.lsp_client.text_document_did_change(self.document_uri, content, self.document_version)

    def initialize_lsp_client(self):
        """Initialize the LSP client for the specified language."""
        if self.language == 'python':
            server_command = ['pylsp']
        elif self.language == 'javascript':
            server_command = ['typescript-language-server', '--stdio']
        elif self.language == 'html':
            server_command = ['html-languageserver', '--stdio']
        else:
            return  # No LSP support for this language

        try:
            self.lsp_client = LSPClient(server_command)
            root_uri = f'file://{os.getcwd()}'
            self.lsp_client.initialize(root_uri)
            # Open the document
            content = self.get_content()
            self.lsp_client.text_document_did_open(self.document_uri, self.language, content, self.document_version)
        except Exception as e:
            print(f"Failed to initialize LSP client: {e}")
            self.lsp_client = None

    def get_cursor_position(self):
        """Get current cursor position as (line, column)."""
        idx = self.text.index(tk.INSERT).split('.')
        return int(idx[0]), int(idx[1])

    def goto_line(self, line_number):
        """Move cursor to specified line number."""
        try:
            line_num = max(1, min(line_number, int(self.text.index('end-1c').split('.')[0])))
            self.text.mark_set(tk.INSERT, f'{line_num}.0')
            self.text.see(tk.INSERT)
        except Exception:
            pass

    def _on_key_release(self, event):
        """Handle key release events for autocomplete."""
        if event.keysym in ('Up', 'Down', 'Return', 'Escape'):
            return

        # Trigger autocomplete on dot or letter
        char = event.char
        if char in '.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789':
            self._show_autocomplete()

    def _on_tab(self, event):
        """Handle Tab key for autocomplete selection."""
        if self.autocomplete_listbox and self.autocomplete_listbox.winfo_ismapped():
            self._select_autocomplete()
            return 'break'  # Prevent default tab behavior

    def _show_autocomplete(self):
        """Show autocomplete suggestions."""
        if not self.lsp_client:
            self._hide_autocomplete_list()
            return

        cursor_pos = self.get_cursor_position()
        # LSP uses 0-based line and column
        response = self.lsp_client.text_document_completion(self.document_uri, cursor_pos[0] - 1, cursor_pos[1])

        if response and 'result' in response:
            items = response['result'].get('items', [])
            self.autocomplete_suggestions = [item['label'] for item in items]
            if self.autocomplete_suggestions:
                self._display_autocomplete_list()
            else:
                self._hide_autocomplete_list()
        else:
            self._hide_autocomplete_list()

    def _display_autocomplete_list(self):
        """Display the autocomplete listbox."""
        if not self.autocomplete_listbox:
            self.autocomplete_listbox = tk.Listbox(self.parent, height=5, width=30)
            self.autocomplete_listbox.bind('<ButtonRelease-1>', self._on_listbox_select)
            self.autocomplete_listbox.bind('<KeyRelease>', self._on_listbox_key)

        self.autocomplete_listbox.delete(0, tk.END)
        for suggestion in self.autocomplete_suggestions:
            self.autocomplete_listbox.insert(tk.END, suggestion)

        # Position the listbox near the cursor
        cursor_x, cursor_y = self._get_cursor_coords()
        self.autocomplete_listbox.place(x=cursor_x, y=cursor_y + 20)
        self.autocomplete_listbox.lift()
        self.autocomplete_index = 0
        self.autocomplete_listbox.selection_set(0)

    def _hide_autocomplete_list(self):
        """Hide the autocomplete listbox."""
        if self.autocomplete_listbox:
            self.autocomplete_listbox.place_forget()

    def _get_cursor_coords(self):
        """Get the screen coordinates of the cursor."""
        bbox = self.text.bbox(tk.INSERT)
        if bbox:
            x = self.text.winfo_rootx() + bbox[0]
            y = self.text.winfo_rooty() + bbox[1] + bbox[3]
            return x, y
        return 0, 0

    def _on_listbox_select(self, event):
        """Handle selection from autocomplete listbox."""
        selection = self.autocomplete_listbox.curselection()
        if selection:
            self._insert_completion(selection[0])
        self._hide_autocomplete_list()

    def _on_listbox_key(self, event):
        """Handle key events in autocomplete listbox."""
        if event.keysym == 'Return':
            selection = self.autocomplete_listbox.curselection()
            if selection:
                self._insert_completion(selection[0])
            self._hide_autocomplete_list()
        elif event.keysym == 'Escape':
            self._hide_autocomplete_list()
        elif event.keysym == 'Up':
            self._navigate_list(-1)
        elif event.keysym == 'Down':
            self._navigate_list(1)

    def _navigate_list(self, direction):
        """Navigate the autocomplete list."""
        if self.autocomplete_listbox:
            current = self.autocomplete_listbox.curselection()
            if current:
                new_index = (current[0] + direction) % len(self.autocomplete_suggestions)
                self.autocomplete_listbox.selection_clear(0, tk.END)
                self.autocomplete_listbox.selection_set(new_index)
                self.autocomplete_listbox.see(new_index)

    def _select_autocomplete(self):
        """Select the current autocomplete suggestion."""
        if self.autocomplete_listbox and self.autocomplete_listbox.curselection():
            index = self.autocomplete_listbox.curselection()[0]
            self._insert_completion(index)
        self._hide_autocomplete_list()

    def _insert_completion(self, index):
        """Insert the selected completion."""
        if 0 <= index < len(self.autocomplete_suggestions):
            completion = self.autocomplete_suggestions[index]
            self.text.insert(tk.INSERT, completion)

