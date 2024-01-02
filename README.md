# Python Testing with pytest - Studies and Practices

[Ler em Português](./README_pt_br.md)

This repository contains my answers and studies based on the book ["Python Testing with pytest"](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/). The goal is to apply and deepen the knowledge acquired throughout the reading, practicing the concepts and techniques presented in the book.

## Learning and Using Git

I am gradually populating this repository as I progress through the book. This process is also helping me learn and practice using Git, ensuring that each learning step is documented and versioned correctly.

## Code Quality with Pre-commit

The repository is configured with the `pre-commit` tool to improve code quality and ensure good practices. Here are some of the configured hooks:

- **Trailing Whitespace**: Removes trailing whitespace at the end of lines.
- **End-of-file Fixer**: Ensures files end with a blank line.
- **Check YAML**: Check the correct formatting of YAML files.
- **Check Added Large Files**: Prevents the accidental addition of large files.
- **Debug Statements**: Detects and prevents commits containing debug statements.
- **Detect Private Key**: Prevents the accidental commit of private keys.
- **Name Tests Test**: Ensures test files are named correctly.
- **Requirements-txt-fixer**: Automatically adjusts the `requirements.txt` file.
- **Isort**: Automatically organizes imports.
- **Pydocstyle**: Checks docstring compliance with style standards.
- **Add Trailing Comma**: Adds commas at the end of lists or dictionaries.
- **Autopep8**: Automatically formats code according to PEP 8.
- **Flake8**: Checks the code to follow PEP 8 guidelines.
- **Mypy**: Checks static typing of the code.
- **Bandit**: A static code analysis tool for security.
- **Commitizen**: Assists in creating standardized commit messages.

### Continuous Configuration Review

The `pre-commit` configuration file is under constant review. As I encounter errors or conflicts in the commit stage, I am adjusting the config file to maintain the balance between code quality and practical usability.
