__author__ = 'moisessiles'


from commons.testBase import TestBase
from pages.home import HomePage


class HomeTests(TestBase):

    def test_search_verification(self):
        home_pg = HomePage(self.selenium)
        home_pg.go_to_home_page()
        home_pg.execute_search("San Jose")
        assert home_pg._page_title == "Nerd Dinner", "Title do not match"

    def test_upcomming_dinners_access(self):
        home_pg = HomePage(self.selenium)
        home_pg.go_to_home_page()
        upcomming_pg = home_pg.click_view_upcoming()

        assert upcomming_pg._page_title == "Upcomming Nerd Dinners", "Title do not match"
