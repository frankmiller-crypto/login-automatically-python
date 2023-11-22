#-------------------------------------------------------------------------------
# Imports
import csv
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#-------------------------------------------------------------------------------
# Setup

username = 0
password = 1




with open('crunchyroll.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.maximize_window()
     
        driver.get('https://www.crunchyroll.com/offer-premium/login?utm_source=google&utm_medium=paid_cr&utm_campaign=CR-Paid_Google_Web_Conversion_LATAM_MX-CL_Trademark_SVOD&utm_term=crunchyroll&referrer=google_paid_cr_CR-Paid_Google_Web_Conversion_LATAM_MX-CL_Trademark_SVOD&gclid=EAIaIQobChMI_PWmhrbWggMVds3CBB3o-woXEAAYASAAEgK2QPD_BwE')

        time.sleep(2)
        username_field = driver.find_element(By.NAME, 'email')
        username_field.send_keys(line[0])

        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys(line[1])


        submit = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/form/div[2]')
        submit.click()
        time.sleep(5)

#-------------------------------------------------------------------------------
