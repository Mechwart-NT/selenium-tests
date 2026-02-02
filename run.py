from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(headless=False):
    options = Options()
    options.add_experimental_option("detach", True)
    if headless:
        options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def test_google_title():
    driver = get_driver()
    driver.get("https://www.google.com")

    assert "Google" in driver.title

    # driver.quit()

test_google_title()