# Contributing Guide

Thank you for your interest in contributing to this project!

## Development Setup

### Prerequisites

- [Pixi](https://pixi.sh) installed on your system

### Setup Steps

1. Fork and clone the repository

   ```bash
   git clone https://github.com/<your-username>/change-to-your-name.git
   cd change-to-your-name
   ```

   <!-- TODO: Replace <your-username> with your actual GitHub username -->

2. Install dependencies

   ```bash
   pixi install
   ```

3. Install Git hooks

   ```bash
   pixi run pre-commit install
   ```

## Development Workflow

### Code Quality

Before committing, ensure your code passes all checks:

```bash
# Lint
pixi run lint

# Format
pixi run format

# Type check
pixi run typecheck

# Run all checks
pixi run lint && pixi run format && pixi run typecheck
```

### Testing

```bash
# Run tests
pixi run test

# Tests include coverage (minimum 80%)
```

### Security

```bash
# Check for dependency vulnerabilities
pixi run security
```

## Git Workflow

### Branch Naming

- `feature/<description>` - New features
- `fix/<description>` - Bug fixes
- `docs/<description>` - Documentation changes
- `refactor/<description>` - Code refactoring

### Commit Messages

This project uses [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <description>

[optional body]

[optional footer]
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `test`: Tests
- `refactor`: Code refactoring
- `chore`: Maintenance

**Examples**:
```
feat: add user authentication
fix: resolve null pointer in config loader
docs: update installation instructions
```

### Pull Request Process

1. Create a feature branch from `main`
2. Make your changes
3. Ensure all checks pass (lint, typecheck, test)
4. Push to your fork
5. Open a PR against `main`

### PR Checklist

- [ ] Code follows the project's style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Documentation updated if needed
- [ ] Commit messages follow Conventional Commits

## Code Style

This project uses:

- **Ruff** for linting and formatting
- **MyPy** for type checking (strict mode)
- **pytest** for testing

Configuration is in `pyproject.toml`.

## Getting Help

- Open an issue for bugs or feature requests
- Check existing issues before opening new ones
- Provide clear reproduction steps for bugs

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
