from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

driver = webdriver.Chrome(executable_path=r"C:\Users\I509049\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://fiorilaunchpad.sap.com/sites#catsxt-create&/staffingUpdate/20190403")

date = datetime.datetime.now()
dateFormatted = date.strftime("%a") + "-" + date.strftime("%b") + "-" + date.strftime("%d") + "-" + date.strftime("%Y")
dateXPath = '//*[@id="__jsview0--catsxtCalendar-' + dateFormatted + '"]'


try:
    WebDriverWait(driver, 6).until(EC.presence_of_all_elements_located((By.XPATH, dateXPath)))
    driver.find_element_by_xpath(dateXPath).click()
except:
    print("Error finding date cell in calendar")


try:
    WebDriverWait(driver, 6).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="__jsview1--idDetailIconTabBar--header-arrowScrollRight"]')))
    driver.find_element_by_xpath('//*[@id="__jsview1--idDetailIconTabBar--header-arrowScrollRight"]').click()
except:
    print("Error finding arrow over button")


try:
    WebDriverWait(driver, 6).until(EC.presence_of_all_elements_located((By.ID, "__filter3-icon")))
    driver.find_element_by_id("__filter3-icon").click()

except:
    print("Error finding time entry section button")


try:
    WebDriverWait(driver, 6).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="__jsview1--detailsSaveButton"]')))
    driver.find_element_by_xpath('//*[@id="__jsview1--detailsSaveButton"]').click()
    print("Time Has Been Entered")

except:
    print("Error finding save button")





