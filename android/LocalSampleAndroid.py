from appium import webdriver

userName = "BROWSERSTACK_USERNAME"
accessKey = "BROWSERSTACK_ACCESS_KEY"

desired_caps = {"realMobile": True,
                "device": "Samsung Galaxy S6",
                "build": "Python Android Local",
                "browserstack.local": True,
                "app": "bs://<app_hashed_id>"}
driver = webdriver.Remote("http://" + userName + ":" + \
                          accessKey + "@hub.browserstack.com/wd/hub", 
                          desired_caps)

search_element = driver.find_element_by_id("com.example.android.basicnetworking:id/test_action")
search_element.click()

test_element = None
search_results = driver.find_elements_by_class_name("android.widget.TextView")
for result in search_results:
    if result.text.__contains__("The active connection is"):
        test_element = result.text

if test_element is None:
    raise Exception("Cannot find the needed TextView element from app")

assert(test_element.__contains__("The active connection is wifi"))
assert(test_element.__contains__("Up and running"))

driver.quit()
