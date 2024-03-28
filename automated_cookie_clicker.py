import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

z = driver.find_element(By.ID, "langSelect-EN")
z.click()
time.sleep(2)

for i in range(30000):
    try:
        pole_pari = driver.find_element(By.ID, "cookies")
        text_od_kol = pole_pari.text
        pari_koj_gi_imame = int(text_od_kol.split()[0])

        try:
            pole_shipment = driver.find_element(By.ID, "productPrice8")
            pari_shipment = int(pole_shipment.text)
            if pari_koj_gi_imame >= pari_shipment:
                shipment = driver.find_element(By.ID, "product8")
                shipment.click()
        except:
            pass

        try:
            pole_wizard_tower = driver.find_element(By.ID, "productPrice7")
            pari_wizard_tower = int(pole_wizard_tower.text)
            if pari_koj_gi_imame >= pari_wizard_tower:
                wizard_tower = driver.find_element(By.ID, "product7")
                wizard_tower.click()
        except:
            pass

        try:
            pole_temple = driver.find_element(By.ID, "productPrice6")
            pari_temple = int(pole_temple.text)
            if pari_koj_gi_imame >= pari_temple:
                temple = driver.find_element(By.ID, "product6")
                temple.click()
        except:
            pass

        try:
            pole_bank = driver.find_element(By.ID, "productPrice5")
            pari_bank = int(pole_bank.text)
            if pari_koj_gi_imame >= pari_bank:
                bank = driver.find_element(By.ID, "product5")
                bank.click()
        except:
            pass

        try:
            pole_factory = driver.find_element(By.ID, "productPrice4")
            pari_factory = int(pole_factory.text)
            if pari_koj_gi_imame >= pari_factory:
                factory = driver.find_element(By.ID, "product4")
                factory.click()
        except:
            pass

        try:
            pole_mine = driver.find_element(By.ID, "productPrice3")
            pari_mine = int(pole_mine.text)
            if pari_koj_gi_imame >= pari_mine:
                mine = driver.find_element(By.ID, "product3")
                mine.click()
        except:
            pass

        try:
            pole_farm = driver.find_element(By.ID, "productPrice2")
            pari_farm = int(pole_farm.text)
            if pari_koj_gi_imame >= pari_farm:
                farm = driver.find_element(By.ID, "product2")
                farm.click()
        except:
            pass

        try:
            pole_baba = driver.find_element(By.ID, "productPrice1")
            pari_baba = int(pole_baba.text)
            if pari_koj_gi_imame >= pari_baba:
                baba = driver.find_element(By.ID, "product1")
                baba.click()
        except:
            pass

        try:
            pole_cursor = driver.find_element(By.ID, "productPrice0")
            pari_cursor = int(pole_cursor.text)
            if pari_koj_gi_imame >= pari_cursor:
                cursor = driver.find_element(By.ID, "product0")
                cursor.click()
        except:
            pass

        try:
            for j in range(9000):
                golemo_kopce = driver.find_element(By.ID, "bigCookie")
                golemo_kopce.click()
        except:
            pass

    except:
        pass


time.sleep(1000)
