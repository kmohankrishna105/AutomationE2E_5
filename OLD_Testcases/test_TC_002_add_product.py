from selenium.webdriver.common.by import By
from Lib import Configreader

from Base import InitiateDriver

def test_login():
    driver=InitiateDriver.startBrowser()
    url=Configreader.readdata("login", "sit_url")
    driver.get(url)
    driver.maximize_window()

    signIn = driver.find_element(By.XPATH, Configreader.readElement("login", "sign_button"))
    signIn.click()

    loginEmail=Configreader.readElement("login","email")
    driver.find_element(By.XPATH,loginEmail).send_keys("sabcfrds@gmail.com")


