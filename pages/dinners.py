__author__ = 'moisessiles'

from base import BasePage


class UpcommingDinnersPage(BasePage):

    _page_title = u"Upcoming Nerd Dinners"

    #TODO
    def click_home_dinner_link(self):
        wlink = self.selenium.find_elements(*self._links_locator)[0]
        wlink.click()