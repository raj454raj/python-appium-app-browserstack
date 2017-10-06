from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

userName = "BROWSERSTACK_USERNAME"
accessKey = "BROWSERSTACK_ACCESS_KEY"

desired_caps = {"realMobile": True,
                "build": "Python iOS Local",
                "device": "iPhone 7",
                "browserstack.local": True,
                "automationName": "XCUITest",
                "app": "bs://<app_hashed_id>"}

hub_url = "http://%s:%s@hub-eu.browserstack.com/wd/hub" % (userName, accessKey)
driver = webdriver.Remote(hub_url, desired_caps)

test_button = driver.find_element_by_accessibility_id("TestBrowserStackLocal")
test_button.click()

def existence_lambda(s):
    result = s.find_element_by_accessibility_id("ResultBrowserStackLocal").get_attribute("value")
    return result and len(result) > 0

WebDriverWait(driver, 10).until(existence_lambda)

result_element = driver.find_element_by_accessibility_id("ResultBrowserStackLocal")
result_string = result_element.text.lower()


if result_string.__contains__("not working"):
    screenshot_file = "%s/screenshot.png" % os.getcwd()
    driver.save_screenshot(screenshot_file)
    print "Screenshot stored at %s" % screenshot_file
    raise Exception("Unexpected BrowserStackLocal test result")
else:
    assert(result_string.__contains__("up and running"))

driver.quit()
