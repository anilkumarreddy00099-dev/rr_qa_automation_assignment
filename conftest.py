import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from configparser import ConfigParser

@pytest.fixture(scope="session")
def setup():
    config = ConfigParser()
    config.read("config/config.ini")
    browser = config.get("DEFAULT", "browser", fallback="chrome")
    base_url = config.get("DEFAULT", "base_url", fallback="https://tmdb-discover.surge.sh/")

    if browser.lower() == "chrome":
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise Exception(f"Unsupported browser: {browser}")

    # Open base URL
    driver.get(base_url)
    yield driver     # 👈 THIS LINE RETURNS THE DRIVER TO TESTS
    driver.quit()
