__author__ = 'moisessiles'


from commons.testBase import TestBase
from pages.utils import Utilities


class HomeTests(TestBase):

    def test_search_verification(self):
        home_pg = Utilities.open_home_page(self.selenium)
        home_pg.execute_search("San Jose")
        assert home_pg._page_title == "Nerd Dinner", "Title do not match"

    def test_upcoming_dinners_access(self):
        home_pg = Utilities.open_home_page(self.selenium)
        upcoming_pg = home_pg.click_view_upcoming()

        assert upcoming_pg._page_title == "Upcoming Nerd Dinners", "Title do not match"
