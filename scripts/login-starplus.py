#-------------------------------------------------------------------------------
# Imports
import os.path
import csv
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
#-------------------------------------------------------------------------------
# Setup


with open('csv/data_starplus.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.maximize_window()
     
        driver.get('https://www.starplus.com/es-419/login')

        time.sleep(2)
        username_field = driver.find_element(By.NAME, 'email')
        username_field.send_keys(line[0])

        submit = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/main/div/form/div[2]/button')
        submit.click()
        time.sleep(2)

        password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/main/div/form/fieldset[2]/span/input')
        password_field.send_keys(line[1])


        submit = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/main/div/form/div/button')
        submit.click()
        time.sleep(5)

#-------------------------------------------------------------------------------
