from bs4 import BeautifulSoup
import requests as req
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://rus-ege.sdamgia.ru/")
time.sleep(5)
login = driver.find_element(By.NAME, 'email').send_keys('george342kurus@gmail.com')
time.sleep(1)
passwrd = driver.find_element(By.NAME, 'password').send_keys('George8888kurushin')
time.sleep(1)
login_btn = driver.find_element(By.mro(), 'Button_view_default ProfileAuth-Button').click()
time.sleep(10)


driver.close()

