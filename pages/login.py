__author__ = 'moisessiles'

from base import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    _login_field_locator = (By.ID, "UserName")
    _password_field_locator = (By.ID, "Password")
    _login_button_locator = (By.CSS_SELECTOR, ".classiclogon")
    _remember_locator = (By.ID, "RememberMe")
    _error_label_locator = (By.CSS_SELECTOR, ".validation-summary-errors>span")
    _field_validation_locator = (By.CSS_SELECTOR, ".field-validation-error")
    _logged_username_locator = (By.CSS_SELECTOR, "#logindisplay>b")
    _page_title = u"Log On"

    def login_as_wrong_user(self):
        self.selenium.implicitly_wait(10)  # seconds
        wlogin = self.selenium.find_element(*self._login_field_locator)
        wpassword = self.selenium.find_element(*self._password_field_locator)
        wbutton = self.selenium.find_element(*self._login_button_locator)

        wlogin.send_keys("test@test.com")
        wpassword.send_keys("wrongPassword")

        wbutton.click()

    def login_successful(self, username, password):
        self.selenium.implicitly_wait(10)  # seconds
        wlogin = self.selenium.find_element(*self._login_field_locator)
        wpassword = self.selenium.find_element(*self._password_field_locator)
        wbutton = self.selenium.find_element(*self._login_button_locator)

        wlogin.send_keys(username)
        wpassword.send_keys(password)

        wbutton.click()

    def error_message(self):
        self.selenium.implicitly_wait(10)  # seconds
        logged_element = self.selenium.find_element(*self._field_validation_locator)

        return logged_element.text

    def welcome_message(self):
        self.selenium.implicitly_wait(10)  # seconds
        logged_element = self.selenium.find_element(*self._logged_username_locator)

        return logged_element.text