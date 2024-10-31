from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.ie.webdriver import WebDriver

from Lib import Configreader


def startBrowser():
    global driver
    #Configreader.readdata
    browser=Configreader.readdata('details','browser')
    if browser=='Chrome':
        path="C:\\Users\\user\\Downloads\\chromedriver.exe"
        serv_obj = Service(path)
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://magento.softwaretestingboard.com/")

    driver.maximize_window()
    print("Checking the server and url connection, DB connection established")
    print("Good to continue with the execution ")
    return driver


def closeBrowser():
    print("Close broweser")
    print("CLosing DB connection ")
