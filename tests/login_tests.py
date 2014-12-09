__author__ = 'moisessiles'


from commons.testBase import TestBase
from commons.utilities import Utilities
from pages.login import LoginPage
import variables as var


class LoginTests(TestBase):

    def test_wrong_login_verification(self):
        home_pg = Utilities.open_homepage(self.selenium)
        login_pg = LoginPage(self.selenium)
        home_pg.go_to_login_page()
        login_pg.login_as_wrong_user()

        assert login_pg.error_message() ==\
            "Login was unsuccessful. Please correct the errors and try again.",\
            "Message do not match"

    def test_successful_login_verification(self):
        home_pg = Utilities.open_homepage(self.selenium)
        login_pg = LoginPage(self.selenium)
        home_pg.go_to_login_page()
        login_pg.login_successful(var.test_username, var.test_password)

        assert login_pg.successful_message() == var.test_username, "User do not match"

    def test_empty_password_verification(self):
        home_pg = Utilities.open_homepage(self.selenium)
        login_pg = LoginPage(self.selenium)
        home_pg.go_to_login_page()
        login_pg.login_successful(var.test_username, "")

        assert login_pg.password_required_message() == "The Password: field is required.", "Message do not match"