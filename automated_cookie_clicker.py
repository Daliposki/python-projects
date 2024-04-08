import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

c = driver.find_element(By.ID, "langSelect-EN")
c.click()
time.sleep(2)

for i in range(30000):
    try:
        column_money = driver.find_element(By.ID, "cookies")
        text_of_cookies = column_money.text
        money_we_have = int(text_of_cookies.split()[0])

        try:
            column_shipment = driver.find_element(By.ID, "productPrice8")
            money_shipment = int(column_shipment.text)
            if money_we_have >= money_shipment:
                shipment = driver.find_element(By.ID, "product8")
                shipment.click()
        except:
            pass

        try:
            column_wizard_tower = driver.find_element(By.ID, "productPrice7")
            money_wizard_tower = int(column_wizard_tower.text)
            if money_we_have >= money_wizard_tower:
                wizard_tower = driver.find_element(By.ID, "product7")
                wizard_tower.click()
        except:
            pass

        try:
            column_temple = driver.find_element(By.ID, "productPrice6")
            money_temple = int(column_temple.text)
            if money_we_have >= money_temple:
                temple = driver.find_element(By.ID, "product6")
                temple.click()
        except:
            pass

        try:
            column_bank = driver.find_element(By.ID, "productPrice5")
            money_bank = int(column_bank.text)
            if money_we_have >= money_bank:
                bank = driver.find_element(By.ID, "product5")
                bank.click()
        except:
            pass

        try:
            column_factory = driver.find_element(By.ID, "productPrice4")
            money_factory = int(column_factory.text)
            if money_we_have >= money_factory:
                factory = driver.find_element(By.ID, "product4")
                factory.click()
        except:
            pass

        try:
            column_mine = driver.find_element(By.ID, "productPrice3")
            money_mine = int(column_mine.text)
            if money_we_have >= money_mine:
                mine = driver.find_element(By.ID, "product3")
                mine.click()
        except:
            pass

        try:
            column_farm = driver.find_element(By.ID, "productPrice2")
            money_farm = int(column_farm.text)
            if money_we_have >= money_farm:
                farm = driver.find_element(By.ID, "product2")
                farm.click()
        except:
            pass

        try:
            column_grandmother = driver.find_element(By.ID, "productPrice1")
            money_grandmother = int(column_grandmother.text)
            if money_we_have >= money_grandmother:
                grandmother = driver.find_element(By.ID, "product1")
                grandmother.click()
        except:
            pass

        try:
            column_cursor = driver.find_element(By.ID, "productPrice0")
            money_cursor = int(column_cursor.text)
            if money_we_have >= money_cursor:
                cursor = driver.find_element(By.ID, "product0")
                cursor.click()
        except:
            pass

        try:
            for j in range(9000):
                big_cookie = driver.find_element(By.ID, "bigCookie")
                big_cookie.click()
        except:
            pass

    except:
        pass


time.sleep(1000)
