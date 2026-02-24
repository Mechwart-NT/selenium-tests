from selenium.webdriver.common.by import By

def room_zero(driver):
    username_input = driver.find_element(By.XPATH,'//*[@id="root"]/main/div[1]/input[1]')
    username_input.send_keys("admin")

    password_input = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[1]/input[2]')

    password_value = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[2]/div/div[2]/p[2]').get_attribute("textContent")

    password_input.send_keys(password_value)

    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[1]/button')
    
    login_button.click()

