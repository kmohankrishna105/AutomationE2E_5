def Take_Screenshot(driver,name):
    driver.get_screenshot_as_file("../Screenshots//" + name + ".png")
