# QA Automation Portfolio

## Overview
This repository is my QA Automation portfolio where I practice and demonstrate skills including:

- Manual and automated testing fundamentals
- Python scripting and test automation with pytest
- API testing (basic GET requests and mocking)
- Load testing basics with Locust and analysis of results
- Writing clean, documented, and maintainable test code following PEP 8 standards
- Managing code with Git, including commits and pushing to GitHub
- UI test automation with Selenium WebDriver including page object models and robust waits

## Progress so far
- Set up Python environment with virtualenv and pylint
- Created reusable test functions and modular code in `/src` and `/tests`
- Implemented API tests with live endpoints and mocked responses
- Performed load testing and documented results with markdown and charts
- Applied coding standards including module and function docstrings
- Learned basic git workflow: staging, committing, pushing, and branching
- Added Selenium-based UI tests for DuckDuckGo search:
  - Used Page Object Model (POM) for maintainable UI tests
  - Implemented explicit waits and expected conditions for reliability
  - Handled element click interception issues with ActionChains and scrolling
  - Parameterized tests using pytest.mark.parametrize for varied inputs
  - Configured WebDriver setup/teardown using pytest fixtures in `conftest.py`
- Added additional test example for Google Search UI automation

## Next steps
- Add authenticated API testing
- Deepen UI test automation skills (e.g., Playwright, Cypress)
- Expand test coverage and robustness for UI tests
- Build a full test framework and integrate continuous integration pipelines
- Explore parallel test execution and reporting tools

---

Feel free to explore the code and tests in the `/src` and `/tests` directories.

---

*Last updated: 2025-06-15*
