import pytest

from Base import InitiateDriver

@pytest.mark.login
def test_login():
    driver=InitiateDriver.startBrowser()
    driver.get("https://magento.softwaretestingboard.com/")
    driver.maximize_window()

