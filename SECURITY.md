# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it by:

1. **Email**: Send details to the project maintainer (check GitHub profile for contact info)
2. **GitHub Security Advisory**: Use [GitHub's private vulnerability reporting](https://github.com/<owner>/<repo>/security/advisories/new)

   <!-- TODO: Replace <owner>/<repo> with your actual GitHub owner/repo -->

### What to Include

- Description of the vulnerability
- Steps to reproduce
- Affected versions
- Potential impact

### Response Time

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 7 days
- **Fix Timeline**: Depends on severity (critical: ASAP, others: next release)

## Security Best Practices

When using this template:

- Keep dependencies up to date (`pixi run security` to check for vulnerabilities)
- Never commit secrets (use `.env` files and add them to `.gitignore`)
- Review third-party dependencies before adding them

## Attribution

Security researchers who responsibly disclose vulnerabilities will be credited in release notes (unless they prefer to remain anonymous).
