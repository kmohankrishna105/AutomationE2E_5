from selenium.webdriver.common.by import By

from Lib import Configreader


class LoginClass:
    def __init__(self,obj):
        global driver
        driver=obj

    def enter_email(self,email):
        loginEmail = Configreader.readElement("login", "email")
        driver.find_element(By.XPATH, loginEmail).send_keys("sabcfrds@gmail.com")

