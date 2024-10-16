# Contributing to the Project

First of all, thank you for your interest in contributing to this project! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Contributing Code](#contributing-code)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Development Workflow](#development-workflow)
  - [Code Structure](#code-structure)
  - [Framework-Specific Code](#framework-specific-code)
  - [Modularity](#modularity)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Code Style](#code-style)
  
## Code of Conduct

By participating in this project, you agree to abide by the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

## How to Contribute

### Reporting Bugs

If you find a bug in the project, we encourage you to help us improve it:

- **Ensure the bug was not already reported** by searching the existing issues.
- If you're unable to find an open issue addressing the problem, open a new issue. Please be sure to include:
  - A clear, descriptive title.
  - A description of the steps needed to reproduce the issue.
  - Any relevant logs, screenshots, or files that may help us troubleshoot the issue.
  
### Suggesting Enhancements

Enhancements are always welcome! You can suggest new features or improvements by opening an issue. Please include the following details:

- A clear description of the enhancement or feature.
- Why you think it would be useful for others.
- Any examples or ideas of how it might be implemented.

### Contributing Code

To contribute code to the project:

1. Fork the repository.
2. Create a new branch from `dev` for your feature.
3. Implement your feature or fix the bug.
4. Commit your changes (follow the [commit message guidelines](#commit-message-guidelines)).
5. Push your branch to your forked repository.
6. Open a pull request to the main repository.
   
Make sure that your code follows the [code style](#code-style) guidelines.

## Pull Request Guidelines

When submitting a pull request (PR):

- Ensure that your PR is small and focused. Larger PRs should be broken into smaller, more manageable parts if possible.
- **Do not change any code unrelated to your contribution.** If there are formatting changes or other unrelated modifications, please submit those in a separate PR.
- Write clear, descriptive commit messages for each commit.
- Include tests whenever possible to ensure that your changes work as intended.
- If your PR relates to an open issue, reference it in the PR description (e.g., "Fixes #123").
- Ensure that your code passes all CI checks (tests, formatting, etc.).
  
## Development Workflow

### Code Structure

The project follows a modular structure, where different submodules handle specific functionalities. Here are the main directories you will encounter:

- **`core/`**: This submodule contains framework-specific code (currently TensorFlow and PyTorch). Any framework-specific logic should reside here.
- **`attacks/`**: This submodule is framework-independent and should not contain any TensorFlow, PyTorch, JAX specific logic. If you need additional functionality for a specific framework, include it in the `core` submodule.

### Framework-Specific Code

The project currently supports **TensorFlow** and **PyTorch**, and is designed to support **JAX** and **NumPy** in the future. If you're adding support for a specific framework or extending functionality:

- Any **framework-specific code** must be added under the `core/` submodule.
  - For example, if you're adding support for a new optimizer or loss function in TensorFlow or PyTorch, it must go under the `core/` module..
- The `attacks/` submodule must remain **completely framework-independent**. If an attack requires framework-specific features, abstract those features into the `core/` submodule.
- If you're unsure where a piece of code should go, refer to existing patterns in the codebase, or ask for clarification in an issue or pull request.

### Modularity

The project is designed to be **highly modular**. Each component (such as loss functions, optimizers, and noise generators) should be designed to plug into the `attacks/` module easily, without requiring the user to understand the internal workings of the system.

- Ensure that new components (like a custom optimizer or noise generator) are easily compatible with the existing attack APIs.
- Follow the existing modular design principles where users can configure components externally and pass them into the attack without modifying core logic.

### Testing Your Code

Please ensure that all new code is thoroughly tested. For new components or features, add tests to verify the functionality. For bug fixes, add a test that demonstrates the issue and proves that it’s resolved.

- Write tests for both framework-specific and framework-independent code.
- Include unit tests for each new functionality.
- Make sure existing tests pass before submitting a PR.

## Commit Message Guidelines

Write clear, meaningful commit messages that describe **what** the change is and **why** it was made. This helps others understand the history of the project and makes reviewing pull requests easier.

A good commit message example:

Add custom loss function for adversarial attacks

This commit adds a new loss function CustomLoss that can be used for adversarial attacks. It follows the modular design of the project and is compatible with both TensorFlow and PyTorch.

## Code Style

Follow the existing style and formatting conventions in the codebase. Some general guidelines:

- Use **PEP 8** for Python code.
- Use meaningful variable and function names.
- Keep functions small and focused on a single task.
- Include docstrings for all functions, classes, and modules.
- Organize imports in the following order: standard library imports, third-party imports, local imports.

We use linters and formatters (like `black` for Python). Ensure that your code passes all formatting checks before submitting a pull request.

---

By following these guidelines, you’ll help maintain the quality and consistency of the project, and make it easier for everyone to contribute. Thanks again for your interest in contributing!
