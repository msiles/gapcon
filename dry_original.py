__author__ = 'moisessiles'


import unittest
from selenium import webdriver


class SeleniumTest(unittest.TestCase):

    def test_gapcon_in_title(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)
        self.browser.get('http://google.com')
        q = self.browser.find_element_by_name("q")
        q.send_keys("gapCon 2014")
        q.submit()
        self.browser.find_element_by_id("search")
        assert 'gapCon 2014' in self.browser.title

        self.browser.quit()

    def test_google_searchfield(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)
        self.browser.get('http://google.com')
        self.browser.find_element_by_name("q")
        assert self.browser.find_element_by_name("q").is_displayed()

        self.browser.quit()

    if __name__ == '__main__':
        unittest.main()
