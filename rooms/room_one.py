from selenium.webdriver.common.by import By


def room_one(driver):
    driver.implicitly_wait(5)
    generate_new_btn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/button[1]')
    print(generate_new_btn.get_attribute("textContent"))

    while(True):
        try:
            generate_new_btn.click()
        except:
            break
    
    end_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/button')
    end_button.click()