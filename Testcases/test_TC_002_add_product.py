from Lib import Configreader
from Base import InitiateDriver
from Pages import LoginPage
import pytest


def data_method():
    user_list=[["sabcfrds@gmail.com","Bhargav@6699"],["mohan2@abc.com","abc@1234"],["mohan1@abc.com","abc@1234"]]
    return user_list

pytest.mark.parametrize('inputdata',data_method())
def test_login(inputdata):
    driver=InitiateDriver.startBrowser()
    url=Configreader.readdata("login", "sit_url")
    driver.get(url)
    driver.maximize_window()

    login=LoginPage.LoginClass(driver)
    login.signinClick()
    login.enter_email(inputdata[0])
    login.enter_password(inputdata[1])
    login.click_submit()




