import os
import sys
import new
import unittest
from selenium import webdriver
from sauceclient import SauceClient

# it's best to remove the hardcoded defaults and always get these values
# from environment variables
USERNAME = os.environ.get('SAUCE_USERNAME', "msiles")
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', "3d1aec67-5936-4898-ba6b-0bc50e8990ba")
sauce = SauceClient(USERNAME, ACCESS_KEY)

browsers = [{"platform": "Mac OS X 10.9",
             "browserName": "chrome",
             "version": "31"},
            {"platform": "Windows 8.1",
             "browserName": "firefox",
             "version": "33"}
            ]

browsersWin = [{"platform": "Mac OS X 10.9",
             "browserName": "chrome",
             "version": "31"},
            {"platform": "Windows 8.1",
             "browserName": "firefox",
             "version": "33"},
            {"platform": "Windows 7",
             "browserName": "firefox",
             "version": "33"},
            {"platform": "Windows XP",
             "browserName": "firefox",
             "version": "33"}
]


def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator


@on_platforms(browsersWin)
class SauceSampleTest(unittest.TestCase):
    def setUp(self):
        self.desired_capabilities['name'] = self.id()

        sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (USERNAME, ACCESS_KEY)
        )
        self.driver.implicitly_wait(30)

    def test_sauce(self):
        self.driver.get('https://saucelabs.com/test/guinea-pig')
        assert "I am a page title - Sauce Labs" in self.driver.title
        comments = self.driver.find_element_by_id('comments')
        comments.send_keys('Hello! I am some example comments.'
                           ' I should be in the page after submitting the form')
        self.driver.find_element_by_id('submit').click()

        commented = self.driver.find_element_by_id('your_comments')
        assert ('Your comments: Hello! I am some example comments.'
                ' I should be in the page after submitting the form'
                in commented.text)
        body = self.driver.find_element_by_xpath('//body')
        assert 'I am some other page content' not in body.text
        self.driver.find_elements_by_link_text('i am a link')[0].click()
        body = self.driver.find_element_by_xpath('//body')
        assert 'I am some other page content' in body.text

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        try:
            if sys.exc_info() == (None, None, None):
                sauce.jobs.update_job(self.driver.session_id, passed=True)
            else:
                sauce.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()