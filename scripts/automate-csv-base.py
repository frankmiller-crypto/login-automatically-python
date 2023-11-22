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

with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.get('https://www.facebook.com')

        time.sleep(2)
        username_field = driver.find_element(By.NAME, 'email')
        username_field.send_keys(line[0])

        password_field = driver.find_element(By.NAME, 'pass')
        password_field.send_keys(line[1])


        submit = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
        submit.click()
        time.sleep(30)

#-------------------------------------------------------------------------------
