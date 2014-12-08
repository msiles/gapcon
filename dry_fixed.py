__author__ = 'moisessiles'


import unittest
from selenium import webdriver


class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.browser.get('http://google.com')

    def tearDown(self):
        self.browser.quit()

    def search(self, search_string):
        q = self.findsearchfield()
        q.send_keys(search_string)
        q.submit()
        results = self.browser.find_element_by_id("search")
        return results.find_element_by_tag_name('a')

    def findsearchfield(self):
        return self.browser.find_element_by_name("q")

    def test_gapcon_in_title(self):
        self.search('gapCon 2014')
        assert 'gapCon 2014' in self.browser.title

    def test_google_searchfield(self):
        q = self.findsearchfield()
        assert q.is_displayed()

    if __name__ == '__main__':
        unittest.main() 
