__author__ = 'moisessiles'

from base import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    _login_field_locator = (By.ID, "UserName")
    _password_field_locator = (By.ID, "Password")
    _login_button_locator = (By.CSS_SELECTOR, ".classiclogon")
    _remember_locator = (By.ID, "RememberMe")
    _page_title = u"Log On"

    def login_as_wrong_user(self):
        wlogin = self.selenium.find_element(*self._login_field_locator)
        wpassword = self.selenium.find_element(*self._password_field_locator)
        wbutton = self.selenium.find_element(*self._login_button_locator)

        wlogin.send_keys("xxxxxxxxx")
        wpassword.send_keys("wrongPassword")

        wbutton.click()


    def login_successful(self, username, password):
        wlogin = self.selenium.find_element(*self._login_field_locator)
        wpassword = self.selenium.find_element(*self._password_field_locator)
        wbutton = self.selenium.find_element(*self._login_button_locator)

        wlogin.send_keys(username)
        wpassword.send_keys(password)

        wbutton.click()