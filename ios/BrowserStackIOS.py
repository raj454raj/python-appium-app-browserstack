from appium import webdriver

userName = "BROWSERSTACK_USERNAME"
accessKey = "BROWSERSTACK_ACCESS_KEY"

desired_caps = {"realMobile": True,
                "build": "Python iOS",
                "device": "iPhone 7",
                "automationName": "XCUITest",
                "app": "bs://<app_hashed_id>"}

hub_url = "http://%s:%s@hub-eu.browserstack.com/wd/hub" % (userName, accessKey)
driver = webdriver.Remote(hub_url, desired_caps)

login_button = driver.find_element_by_id("Log In")
login_button.click()

email_input = driver.find_element_by_id("Email address")
email_input.click()

email_input.send_keys("hello@browserstack.com")
driver.find_element_by_accessibility_id("Next").click()

text_elements = driver.find_elements_by_xpath("//XCUIElementTypeStaticText")
assert(len(text_elements) > 0)
elements = filter(lambda x: x.__contains__("not registered"),
                  [x.text for x in text_elements])
assert(len(elements) > 0)
driver.quit()
