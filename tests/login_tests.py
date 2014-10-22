__author__ = 'moisessiles'


from commons.testBase import TestBase
from pages.home import HomePage
from pages.login import LoginPage

class LoginTests(TestBase):

    def test_login_verification(self):
        home_pg = HomePage(self.selenium)
        home_pg.go_to_home_page()
        login_pg = LoginPage(self.selenium)
        home_pg.go_to_login_page()
        login_pg.login_as_wrong_user()

