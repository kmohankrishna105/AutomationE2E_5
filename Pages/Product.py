import time

from selenium.webdriver.common.by import By

from Lib import Configreader


class ProductClass:
    def __init__(self,obj):
        global driver
        driver=obj

    def Click_women_link(self):
        driver.execute_script('scrollBy(0,400)')
        click_link = driver.find_element(By.XPATH, "//a[@role='menuitem'][*='Women']")
        click_link.click()


    def select_product(self):
        driver.execute_script('scrollBy(0,600)')
        click_sublink = driver.find_element(By.XPATH, "//*[@id='narrow-by-list2']//li[1]/a")
        click_sublink.click()

    def select_subproduct(self):
        time.sleep(2)
        driver.execute_script('scrollBy(0,500)')
        driver.find_element(By.XPATH, "//a[@class='product-item-link']").click()

    def select_size(self,size):
        driver.execute_script('scrollBy(0,800)')
        driver.find_element(By.XPATH, "//div[@option-label='"+size+"']").click()
        driver.find_element(By.XPATH, "//div[@option-label='Purple']").click()
