from appium import webdriver

userName = "BROWSERSTACK_USERNAME"
accessKey = "BROWSERSTACK_ACCESS_KEY"

desired_caps = {"realMobile": True,
                "device": "Samsung Galaxy S6",
                "build": "Python Android",
                "app": "bs://<app_hashed_id>"}
driver = webdriver.Remote("http://" + userName + ":" + \
                          accessKey + "@hub.browserstack.com/wd/hub",
                          desired_caps)

search_element = driver.find_element_by_id("Search Wikipedia")
search_element.click()

search_input = driver.find_element_by_id("org.wikipedia.alpha:id/search_src_text")
search_input.send_keys("BrowserStack")

search_results = driver.find_elements_by_class_name("android.widget.TextView")
assert(len(search_results) > 0)

driver.quit()
