# Continuous Integration (CI) Pipeline

This project implements a Continuous Integration (CI) pipeline using GitHub Actions. It automates code quality checks, security scans, test coverage, static analysis with SonarQube, and sends email notifications with reports.

## 🚀 Workflow Trigger

The pipeline runs on every push or pull request to the repository.

## 🧱 Workflow Steps Breakdown

1. **Checkout Code**
   - Checks out the repository code so the workflow can access it.

2. **Set Up Python**
   - Sets up a Python 3.x environment for the job.

3. **Install Dependencies**
   - Installs Python dependencies listed in `requirements.txt`.
   - Installs and sets up the SonarQube scanner.

4. **Lint with Pylint**
   - Runs static code analysis using pylint. The configuration is defined in `.pylintrc`.
   - Edit `.pylintrc` to customize linting rules (e.g., naming conventions, complexity thresholds).

5. **Check Code Format with Black**
   - Checks if code is formatted according to black. Fails if formatting is incorrect.
   - Edit `pyproject.toml` to configure black (e.g., line length, exclusions).

6. **Run Security Scan with Bandit**
   - Scans for security issues in Python code.
   - `|| true` ensures the pipeline continues even if issues are found (for now).

7. **Run Tests with Coverage**
   - Runs unit tests and generates code coverage reports.
   - Coverage is used later by SonarQube.

8. **Upload CI Reports**
   - Uploads reports (pylint, bandit, coverage) as artifacts for download.

9. **SonarQube Scan**
   - Performs static analysis and uploads results to SonarCloud.
   - Uses `SONAR_TOKEN` secret for authentication.
   - Project key and organization are configured in the script.

10. **Send Email Notification**
    - Sends an email with:
      - SonarQube dashboard link
      - Attached reports
    - ⚠️ Important: Use an App Password for Gmail if 2FA is enabled.

## ⚠️ About `continue-on-error: true`

This flag allows the workflow to continue even if a step fails. It's useful during development to collect all reports regardless of individual failures.

### In Production:
- Remove `continue-on-error: true` to ensure the pipeline fails fast.
- This prevents merging code that doesn't meet quality or security standards.

## 🛠️ Configuration Files

| File             | Purpose                          | How to Edit                              |
|------------------|----------------------------------|------------------------------------------|
| `.pylintrc`      | Pylint rules (naming, complexity, etc.) | Modify rule values or disable specific checks |
| `pyproject.toml` | Black formatting rules           | Change line length, exclude files, etc.  |
| `requirements.txt` | Python dependencies              | Add/remove packages as needed            |

## 📬 Secrets Required

| Secret Name      | Description                      |
|------------------|----------------------------------|
| `SONAR_TOKEN`    | SonarCloud authentication token  |
| `EMAIL_USERNAME` | Sender email address             |
| `EMAIL_PASSWORD` | App password for email           |
| `EMAIL_RECEIVER` | Recipient email address          |

