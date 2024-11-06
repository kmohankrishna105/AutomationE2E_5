from Base import InitiateDriver
from Pages import LoginPage

#technical or selenium code we divided business flow
#TO DO : You need to seperate test data from the code
def test_login():
    driver=InitiateDriver.startBrowser()
    login=LoginPage.LoginClass(driver)
    login.signinClick()
    login.enter_email("sabcfrds@gmail.com")
    login.enter_password("Bhargav@6699")
    login.click_submit()

"""


def data_method():
    user_list=[["sabcfrds@gmail.com","Bhargav@6699"],["mohan2@abc.com","abc@1234"],["mohan1@abc.com","abc@1234"]]
    return user_list

pytest.mark.parametrize("email,password",[("sabcfrds@gmail.com","Bhargav@6699"),("mohan2@abc.com","abc@1234"),])
def test_login(email,password):
    driver=InitiateDriver.startBrowser()
    login=LoginPage.LoginClass(driver)
    login.signinClick()
    login.enter_email(email)
    login.enter_password(password)
    login.click_submit()

def data_method():
    user_list=[["sabcfrds@gmail.com","Bhargav@6699"],["mohan2@abc.com","abc@1234"],["mohan1@abc.com","abc@1234"]]
    return user_list

pytest.mark.parametrize("inputdata1",data_method())
def test_login(inputdata1):
    driver=InitiateDriver.startBrowser()
    login=LoginPage.LoginClass(driver)
    login.signinClick()
    login.enter_email(inputdata1[0])
    login.enter_password(inputdata1[1])
    login.click_submit()
"""



