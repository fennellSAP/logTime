from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import datetime

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)

def clickSomething(selector):

    foundElement = False

    while not foundElement:

        try:
            driver.find_element_by_xpath(selector).click()
            foundElement = True
            return
        
        except: 
            time.sleep(.5)


def findSectionBtn(selector):

    foundElement = False

    while not foundElement:

        try:
            driver.find_element_by_id(selector).click()
            foundElement = True
            return
        
        except: 
            time.sleep(.5)


def enterTime():

    driver.get("https://fiorilaunchpad.sap.com/sites#catsxt-create&/staffingUpdate/20190403")
    date = datetime.datetime.now()
    dateFormatted = date.strftime("%a") + "-" + date.strftime("%b") + "-" + date.strftime("%d") + "-" + date.strftime("%Y")
    dateXPath = '//*[@id="__jsview0--catsxtCalendar-' + dateFormatted + '"]'

    # Click date cell
    clickSomething(dateXPath)

    # Click arrow right
    clickSomething('//*[@id="__jsview1--idDetailIconTabBar--header-arrowScrollRight"]')

    # Click time entry section
    findSectionBtn('__filter3-text')

    # Wait for popup to go away
    time.sleep(3)

    # Click save button
    clickSomething('//*[@id="__jsview1--detailsSaveButton"]')

    print("Time Has Been Entered!")

enterTime()






