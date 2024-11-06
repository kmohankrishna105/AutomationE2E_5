from Lib import Configreader
from Base import InitiateDriver
from Pages import LoginPage
import pytest


pytest.mark.parametrize("email,password",[("sabcfrds@gmail.com","Bhargav@6699"),("mohan2@abc.com","abc@1234"),])
def test_login(email,password):
    driver=InitiateDriver.startBrowser()
    login=LoginPage.LoginClass(driver)
    login.signinClick()
    login.enter_email(email)
    login.enter_password(password)
    login.click_submit()