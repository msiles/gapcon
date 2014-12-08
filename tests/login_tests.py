__author__ = 'moisessiles'


from commons.testBase import TestBase
from commons.utilities import Utilities
from pages.login import LoginPage


class LoginTests(TestBase):

    def test_wrong_login_verification(self):
        home_pg = Utilities.open_homepage(self.selenium)
        login_pg = LoginPage(self.selenium)
        home_pg.go_to_login_page()
        login_pg.login_as_wrong_user()

        assert login_pg.error_message() == "Login was unsuccessful. Please correct the errors and try again.", "Error message do not match"

    def test_successful_login_verification(self):
        home_pg = Utilities.open_homepage(self.selenium)
        login_pg = LoginPage(self.selenium)
        home_pg.go_to_login_page()
        login_pg.login_successful("moises.siles@gmail.com", "123456")

        assert login_pg.successful_message() == "moises.siles@gmail.com", "User do not match"
