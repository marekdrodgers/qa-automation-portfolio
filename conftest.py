"""
Pytest fixtures and hooks for Selenium WebDriver setup and screenshot on failure.
"""

import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    """Initialize and yield a Chrome WebDriver instance, with optional headless mode."""
    options = ChromeOptions()
    # Optional headless toggle from CLI
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    service = ChromeService(ChromeDriverManager().install())
    driver_instance = webdriver.Chrome(service=service, options=options)
    driver_instance.implicitly_wait(5)

    yield driver_instance

    driver_instance.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to take screenshot on test failure."""
    _ = call  # mark as used to avoid pylint warning
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver_instance = item.funcargs.get("driver", None)
        if driver_instance:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = f"{screenshot_dir}/{item.name}.png"
            driver_instance.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved to {screenshot_path}")


def pytest_addoption(parser):
    """Add command-line option to run tests headlessly."""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests headlessly"
    )
