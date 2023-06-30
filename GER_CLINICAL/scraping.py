import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd



if __name__ == '__main__':

    URL = "https://www.deutsches-krankenhaus-verzeichnis.de/app/suche/bundesland"
    driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(URL)
    df = pd.DataFrame(columns = ["clinicname", "Fälle", "Betten", "titel", "Vorname", "name", "Position", "Telefon", "fax", "email", "homepage", "Hausnummer", "Ort", "Department", "Region"])

    for i in range(1, 17):
        region = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//a[@class="js_state btn btn-link"])[{str(i)}]')))
        #region
        region = region.text
        print("region")
        print(region)
        print(type(region))
        aa = region
        print("######################")
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//a[@class="js_state btn btn-link"])[{str(i)}]'))))
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//a[@role="tab"]'))))
        
        orts = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="list-group-item"]')))

        for j in range(1, int(len(list(orts)) / 2) + 1):
            #ort
            ort = (WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//a[@class="list-group-item"])[{str(j)}]')))).text
            print("ort")
            bb = ort
            print(ort)
            # print(type(ort))
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//a[@class="list-group-item"])[{str(j)}]'))))
            print("################")
            weiter = driver.find_elements(By.XPATH, '//a[contains(text(),"Weiter")]')
            print("weiter:::::::::::::::", weiter)
            counts = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//h4[contains(text(),"Treffer" )]/span')))
            counts = counts.text
            counts = int(counts)
            print("#####################################")
            print("counts : ", counts)
            print("#####################################")
            
            while counts > 20:
                # clis = driver.find_elements(By.XPATH, '//address/strong/a')
                print("get in while.")
                for k in range(1, 21):
                    print("print k:::::::::::", k)
                    clinic_name = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//address/strong/a)[{str(k)}]')))
                    # print("clinic_name")
                    print(clinic_name.text)
                    # print(type(clinic_name.text))
                    cc = clinic_name.text
                    # clinicnamee.append(clinic_name.text)
                    print("################")
                    #click clinic
                    driver.implicitly_wait(3)
                    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//address/strong/a)[{str(k)}]'))))
                    #hausnummer
                    hausnummer = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '(//section[@class="head"]/div/div/p)[1]')))
                    # print("hausnummer")
                    print(hausnummer.text)
                    # print(type(hausnummer.text))
                    dd = hausnummer.text
                    print("################")
                    #homepage
                    homepage = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//a[@class="btn btn-link url"]/span')))
                    # print("homepage")
                    print(homepage.text)
                    # print(type(homepage.text))
                    ee = homepage.text
                    # homepagee.append(homepage.text)
                    print("################")
                    #info
                    # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Unternehmen")]'))))
                    # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Allgemeine Kontaktdaten des Krankenhauses")]'))))
                    #   #fax
                    # un1 = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//div[@class="col-sm-8"]/p)[2]')))
                    # print("fax")
                    # print(un1.text)
                    # print("################")
                    #department
                    print("departments")
                    # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Fachabteilungen")]'))))
                    try:
                        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Fachabteilungen")]'))))
                    except:
                        temp = {"clinicname" : [cc], "Fälle" : [""], "Betten" : [""], "titel" : [""], "Vorname" : [""], "name" : [""], "Position" : [""], "Telefon" : [""], "fax" : [" "], "email" : [""], "homepage" : [ee], "Hausnummer" : [dd], "Ort" : [bb], "Department" : [""], "Region" : [aa]}
                        temp = pd.DataFrame(temp)
                        df = df.append(temp)
                        #back
                        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Zurück zu den Suchergebnissen")]'))))
                        continue
                    # departments = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="panel-collapse collapse in"]/div/ul/li/a')))
                    
                    # for k in range(1, len(list(departments)) + 1):
                    department = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@class="panel-collapse collapse in"]/div/ul'))).text
                    print(department)
                    # print(type(department))
                    ff = department
                    # departmentt.append(department)
                    print("#############################")
                    #personal
                    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Unternehmen")]'))))
                    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Ärztliche Leitung")]'))))
                    #titel, vorname, name
                    print("all")
                    all = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '(//a/span[contains(text(), "Ärztliche Leitung")]/../../../div[@class="panel-collapse collapse in"]/div/div/div/p)[1]')))
                    print(all.text)
                    if len(all.text.split()) == 4 :
                        print(all.text.split()[0])
                        print(all.text.split()[1])
                        print(type(all.text.split()[0] + " " + all.text.split()[1]))
                        gg = all.text.split()[0] + " " + all.text.split()[1]
                        # titell.append(all.text.split()[0] + " " + all.text.split()[1])
                        print(all.text.split()[2])
                        print(type(all.text.split()[2]))
                        hh = all.text.split()[2]
                        # vornamee.append(all.text.split()[2])
                        print(all.text.split()[3])
                        print(type(all.text.split()[3]))
                        ii = all.text.split()[3]
                    else :
                        gg = " "
                        hh = " "
                        ii = ""
                        for q in range(len(all.text.split())) :
                            ii += all.text.split()[q]

                    # namee.append(all.text.split()[3])
                    print("#################################")
                    #position
                    # print("Position")
                    Position = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '(//a/span[contains(text(), "Ärztliche Leitung")]/../../../div[@class="panel-collapse collapse in"]/div/div/div/p)[2]')))
                    print(Position.text)
                    # print(type(Position.text))
                    jj = Position.text
                    # positionn.append(Position.text)
                    print("#####################")
                    #tel, mail, fax
                    tel = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '(//a/span[contains(text(), "Ärztliche Leitung")]/../../../div[@class="panel-collapse collapse in"]/div/div/div/p[4]/a)[1]')))
                    # print("tel")
                    print(tel.text)
                    # print(type(tel.text))
                    kk = tel.text
                    # telee.append(tel.text)
                    print("#########################")
                    mail = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '(//a/span[contains(text(), "Ärztliche Leitung")]/../../../div[@class="panel-collapse collapse in"]/div/div/div/p[4]/a)[2]')))
                    # print("mail")
                    print(mail.text)
                    # print(type(mail.text))
                    ll = mail.text
                    # emaill.append(mail.text)
                    print("##########################")
                    #back
                    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Zurück zu den Suchergebnissen")]'))))
                    #falle
                    falle = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//address/../../td)[{str(6*(k - 1) + 4)}]')))
                    # print("falle")
                    print(falle.text)
                    # print(type(falle.text))
                    mm = falle.text
                    # fallee.append(falle.text)
                    print("################")
                    #betten
                    betten = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//address/../../td)[{str(6*(k - 1) + 3)}]')))
                    # print("betten")
                    print(betten.text)
                    # print(type(betten.text))
                    nn = betten.text
                    # bettenn.append(betten.text)
                    print("################")
                    temp = {"clinicname" : [cc], "Fälle" : [mm], "Betten" : [nn], "titel" : [gg], "Vorname" : [hh], "name" : [ii], "Position" : [jj], "Telefon" : [kk], "fax" : [" "], "email" : [ll], "homepage" : [ee], "Hausnummer" : [dd], "Ort" : [bb], "Department" : [ff], "Region" : [aa]}
                    temp = pd.DataFrame(temp)
                    df = df.append(temp)
                print("uhaha............................................................")
                weiter = driver.find_element(By.XPATH, '//a[contains(text(),"Weiter")]')
                weiter.click()
                counts = counts  - 20
                print("#####################################")
                print("counts : ", counts)
                print("#####################################")


            for k in range(1, counts + 1):
                print("get in for!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("print k:::::::::::", k)
                driver.implicitly_wait(3)
                clinic_name = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//address/strong/a)[{str(k)}]')))
                # print("clinic_name")
                print(clinic_name.text)
                # print(type(clinic_name.text))
                cc = clinic_name.text
                # clinicnamee.append(clinic_name.text)
                print("################")
                #click clinic
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//address/strong/a)[{str(k)}]'))))
                #hausnummer
                hausnummer = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '(//section[@class="head"]/div/div/p)[1]')))
                # print("hausnummer")
                print(hausnummer.text)
                # print(type(hausnummer.text))
                dd = hausnummer.text
                # hausnummerr.append(hausnummer.text)
                print("################")
                # # telefon,
                # te = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '(//section[@class="head"]/div/div/p)[2]/a')))
                # print(te[0].text)
                # print("################")
                # #fax
                # fax = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '(//section[@class="head"]/div/div/p)[2]')))
                # print(fax[0].text)
                # print("################")
                #homepage
                homepage = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//a[@class="btn btn-link url"]/span')))
                # print("homepage")
                print(homepage.text)
                # print(type(homepage.text))
                ee = homepage.text
                # homepagee.append(homepage.text)
                print("################")
                #info
                # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Unternehmen")]'))))
                # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Allgemeine Kontaktdaten des Krankenhauses")]'))))
                #   #fax
                # un1 = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//div[@class="col-sm-8"]/p)[2]')))
                # print("fax")
                # print(un1.text)
                # print("################")
                #department
                print("departments")
                try:
                    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Fachabteilungen")]'))))
                except:
                    temp = {"clinicname" : [cc], "Fälle" : [""], "Betten" : [""], "titel" : [""], "Vorname" : [""], "name" : [""], "Position" : [""], "Telefon" : [""], "fax" : [" "], "email" : [""], "homepage" : [ee], "Hausnummer" : [dd], "Ort" : [bb], "Department" : [""], "Region" : [aa]}
                    temp = pd.DataFrame(temp)
                    df = df.append(temp)
                    #back
                    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Zurück zu den Suchergebnissen")]'))))
                    continue
                # departments = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="panel-collapse collapse in"]/div/ul/li/a')))
                
                # for k in range(1, len(list(departments)) + 1):
                department = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@class="panel-collapse collapse in"]/div/ul'))).text
                print(department)
                # print(type(department))
                ff = department
                # departmentt.append(department)
                print("#############################")
                #personal
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Unternehmen")]'))))
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Ärztliche Leitung")]'))))
                #titel, vorname, name
                print("all")
                all = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '(//a/span[contains(text(), "Ärztliche Leitung")]/../../../div[@class="panel-collapse collapse in"]/div/div/div/p)[1]')))
                print(all.text)
                if len(all.text.split()) == 4 :
                    print(all.text.split()[0])
                    print(all.text.split()[1])
                    # print(type(all.text.split()[0] + " " + all.text.split()[1]))
                    gg = all.text.split()[0] + " " + all.text.split()[1]
                    # titell.append(all.text.split()[0] + " " + all.text.split()[1])
                    print(all.text.split()[2])
                    # print(type(all.text.split()[2]))
                    hh = all.text.split()[2]
                    # vornamee.append(all.text.split()[2])
                    print(all.text.split()[3])
                    # print(type(all.text.split()[3]))
                    ii = all.text.split()[3]
                else :
                    gg = " "
                    hh = " "
                    ii = ""
                    for q in range(len(all.text.split())) :
                        ii += all.text.split()[q]

                # namee.append(all.text.split()[3])
                print("#################################")
                #position
                # print("Position")
                Position = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '(//a/span[contains(text(), "Ärztliche Leitung")]/../../../div[@class="panel-collapse collapse in"]/div/div/div/p)[2]')))
                print(Position.text)
                # print(type(Position.text))
                jj = Position.text
                # positionn.append(Position.text)
                print("#####################")
                #tel, mail, fax
                tel = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '(//a/span[contains(text(), "Ärztliche Leitung")]/../../../div[@class="panel-collapse collapse in"]/div/div/div/p[4]/a)[1]')))
                # print("tel")
                print(tel.text)
                # print(type(tel.text))
                kk = tel.text
                # telee.append(tel.text)
                print("#########################")
                mail = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '(//a/span[contains(text(), "Ärztliche Leitung")]/../../../div[@class="panel-collapse collapse in"]/div/div/div/p[4]/a)[2]')))
                # print("mail")
                print(mail.text)
                # print(type(mail.text))
                ll = mail.text
                # emaill.append(mail.text)
                print("##########################")
                #back
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Zurück zu den Suchergebnissen")]'))))
                #falle
                falle = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//address/../../td)[{str(6*(k - 1) + 4)}]')))
                # print("falle")
                print(falle.text)
                # print(type(falle.text))
                mm = falle.text
                # fallee.append(falle.text)
                print("################")
                #betten
                betten = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//address/../../td)[{str(6*(k - 1) + 3)}]')))
                # print("betten")
                print(betten.text)
                # print(type(betten.text))
                nn = betten.text
                # bettenn.append(betten.text)
                print("################")
                temp = {"clinicname" : [cc], "Fälle" : [mm], "Betten" : [nn], "titel" : [gg], "Vorname" : [hh], "name" : [ii], "Position" : [jj], "Telefon" : [kk], "fax" : [" "], "email" : [ll], "homepage" : [ee], "Hausnummer" : [dd], "Ort" : [bb], "Department" : [ff], "Region" : [aa]}
                temp = pd.DataFrame(temp)
                df = df.append(temp)
            driver.get(URL)
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, f'(//a[@class="js_state btn btn-link"])[{str(i)}]'))))
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//a[@role="tab"]'))))
        driver.get(URL)
    df.to_excel("final.xlsx")