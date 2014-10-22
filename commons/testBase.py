__author__ = 'msiles'


import unittest
from selenium import webdriver


class TestBase(unittest.TestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()

    def tearDown(self):
        self.selenium.quit()