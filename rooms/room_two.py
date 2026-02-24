from selenium.webdriver.common.by import By

def room_two(driver):
    driver.implicitly_wait(5)
    input_element = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/input')
    tipp_btn = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/button')
    for i in range(0,99):
        input_element.send_keys(i)
        tipp_btn.click()
        driver.implicitly_wait(5)
        result_h2 = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/h2')
        if "Eltaláltad" in result_h2.get_attribute("textContent"):
            break
        input_element.clear()

    driver.implicitly_wait(5)
    link = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/a')
    link.click()