from selenium.webdriver.common.by import By

from Lib import Configreader


class LoginClass:
    def __init__(self,obj):
        global driver
        driver=obj

    def signinClick(self):
        driver.find_element(By.XPATH, Configreader.readElement("login", "sign_button")).click()

    def enter_email(self,email):
        loginEmail = Configreader.readElement("login", "email")
        driver.find_element(By.XPATH, loginEmail).send_keys(email)

    def enter_password(self,password):
        loginPassword = Configreader.readElement("login", "password")
        driver.find_element(By.XPATH, loginPassword).send_keys(password)

    def click_submit(self):
        driver.execute_script('scrollBy(0,200)')
        submitButton = Configreader.readElement("login", "submit")
        driver.find_element(By.XPATH, submitButton).click()

    #def select_option(self):