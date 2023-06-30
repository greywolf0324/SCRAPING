import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import pandas as pd
import urllib


dat = pd.read_csv("parts_not_found.csv")
partnums = list(dat["03M7307"])
partnums.append("03M7307")
content = list(dat["BOLT, RD HD SQ SHORT NECK, METRIC"])
content.append("BOLT, RD HD SQ SHORT NECK, METRIC")

os.mkdir("scraped_data")

if __name__ == '__main__':
    URL = "https://partscatalog.deere.com/jdrc/"
    driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    for partnum in partnums:
        for p in range(1, 11):
            driver.get(URL)
            print("came in.")
            try:
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//button[@class="primary"]'))))
                print("primary key tried.")
            except:
                pass
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, '//button[@class="primary selectpicker form-control selectButton ng-star-inserted"]'))))
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div/a[@class="searchOptions"][contains(text(),"Part Number")]'))))
            input_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//span/input[@class="ng-tns-c64-14 p-autocomplete-input p-inputtext p-component ng-star-inserted"]'))
            )
            input_element.send_keys(partnum)
            print("input")
            input_element.send_keys(Keys.RETURN)
            print("return")
            try:
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="primary"]'))))
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, '//button[@class="primary selectpicker form-control selectButton ng-star-inserted"]'))))
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div/a[@class="searchOptions"][contains(text(),"Part Number")]'))))
                input_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//span/input[@class="ng-tns-c64-14 p-autocomplete-input p-inputtext p-component ng-star-inserted"]'))
                )
                input_element.send_keys(partnum)
                print("input")
                input_element.send_keys(Keys.RETURN)
                print("return")
            except:
                pass
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'//div/a[@class="ng-star-inserted"][{str(p)}]'))))
            img_btns = WebDriverWait(driver, 200).until(EC.presence_of_all_elements_located((By.XPATH, '//div/img[@class="dpr2 img-responsive"]')))
            print(len(img_btns))
            os.mkdir(f'scraped_data/{partnum}')
            os.mkdir(f"scraped_data/{partnum}/image")
            os.mkdir(f"scraped_data/{partnum}/csv_files")
            for i in range(1, len(img_btns) + 1):
                ele =WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//div/img[@class="dpr2 img-responsive"])[{str(i)}]')))
                urllib.request.urlretrieve(str(ele.get_attribute("src")), f'scraped_data/{partnum}/image/{i}.jpg')
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//div/img[@class="dpr2 img-responsive"])[{str(i)}]'))))
                part_btns = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="partDesc"]')))
                print(len(part_btns))
                temp_description = []
                temp_weight = []
                temp_partnumber = []
                for j in range(1, len(part_btns) + 1):

                    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//a[@class="partDesc"])[{str(j)}]'))))
                    try:
                        description = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-xs-12 col-sm-9 col-md-9 col-lg-9 col-xl-9 paddeddivs ng-star-inserted"]')))
                    except:
                        try:
                            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="primary"]'))))
                            description = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-xs-12 col-sm-9 col-md-9 col-lg-9 col-xl-9 paddeddivs ng-star-inserted"]')))
                        except:
                            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//button[@class="secondary cartbtn ctnButtonMultiplePartPadding"]'))))
                            continue
                    print("printed description : ", description.text, type(description.text), type(description))
                    
                    try :
                        weight = driver.find_element(By.XPATH, '//table[@class="table table-striped shippinginfotable"]/tbody/tr/td[@width="60%"]')
                        # weight = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//table[@class="table table-striped shippinginfotable"]/tbody/tr/td[@width="60%"]')))
                        temp_weight.append(weight.text)
                        print("weight : ", weight.text, type(weight.text), type(weight))
                    except:
                        print("no weight element in ", j)
                        temp_weight.append(None)
                    partnumber = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="partnumbertext"]')))
                    temp_description.append(description.text)
                    temp_partnumber.append(partnumber.text)            
                    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//button[@class="secondary cartbtn ctnButtonSinglePartPadding"]'))))
                    print(j)
                tem = {"description" : temp_description, "weight" : temp_weight, "partnumber" : temp_partnumber}
                df = pd.DataFrame(tem)
                df.to_csv(f"scraped_data/{partnum}/csv_files/{i}.csv")
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//button[@class="secondary ng-star-inserted"]'))))
                print(i)
            print(1)
            driver.close()