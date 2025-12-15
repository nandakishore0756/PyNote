# PyNote — A Beginner-Friendly Desktop Text Editor

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**PyNote** is a lightweight, cross-platform desktop text editor built with **Python + Tkinter**. It's designed for college-level contributors: approachable for beginners, with room for intermediate and harder issues (syntax highlighting, plugin system, mini-map, markdown preview).

## 🎯 Project Goals

* Give new contributors immediate, visible wins (UI, theming, docs)
* Provide medium/hard tasks that teach useful skills (file I/O, tokenizers, UI architecture)
* Produce a usable editor students will be proud of

## ✨ Core Features (MVP)

* ✅ Open / Save / Save As
* ✅ Undo / Redo
* ✅ Line numbers
* ✅ Status bar showing line/column
* ✅ Basic keyboard shortcuts (Ctrl+S, Ctrl+O, Ctrl+Z)
* ✅ Light / Dark theme toggle
* ✅ Autosave (configurable)

## Theming and Configuration
* Apply themes from themes.py in main.py
* Add theme switching menu option
* Utilize settings system from utils.py for user preferences

## Feature Enhancements
* Add line numbers to EditorWidget
* Implement autosave functionality
* Improve status bar with word count, character count, and file encoding

## Code Quality Improvements
* Add type hints throughout the codebase
* Enhance error handling with specific exceptions and user-friendly messages
* Add comprehensive docstrings to all classes and methods
* Use constants for magic numbers and strings
* Implement logging for debugging

## 🚀 Nice-to-Have Features (Stretch)

* Tabbed editing (multiple files)
* Find & Replace dialog
* Syntax highlighting for Python / JavaScript / HTML
* Settings saved to JSON
* Recent files list
* Markdown preview (split view)
* Plugin system (simple hook-based)
* Spell checking (integrate `pyspellchecker`)

## 📋 Quickstart

### Prerequisites

* Python 3.10+ (3.11 recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_ORG/PyNote.git
cd PyNote
```

2. Create virtual environment and install dependencies:
```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

3. Run the application:
```bash
python -m src.pynote.main
```

## 📁 Project Structure

```
PyNote/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/
│       └── python-app.yml
├── docs/
│   ├── ROADMAP.md
│   └── DESIGN.md
├── src/
│   └── pynote/
│       ├── __init__.py
│       ├── main.py          # starter app
│       ├── editor.py        # Text widget wrapper
│       ├── ui.py            # UI components (menus, dialogs)
│       ├── themes.py        # theme definitions
│       └── utils.py         # helper functions
├── tests/
│   └── test_utils.py
├── examples/
│   └── example.md/
├── CONTRIBUTING.md
├── README.md
├── LICENSE
└── requirements.txt
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

* Look for issues labeled `good first issue` to get started
* Check the [ROADMAP.md](docs/ROADMAP.md) for project milestones
* All PRs should reference an issue

## Roadmap

See [docs/ROADMAP.md](docs/ROADMAP.md) for detailed milestones:

* `v0.1 - MVP` (Open/Save, menu, status bar, shortcuts)
* `v0.2 - UX` (themes, line numbers, autosave)
* `v0.3 - Power features` (tabs, find/replace, syntax highlighting)
* `v1.0 - Release` (stable, docs, tests)

## Reporting Issues

Found a bug or have a feature request? Please use our [issue templates](.github/ISSUE_TEMPLATE/)!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



**Happy Coding! 🎉**

