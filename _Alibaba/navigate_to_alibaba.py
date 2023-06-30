from argparse import Action
from multiprocessing.context import SpawnContext
from tkinter import Button
from turtle import width
from selenium import webdriver
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

if __name__ == '__main__':
    URL = "https://www.alibaba.com/"
    driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
    actions = ActionChains(driver)
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(URL)
    print("getin")

    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//a[@title="Sign in"][@rel="nofollow"]'))))
    print("clicked1")
    login_id = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@class="fm-text"][@id="fm-login-id"]'))
    )
    login_id.clear()
    login_id.send_keys('in19026260965vxbw')
    print("wrote id")
    login_password = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@class="fm-text"][@id="fm-login-password"]'))
    )
    login_password.clear()
    login_password.send_keys('k3TV9!0R%$6e')
    login_password.send_keys(Keys.RETURN)
    print("wrote pass")
    driver.implicitly_wait(5)
    driver.switch_to.frame("baxia-dialog-content")
    slider = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//span[@class="nc_iconfont btn_slide"]')))
    move = ActionChains(driver)
    move.click_and_hold(slider).move_by_offset(350, 0).release().perform()  
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//input[@id="fm-login-submit"]'))))
    
    
    input_verify_code = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@id="J_Checkcode"]')))
    driver.implicitly_wait(5)
    val = input("Enter your value: ")
    driver.implicitly_wait(25)  
    input_verify_code.send_keys(val)
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(),"Submit")]'))))
    
    
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@class="fm-button fm-submit"]')))
    
    #My alibaba
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//a[@class="need-pre-check-login"][@title="My Alibaba"]'))))
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//i[@class="seller-menu-icon seller-menu-icon-message"]'))))
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div/div/div/div/ul/li/a/span[@title="Post Products"]'))))
    input_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@role="searchbox"]'))
    )
    input_element.send_keys('tractors')
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//i[@class="next-icon next-icon-search next-medium next-search-icon"]'))))
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//li[contains(text(), "Machinery >> Agricultural Machinery & Equipment >> Agricultural Machinery Parts")]'))))
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//button[@class="next-btn next-medium next-btn-primary"]'))))
    
    product_name_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@id="productTitle"]'))
    )
    product_name_str = "Part for JD JohnDeere Tractor, label Part Number " + "column A here!!!"
    product_name_input.send_keys(product_name_str)
    
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//button[@role="add-btn"]'))))
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//button[@role="add-btn"]'))))
    # product_keywords_inputs = WebDriverWait(driver, 5).until(
    #     EC.visibility_of_all_elements_located((By.XPATH, '//input[@type="text"][@role="input"]'))
    # )
    list_of_product_keywords_str = ["John -  deere parts agricultural machinery & equipment Agricultural Machinery Parts john deere tractor parts",
                                    "John - deere spare parts engine parts john deere tractor",
                                    "John - deere tractor spare parts john deere parts"
                                    ]
    for i in range(1, 4):
        product_key_input = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//input[@type="text"][@role="input"])[{str(i)}]')))
        product_key_input.send_keys(list_of_product_keywords_str[i])
    #product group
    # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//span[@class="next-select medium"]/i[@class="next-icon next-icon-arrow-down next-icon-small next-select-arrow"]'))))
    # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//a[@class="next-tree-node-handle"][contains(text(), "Johndeere")]'))))
    
    

    new_icon_btns = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//i[@class="next-icon next-icon-arrow-down next-icon-small next-select-arrow"]')))
    i = 0
    list_btns_str = ['//a[contains(text(), "Johndeere")]', '//div[contains(text(), "1 Year")]', '//div[contains(text(), "Provided")]', '//div[contains(text(), "Not Available")]', '//div[contains(text(), "New Product 2020")]', 'India', '//div[contains(text(), "New")]', ' ', '//div[contains(text(),"Tractors")]']
    for new_icon_btn in new_icon_btns :
        
        if (i != 5) & (i != 7) :
            driver.execute_script("arguments[0].click();",new_icon_btn)
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, list_btns_str[i]))))
        i = i + 1
        if (i == 5):
            input_tag = WebDriverWait(driver, 300).until(EC.presence_of_element_located(By.XPATH, '//input[@data-spm-anchor-id="a2700.post-publish.0.i39.17233e5fZGEygd"]'))
            input_tag.send_keys("India")
        if (i == 7):
            continue
        if i == 8 :
            break
    #Farm_checkbox
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//input[@data-spm-anchor-id="a2700.post-publish.0.i65.17233e5fZGEygd"]'))))
    #Machinery Repair Shops
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//input[@data-spm-anchor-id="a2700.post-publish.0.i68.17233e5fZGEygd"]'))))
    #construction works
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//input[@data-spm-anchor-id="a2700.post-publish.0.i73.17233e5fZGEygd"]'))))
    #India_checkbox
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//input[@data-spm-anchor-id="a2700.post-publish.0.i67.17233e5fZGEygd"]'))))
    print(1)