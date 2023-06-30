# import sys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager 
# import seleniumwire.undetected_chromedriver as uc
from django.conf import settings
from selenium import webdriver
import time as t
import pandas as pd
from twocaptcha import TwoCaptcha
from datetime import datetime
import  csv
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import os

captcha_api_key = '456c5c91597f30e8a985a29875d9e368'
solver = TwoCaptcha(captcha_api_key)
df = pd.read_csv("input.csv")
dat = []
delay = 3
# proxy = "http://8310929dba51dfe534aed15b7e2494f8ee4fe5cf:@proxy.zenrows.com:8001"
# proxies = {"http": proxy, "https": proxy}
# chrome_options = webdriver.ChromeOptions()
# seleniumwire_options = { 
# 	"proxy": { 
# 		"https": "https://8310929dba51dfe534aed15b7e2494f8ee4fe5cf:@proxy.zenrows.com:8001", 
# 		"verify_ssl": False, 
# 	}, 
# } 
# chrome_driver = uc.Chrome(options=chrome_options, seleniumwire_options=seleniumwire_options, version_main=109)
from zenrows import ZenRowsClient 
 
client = ZenRowsClient("8310929dba51dfe534aed15b7e2494f8ee4fe5cf") 
url = "https://wafid.com/book-appointment/" 
params = { 
	"js_render": "true", 
	"antibot": "true", 
	"premium_proxy": "true", 
} 
 
response = client.get(url, params=params) 
 
print(response.text)

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nirla.settings")
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# DJANGO_SETTINGS_MODULE=mysites.settings
settings.configure()
settings.CSRF_COOKIE_SECURE = True
settings.SESSION_COOKIE_SECURE = True

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
def test_lambdatest_google(da):
    for i in range(10, 20) :
        chrome_driver.execute_script(f"window.open('https://wafid.com/book-appointment/', '{i}th');")
    for i in range(10, 20) :
        chrome_driver.switch_to.window(f"{i}" + "th")
        data = da.iloc[(i - 1) % 10]
        chrome_driver.get('https://wafid.com/book-appointment/')
        print("initial")
        while chrome_driver.title != "Wafid | وافد":
            print("1try")
            chrome_driver.get('https://wafid.com/book-appointment/')
        print("2try")
        # try :
        #     WebDriverWait(chrome_driver, delay).until(EC.element_to_be_clickable((By.ID, 'id_country')))
        # except :
        #     chrome_driver.get('https://wafid.com/book-appointment/')
        #     if chrome_driver.title != "Wafid | وافد":
        #         chrome_driver.get('https://wafid.com/book-appointment/')
            # t.sleep(2)
            # try :
            #     chrome_driver.find_element(By.XPATH, "//label[@class='ctp-checkbox-label']/input").click()
            # except :
            #     pass
        WebDriverWait(chrome_driver, delay).until(EC.element_to_be_clickable((By.ID, 'id_country')))
        select_country = Select(chrome_driver.find_element(By.ID, "id_country"))
        select_country.select_by_visible_text(data["Country"])
        

        select_city = Select(chrome_driver.find_element(By.ID, "id_city"))
        select_city.select_by_visible_text(data["City"])

        select_traveling = Select(chrome_driver.find_element(By.ID, "id_traveled_country"))
        select_traveling.select_by_visible_text(data["Travelling to"])

        select_nationality = Select(chrome_driver.find_element(By.ID, "id_nationality"))
        select_nationality.select_by_visible_text(data["Nationality"])

        select_gender = Select(chrome_driver.find_element(By.ID, "id_gender"))
        select_gender.select_by_visible_text(data["Gender"])

        select_marital = Select(chrome_driver.find_element(By.ID, "id_marital_status"))
        select_marital.select_by_visible_text(data["Marital status"])

        select_Visa = Select(chrome_driver.find_element(By.ID, "id_visa_type"))
        select_Visa.select_by_visible_text(data["Visa Type"])

        select_position = Select(chrome_driver.find_element(By.ID, "id_applied_position"))
        select_position.select_by_visible_text(data["Position applied for"])

        firstName = chrome_driver.find_element(By.NAME, "first_name")
        firstName.send_keys(data["First Name"])

        lastName = chrome_driver.find_element(By.NAME, "last_name")
        lastName.send_keys(data["Last Name"])

        dob = chrome_driver.find_element(By.NAME, "dob")
        dob.send_keys(data["DOB"])

        passportN = chrome_driver.find_element(By.NAME, "passport")
        passportN.send_keys(data["Passport number"])

        passportC = chrome_driver.find_element(By.NAME, "confirm_passport")
        passportC.send_keys(data["Passport number"])

        passportIssueDate = chrome_driver.find_element(By.ID, "id_passport_issue_date")
        passportIssueDate.send_keys(data["Passport Issue date"])

        passportExpiryDate = chrome_driver.find_element(By.ID, "id_passport_expiry_on")
        passportExpiryDate.send_keys(data["Passport Expiry date"])
        
        passportIssuePlace = chrome_driver.find_element(By.ID, "id_passport_issue_place")
        passportIssuePlace.send_keys(data["Passport Issue place"])

        emailID = chrome_driver.find_element(By.NAME, "email")
        emailID.send_keys(data["Email"])
        print(type(data["Email"]))
        phoneN = chrome_driver.find_element(By.NAME, "phone")
        print(type(str(data["Phone"])))
        phoneN.send_keys("+"+str(data["Phone"]))

        nationalID = chrome_driver.find_element(By.NAME, "national_id")
        nationalID.send_keys(str(data["National ID"]))
        
        confirmB = chrome_driver.find_element(By.XPATH, ".//*[contains(text(), 'I confirm that the information given in this from is true, complete and accurate')]")
        confirmB.click()
        
        token_value = chrome_driver.find_element(By.XPATH, "//*[@id=\"id_captcha_0\"]").get_attribute('value')
        token_image = chrome_driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div/form/div[1]/div[7]/div/div/div/img").screenshot("temp.png")

        config = {
            'server':           '2captcha.com',
            'apiKey':           captcha_api_key,
            'softId':            123,
            'callback':         'https://wafid.com/book-appointment/',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
            }

        t.sleep(10)
        solver = TwoCaptcha(**config)
        t.sleep(5)

        id = solver.send(file='temp.png')
        # import time
        t.sleep(20)  # import time
        code = solver.get_result(id)
        print(code)
        input_token = chrome_driver.find_element(By.XPATH, "//*[@id=\"id_captcha_1\"]")
        input_token.send_keys(code)
        print("start")
        chrome_driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div/form/div[2]/div/div[2]/div/div[2]/button").click()
        print(code)
        t.sleep(10)
        print("end")
        # for p in [1, 3] :
        #     out_ = chrome_driver.find_element(By.XPATH, '//div[@class="left floated content"][contains(text(), "PassportNo:")]/parent::div[@class="item"]/div[@class="right floated content payment-confirmation-info-field"]').text
        #     out.append(out_)
        #     # out_email = chrome_driver.find_element(By.XPATH, f'//div[@class="right floated content payment-confirmation-info-field"][{str(2)}]')
        #     # out_passport = chrome_driver.find_element(By.XPATH, f'//div[@class="right floated content payment-confirmation-info-field"][{str(i)}]')
        #     # out_amount = chrome_driver.find_element(By.XPATH, f'//div[@class="right floated content payment-confirmation-info-field"][{str(4)}]')
        out_name = chrome_driver.find_element(By.XPATH, f'//div[@class="right floated content payment-confirmation-info-field"][{str(1)}]').text
        out_passport = chrome_driver.find_element(By.XPATH, '//div[@class="left floated content"][contains(text(), "PassportNo:")]/parent::div[@class="item"]/div[@class="right floated content payment-confirmation-info-field"]').text
        out_session = chrome_driver.current_url
        out_medical = "ALIF-LAM-MIM HEALTH SERVICES LTD "
        out_gcc = 91502202346136 * 100 + 10 * i + i
        out_matched = 46136 * 100 + 10 * i + i
        out_reference = "ARIF"
        out_time = datetime.now()
        dt = {"Passport No" : out_passport, 
            "Full Name" : out_name, 
            "Medical Center" : out_medical,
            "Session Link" : out_session,
            "GCC Slip No" : out_gcc,
            "MatchedSerial" : out_matched,
            "Referrence" : out_reference,
            "Save Time" : out_time}
        dat.append(dt)

test_lambdatest_google(df)

keys = dat[0].keys()

with open('people.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(dat)