from selenium.webdriver.common.by import By
from Lib import Configreader

from Base import InitiateDriver
from Pages import LoginPage


def test_login():
    driver=InitiateDriver.startBrowser()
    url=Configreader.readdata("login", "sit_url")
    driver.get(url)
    driver.maximize_window()

    signIn = driver.find_element(By.XPATH, Configreader.readElement("login", "sign_button"))
    signIn.click()

    login=LoginPage.LoginClass(driver)
    login.enter_email("sabcfrds@gmail.com")



