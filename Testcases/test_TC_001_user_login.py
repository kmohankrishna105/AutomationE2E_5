import pytest

from Base import InitiateDriver

def test_login():
    driver=InitiateDriver.startBrowser()
    driver.get("https://magento.softwaretestingboard.com/")
    driver.maximize_window()

