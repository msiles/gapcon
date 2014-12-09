__author__ = 'msiles'

import os
import sys
import new
import unittest
import variables as var
from selenium import webdriver
from sauceclient import SauceClient


USERNAME = os.environ.get('SAUCE_USERNAME', var.username_sauce)
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', var.key)
sauce = SauceClient(USERNAME, ACCESS_KEY)
browsers = [{"platform": "Mac OS X 10.9",
            "browserName": "chrome",
            "version": "31"},
            {"platform": "Windows 8.1",
            "browserName": "internet explorer",
            "version": "11"}]


# def on_platforms(platforms):
#     def decorator(base_class):
#         module = sys.modules[base_class.__module__].__dict__
#         for i, platform in enumerate(platforms):
#             d = dict(base_class.__dict__)
#             d['desired_capabilities'] = platform
#             name = "%s_%s" % (base_class.__name__, i + 1)
#             module[name] = new.classobj(name, (base_class,), d)
#     return decorator
#
#
#
# @on_platforms(browsers)
class TestBase(unittest.TestCase):

    # def setUp(self):
    #     self.desired_capabilities['name'] = self.id()
    #
    #     sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
    #     self.selenium = webdriver.Remote(
    #         desired_capabilities=self.desired_capabilities,
    #         command_executor=sauce_url % (USERNAME, ACCESS_KEY)
    #     )
    #     self.selenium.implicitly_wait(30)
    #
    # def tearDown(self):
    #     print("Link to your job: https://saucelabs.com/jobs/%s" % self.selenium.session_id)
    #     try:
    #         if sys.exc_info() == (None, None, None):
    #             sauce.jobs.update_job(self.selenium.session_id, passed=True)
    #         else:
    #             sauce.jobs.update_job(self.selenium.session_id, passed=False)
    #     finally:
    #         self.selenium.quit()

    def setUp(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.desired_capabilities['version'] = '31'
        self.desired_capabilities['platform'] = 'Linux'
        self.desired_capabilities['name'] = self.id()
        sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.selenium = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (USERNAME, ACCESS_KEY)
        )

    def tearDown(self):
        try:
            if sys.exc_info() == (None, None, None):
                sauce.jobs.update_job(self.selenium.session_id, passed=True)
            else:
                sauce.jobs.update_job(self.selenium.session_id, passed=False)
        finally:
            self.selenium.quit()