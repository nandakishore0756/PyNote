# Contributing to PyNote

Thank you for your interest in contributing to PyNote! This document provides guidelines and instructions for contributing to the project.

## 🎯 Getting Started

1. **Fork the repository** and clone it locally
2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Find an issue** labeled `good first issue` or check the difficulty labels
4. **Create a branch** following our naming convention
5. **Make your changes** and test them
6. **Submit a pull request**

## 📝 Branch Naming

Use descriptive branch names:
- `feature/<short-desc>` - for new features
- `bug/<short-desc>` - for bug fixes
- `docs/<short-desc>` - for documentation updates

Examples:
- `feature/add-toolbar-icons`
- `bug/fix-save-dialog`
- `docs/update-readme`

## 💬 Commit Messages

Use short, imperative commit messages:
- ✅ `fix: update save dialog`
- ✅ `feat: add dark theme toggle`
- ✅ `docs: update contributing guide`
- ❌ `Fixed some stuff`
- ❌ `updates`

Format: `<type>: <description>`

Types: `fix`, `feat`, `docs`, `style`, `refactor`, `test`, `chore`

## 🔍 Issue Labels

- `good first issue` - Perfect for beginners
- `easy` - Beginner-friendly tasks (1-2 hours)
- `medium` - Intermediate tasks (3-5 hours)
- `hard` - Advanced tasks (6-10 hours)
- `bug` - Something isn't working
- `enhancement` - New feature or improvement
- `documentation` - Documentation improvements
- `help wanted` - Extra attention needed
- `design` - UI/UX related

## 📋 Pull Request Process

1. **Reference an issue** - All PRs should reference an issue number (e.g., `Fixes #123`)
2. **Keep PRs focused** - One logical change per PR
3. **Include screenshots** - For UI changes, include before/after screenshots
4. **Test your changes** - Run the app and verify it works
5. **Update documentation** - If adding features, update relevant docs
6. **Label your PR** - Add appropriate labels when creating the PR

### PR Template

When creating a PR, include:

```markdown
## Description
Brief description of changes

## Related Issue
Closes #123

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Other (please describe)

## Testing
Steps to test:
1. ...
2. ...

## Screenshots (if applicable)
[Add screenshots here]

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests pass (if applicable)
```

## 🧪 Testing

Before submitting a PR:

1. **Run the application**:
   ```bash
   python -m src.pynote.main
   ```
2. **Test your changes** manually
3. **Run tests** (if applicable):
   ```bash
   pytest tests/
   ```

## 📐 Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small
- Use type hints where appropriate

## 🎨 UI Guidelines

- Follow existing UI patterns
- Ensure dark/light theme compatibility
- Test on different screen sizes if applicable
- Keep the interface clean and intuitive

## 🐛 Reporting Bugs

Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md) and include:

- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Environment details (OS, Python version)

## 💡 Suggesting Features

Use the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md) and include:

- Clear description of the feature
- Use case / problem it solves
- Proposed solution
- Mockups or examples (if applicable)

## 📊 Acceptance Criteria

Each issue includes acceptance criteria. Make sure your PR satisfies all criteria before submitting.

Example:
- ✅ Feature works as described
- ✅ Code follows style guidelines
- ✅ No regressions introduced
- ✅ Documentation updated

## 🔍 Code Review Guidelines

Code reviews ensure quality and consistency. Follow these guidelines:

### For Reviewers:
- Be constructive and respectful
- Focus on code quality, not personal preferences
- Suggest improvements, don't dictate
- Approve when criteria are met
- Request changes with clear explanations

### For Contributors:
- Address all review comments
- Explain complex changes when needed
- Don't take feedback personally
- Iterate on feedback

### Review Checklist:
- [ ] Code follows style guidelines
- [ ] Logic is sound and efficient
- [ ] Tests are included/updated
- [ ] Documentation is updated
- [ ] No security vulnerabilities
- [ ] Performance impact considered

## 🔒 Security

If you discover a security vulnerability:

1. **Do not** create a public issue
2. Email maintainers directly at [security@pynote.dev](mailto:security@pynote.dev)
3. Include detailed steps to reproduce
4. Allow time for fix before public disclosure

## 🤝 Community Guidelines

- Be respectful and inclusive
- Use welcoming language
- Focus on constructive feedback
- Respect differing viewpoints
- Help newcomers learn

## 🧪 Advanced Testing

Beyond basic testing:

### Unit Tests:
```bash
pytest tests/test_utils.py -v
```

### Integration Tests:
- Test full workflows end-to-end
- Verify file operations work correctly
- Check UI interactions

### Performance Testing:
- Monitor memory usage for large files
- Test startup time
- Verify responsiveness

## ⚡ Performance Considerations

- Optimize file operations for large documents
- Minimize UI redraws
- Use efficient data structures
- Profile code for bottlenecks

## 📚 Resources

- [Python PEP 8 Style Guide](https://pep8.org/)
- [PyQt Documentation](https://doc.qt.io/qtforpython/)
- [Git Best Practices](https://git-scm.com/book/en/v2)
- [Conventional Commits](https://conventionalcommits.org/)

## 🚀 Release Process

1. **Version Bumping**: Update version in `__init__.py`
2. **Changelog**: Document changes in `CHANGELOG.md`
3. **Testing**: Run full test suite
4. **Build**: Create distributable packages
5. **Tag**: Create git tag with version
6. **Publish**: Upload to PyPI

## ❓ Questions?

- Open a discussion in the repository
- Check existing issues for similar questions
- Reach out to maintainers

## 🙏 Thank You!

Your contributions make PyNote better for everyone. We appreciate your time and effort!

---

**Happy Contributing! 🚀**

