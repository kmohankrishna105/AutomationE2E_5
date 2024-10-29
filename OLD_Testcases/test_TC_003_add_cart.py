from selenium.webdriver.common.by import By
from Lib import Configreader

from Base import InitiateDriver

def test_login():
    driver=InitiateDriver.startBrowser()
    url=Configreader.readdata("login", "sit_url")
    driver.get(url)
    driver.maximize_window()

    signIn = driver.find_element(By.XPATH, Configreader.readdata("login", "sign_button"))
    signIn.click()

    loginEmail=Configreader.readdata("login","email")
    driver.find_element(By.XPATH,loginEmail).send_keys("sabcfrds@gmail.com")
    loginPassword = driver.find_element(By.XPATH, "//*[@id='pass']")
    loginPassword.send_keys("Bhargav@6699")
    driver.execute_script('scrollBy(0,200)')
    waitTime = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[ElementClickInterceptedException])

    signInButton = waitTime.until(EC.presence_of_element_located((By.XPATH, "(//*[@id='send2'])[1]")))

    time.sleep(5)
    # signInButton=driver.find_element(By.XPATH,"//*[@id="send2"]")
    signInButton.click()
    print("Ssuccessfull")

    time.sleep(2)
    # checking the welcome message
    wel_come_msg = "//span[@class='logged-in']"
    welcome_text = driver.find_element(By.XPATH, wel_come_msg).text
    b = 'Welcome, Bhargav Reddy Lakkireddy!'
    # assert b == welcome_text
    if welcome_text == b:
        print("Welcome message validation successfull")

    c = 'Welcome, Bhargav Reddy Lakkireddy'
    # checking with assert condition
    # assert welcome_text == c, "Problem with welcome message please check"
    try:
        assert welcome_text == c, "Problem with welcome message please check"
    except:
        print("There is an exception")
    e = 'Bhargav Reddy Lakkireddy'
    if e in welcome_text:
        print("User identified successfully")

    click_link = driver.find_element(By.XPATH, "//a[@role='menuitem'][*='Women']")
    click_link.click()
    driver.execute_script('scrollBy(0,400)')
    click_sublink = driver.find_element(By.XPATH, "//*[@id='narrow-by-list2']//li[1]/a")
    click_sublink.click()
    driver.execute_script('scrollBy(0,200)')
    driver.find_element(By.XPATH, "//a[@class='product-item-link']").click()
    print("Navigation to Product details page")
    driver.execute_script('scrollBy(0,400)')
    driver.find_element(By.XPATH, "//div[@option-label='S']").click()
    driver.find_element(By.XPATH, "//div[@option-label='Purple']").click()
    driver.execute_script('scrollBy(0,200)')
    driver.find_element(By.XPATH, "//button[@title='Add to Cart']").click()
    print("Product added t0 cart successfully")
    show_Cart = driver.find_element(By.CSS_SELECTOR, "a.action.showcart")
    show_Cart.click()
    pc_checkout = driver.find_element(By.XPATH, "//button[@title='Proceed to Checkout']")
    pc_checkout.click()
    print("Navigated to Checkout page")
    time.sleep(2)
    # driver.execute_script('scrollBy(0,600)')
    try:
        street_address = driver.find_element(By.XPATH, "//input[@name='street[0]']")
        # street_address.location_once_scrolled_into_view
        driver.execute_script("arguments[0].scrollIntoView();", street_address)
        street_address.clear()
        street_address.send_keys("Street1")

        city_name = driver.find_element(By.XPATH, "//input[@name='city']")
        city_name.clear()
        city_name.send_keys("mycity")

        select = Select(driver.find_element(By.XPATH, "//select[@name='region_id']"))
        # select by visible text
        region = "ALABAMA"
        # select.select_by_visible_text(region)
        # select.select_by_value(region)
        print("Address added successfully")

        post_code = driver.find_element(By.XPATH, "//input[@name='postcode']")
        post_code.clear()
        post_code.send_keys("50318")

        post_code = driver.find_element(By.XPATH, "//input[@name='telephone']")
        post_code.clear()
        post_code.send_keys("999666")
    except:
        print("Address added already")
        existing_address = driver.find_element(By.XPATH, "//div[@class ='shipping-address-item selected-item']").text
        print(existing_address)
    driver.execute_script('scrollBy(0,200)')



