# QA Engineering Portfolio

Responsive high-contrast dark-themed portfolio for Abdul Rehman Rizwan, with an interactive browser-side QA lab preview and a genuine Python + Playwright suite.

## What's included

- Static portfolio website suitable for GitHub Pages.
- High-contrast dark engineering theme with prominent personal introduction and detailed project case studies, including Envirosoft Ticket Gap Analysis and Jira Ticket-to-Test Case Documentation.
- Source explorer showing real Playwright code with an explanation of Arrange / Act / Assert.
- QA Lab preview: illustrative browser-side checks; it does **not** launch Python or real Playwright tests.
- Six real Playwright tests against a small local demo shop.
- GitHub Actions workflow that runs the browser tests on relevant pushes and pull requests, or manually.
- HTML and JUnit reports uploaded as workflow artifacts.

GitHub Pages is static hosting, so it cannot run Python Playwright on demand from a visitor's click. The portfolio deliberately separates its instant preview from real CI execution.

## Featured QA case studies

### Envirosoft Ticket Gap Analysis

A Claude Project designed to analyze Envirosoft Jira tickets as a senior Business Analyst / Product Manager. It researches ticket descriptions, acceptance criteria, comments, linked issues, attachments, relevant Confluence documentation, related Jira tickets, project knowledge, and applicable public sources before drawing conclusions.

- Separates findings into **Answered**, **Derived**, **Open Question**, and **Risk**.
- Checks applicable scope, fields and validation, calculations, dates and periods, workflow, permissions, downstream dependencies, release constraints, and acceptance-criteria verifiability.
- Asks only high-value questions that sources cannot answer and that require a human decision; provides impact, recommended answer, owner, and blocking status.
- Identifies regression areas across shared components, reports, exports, APIs, integrations, downstream modules, existing data, client configuration, and historical defects.
- Prioritizes regression checks as High / Medium / Low and specifies measurable verification.
- Produces a structured report with plain-language summary, current-versus-new behavior, sourced requirements, questions, risks, regression areas, and references.
- Read-only by default; it does not edit Jira or Confluence unless explicitly requested. It labels assumptions and does not invent missing facts.

### Jira Ticket-to-Test Case Documentation

A questions-first workflow for turning a Jira ticket into lean scenarios and detailed Excel/CSV test cases.

- Reads ticket details, comments, linked issues, attachments, and supplied screenshots.
- Asks numbered requirement-gap questions before scenarios; blocking questions must be answered or explicitly recorded as assumptions.
- Generates concise, measurable scenarios, avoids duplicate coverage, and checks positive and applicable negative behavior for acceptance criteria.
- Exports `<TICKET>_Test_Cases.xlsx` and `<TICKET>_Test_Cases.csv`.
- Uses a seven-column test-case format: title, detailed description, precondition, main expected result, test step, test data, and step-level expected result. The workbook also includes an approved Scenarios sheet.
- Maintains traceability, uses measurable expected results, keeps Jira read-only, and produces a Knowledge to save block for manually updating product knowledge.

These case studies describe workflow design and documented capabilities; they do not expose employer source code, private tickets, customer information, or production data.

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
