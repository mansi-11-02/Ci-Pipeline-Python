# Continuous Integration (CI) Pipeline

This project implements a Continuous Integration (CI) pipeline using GitHub Actions. It automates code quality checks, security scans, test coverage, static analysis with SonarQube, and sends email notifications with reports.

## 🚀 Workflow Trigger

The pipeline runs on every push to the repository.

## 🧱 Workflow Steps Breakdown

1. **Checkout Code**
   - Checks out the repository code so the workflow can access it.

2. **Set Up Python**
   - Sets up a Python 3.x environment for the job.

3. **Install Dependencies**
   - Installs Python dependencies listed in `requirements.txt`.
   - Installs and sets up the SonarQube scanner.

4. **Lint with Pylint**
   - Linting checks code for syntax and style issues to ensure consistency and catch potential errors.
   - Runs static code analysis using pylint. The configuration is defined in `.pylintrc`.
   - Edit `.pylintrc` to customize linting rules (e.g., naming conventions, complexity thresholds).

6. **Check Code Format with Black**
   - Formatting automatically adjusts code layout to follow defined style guidelines.
   - Checks if code is formatted according to black. Fails if formatting is incorrect.
   - Edit `pyproject.toml` to configure black (e.g., line length, exclusions).

8. **Run Security Scan with Bandit**
   - Security scanning analyzes code for known vulnerabilities and insecure coding practices.
   - Scans for security issues in Python code.
   - `|| true` ensures the pipeline continues even if issues are found (for now).

10. **Run Tests with Coverage**
   - Testing runs automated tests to verify that the code behaves as expected and meets requirements.
   - Runs unit tests and generates code coverage reports.
   - Coverage is used later by SonarQube.

11. **Upload CI Reports**
   - Uploads reports (pylint, bandit, coverage) as artifacts for download.

11. **SonarQube Scan**
   - Performs static analysis and uploads results to SonarCloud.
   - Uses `SONAR_TOKEN` secret for authentication.
   - Project key and organization are configured in the script.

11. **Send Email Notification**
    - Sends an email with:
      - SonarQube dashboard link
      - Attached reports
    - ⚠️ Important: Use an App Password for Gmail if 2FA is enabled.
    - The mail will look like this
    - ![image](https://github.com/user-attachments/assets/d2a7c9f9-34e7-4d84-be60-934a57ea4428)



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

