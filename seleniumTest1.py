__author__ = 'moisessiles'


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefox()
desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
desired_capabilities['platform'] = 'Windows 8'
desired_capabilities['name'] = 'Useful Python commands'
# http://saucelabs.com/docs/additional-config
desired_capabilities['tags'] = ['cloud', 'testing']

sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
driver = webdriver.Remote(desired_capabilities=desired_capabilities, command_executor=sauce_url % ("msiles", "3d1aec67-5936-4898-ba6b-0bc50e8990ba"))

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
driver.quit()