__author__ = 'msiles'

import os
import sys
import new
import unittest
from selenium import webdriver
from sauceclient import SauceClient


class TestBase(unittest.TestCase):

    USERNAME = os.environ.get('SAUCE_USERNAME', "msiles")
    ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', "3d1aec67-5936-4898-ba6b-0bc50e8990ba")
    sauce = SauceClient(USERNAME, ACCESS_KEY)

    def setUp(self):
        self.selenium = webdriver.Chrome()

    def tearDown(self):
        self.selenium.quit()