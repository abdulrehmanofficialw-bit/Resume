# QA Engineering Portfolio

Responsive high-contrast dark-themed portfolio for Abdul Rehman Rizwan, with an interactive browser-side QA lab preview and a genuine Python + Playwright suite.

## What's included

- Static portfolio website suitable for GitHub Pages.
- High-contrast dark engineering theme with prominent personal introduction and project case studies.
- Source explorer showing real Playwright code with an explanation of Arrange / Act / Assert.
- QA Lab preview: illustrative browser-side checks; it does **not** launch Python or real Playwright tests.
- Six real Playwright tests against a small local demo shop.
- GitHub Actions workflow that runs the browser tests on relevant pushes and pull requests, or manually.
- HTML and JUnit reports uploaded as workflow artifacts.

GitHub Pages is static hosting, so it cannot run Python Playwright on demand from a visitor's click. The portfolio deliberately separates its instant preview from real CI execution.

## Run locally

Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
mkdir -p reports
pytest -q --html=reports/report.html --self-contained-html --junitxml=reports/junit.xml
```

## GitHub Actions

1. Open the repository's **Actions** tab.
2. Select **Playwright QA Demo**.
3. Click **Run workflow**. It also runs for relevant pushes and pull requests.
4. Open the run to inspect logs and download the `playwright-test-reports` artifact.

The suite uses one Chromium browser, a small local page, six focused tests, and no arbitrary sleep calls in the tests. CI setup must still install Python packages and Chromium, so the whole workflow takes longer than the test execution itself.

## Enable GitHub Pages

1. Open **Settings → Pages**.
2. Under build and deployment, choose **Deploy from a branch**.
3. Select branch `main` and folder `/(root)`, then save.
4. Wait for deployment. The site URL should be `https://abdulrehmanofficialw-bit.github.io/Resume/`.

## Before sharing publicly

- Verify all CV facts and metrics.
- Add LinkedIn and any additional professional links you want public.
- Add only project links or screenshots you're allowed to share.
- Never publish employer source code, private tickets, confidential reports, credentials, or production data.
- Case studies describe work from the CV; they do not imply that public demo repositories already exist.

## Structure

```text
index.html
styles.css
app.js
README.md
requirements.txt
pytest.ini
tests/
  conftest.py
  test_demo_shop.py
  demo_app/index.html
.github/workflows/playwright.yml
```
