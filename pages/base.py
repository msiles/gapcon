from selenium.webdriver.common.by import By

from pages.page import Page


class BasePage(Page):

    _page_title_locator = (By.CSS_SELECTOR, "h1.page-title")
    _login_link_locator = (By.CSS_SELECTOR, "#logindisplay>a")
    _about_tab_locator = (By.CSS_SELECTOR, ".last>a")


    #@property
    #def login_region(self):
    #    from regions.login import LoginRegion
    #    return LoginRegion(self.testsetup)

    #@property
    #def is_logged_in(self):
    #    return self.login_region.is_logout_visible

    @property
    def page_title(self):
        return self.selenium.find_element(*self._page_title_locator).text

    def go_to_login_page(self):
        welement = self.selenium.find_element(*self._login_link_locator)
        welement.click()