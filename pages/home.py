__author__ = 'moisessiles'

import time
from dinners import UpcommingDinnersPage
from base import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    _search_locator = (By.ID, "Location")
    _search_button_locator = (By.ID, "search")
    _view_upcoming_locator = (By.CSS_SELECTOR, ".search-text>strong>a")
    _page_title = u"Nerd Dinner"

    def go_to_home_page(self):
        self.selenium.get("http://nerddinner.com")
        self.is_the_current_page

    def execute_search(self, search_value):
        welement = self.selenium.find_element(*self._search_locator)

        #TODO, need to remove this Sleep
        time.sleep(5)

        welement.clear()
        welement.send_keys(search_value)

    def click_view_upcoming(self):
        welement = self.selenium.find_element(*self._view_upcoming_locator)
        welement.click()

        return UpcommingDinnersPage

