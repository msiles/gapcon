__author__ = 'moisessiles'

from base import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    _login_field_locator = (By.ID, "UserName")
    _password_field_locator = (By.ID, "Password")
    _login_button_locator = (By.CSS_SELECTOR, ".classiclogon")
    _remember_locator = (By.ID, "RememberMe")
    _page_title = u"Log On"
    _summary_error = (By.CSS_SELECTOR, ".validation-summary-errors>span")
    _welcome_user = (By.CSS_SELECTOR, "#logindisplay>b")
    _password_required = (By.CSS_SELECTOR, ".field-validation-error>span")

    def login_as_wrong_user(self):
        self.selenium.implicitly_wait(10) # seconds
        wlogin = self.selenium.find_element(*self._login_field_locator)
        wpassword = self.selenium.find_element(*self._password_field_locator)
        wbutton = self.selenium.find_element(*self._login_button_locator)

        wlogin.send_keys("testuser@test.com")
        wpassword.send_keys("wrongPassword")

        wbutton.click()

    def login_successful(self, username, password):
        self.selenium.implicitly_wait(10) # seconds
        wlogin = self.selenium.find_element(*self._login_field_locator)
        wpassword = self.selenium.find_element(*self._password_field_locator)
        wbutton = self.selenium.find_element(*self._login_button_locator)

        wlogin.send_keys(username)
        wpassword.send_keys(password)

        wbutton.click()

    def successful_message(self):
        self.selenium.implicitly_wait(10) # seconds
        welcome_message = self.selenium.find_element(*self._welcome_user)
        return welcome_message.text

    def error_message(self):
        self.selenium.implicitly_wait(10) # seconds
        error_message = self.selenium.find_element(*self._summary_error)
        return error_message.text

    def password_required_message(self):
        self.selenium.implicitly_wait(10) # seconds
        error_message = self.selenium.find_element(*self._password_required)
        return error_message.text