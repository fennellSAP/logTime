from selenium import webdriver
import time
import datetime

driver = webdriver.Chrome(executable_path=r"C:\Users\I509049\Downloads\chromedriver_win32\chromedriver.exe")

def enterHours():

    global driver

    time.sleep(3)

    arrow = driver.find_element_by_xpath('//*[@id="__jsview1--idDetailIconTabBar--header-arrowScrollRight"]')
    arrow.click()

    time.sleep(2)
    
    entryBtn = driver.find_element_by_id("__filter3-icon")
    entryBtn.click()

    time.sleep(2)

    saveBtn = driver.find_element_by_xpath('//*[@id="__jsview1--detailsSaveButton"]')
    saveBtn.click()
    print("Time Has Been Entered")
        
def clickDateCell(dateXPath):

    global driver
    
    foundDateCell = False

    while not foundDateCell:

        try:
            
            dateCell = driver.find_element_by_xpath(dateXPath)
            dateCell.click()
            foundDateCell = True
        
        except:

            time.sleep(.5)

    enterHours()

def main():

    global driver

    driver.get("https://fiorilaunchpad.sap.com/sites#catsxt-create&/staffingUpdate/20190403")

    date = datetime.datetime.now()
    dateFormatted = date.strftime("%a") + "-" + date.strftime("%b") + "-" + date.strftime("%d") + "-" + date.strftime("%Y")
    dateXPath = '//*[@id="__jsview0--catsxtCalendar-' + dateFormatted + '"]'

    clickDateCell(dateXPath)

main()

