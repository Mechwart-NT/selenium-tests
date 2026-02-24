from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from rooms.room_zero import room_zero
from rooms.room_one import room_one
from rooms.room_two import room_two


def get_driver(headless=False):
    options = Options()
    options.add_experimental_option("detach", True)
    if headless:
        options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def start_bot():
    driver = get_driver()
    driver.get("https://csati.nemestamas.hu/")

    room_zero(driver)
    room_one(driver)
    room_two(driver)
    # driver.quit()

start_bot()