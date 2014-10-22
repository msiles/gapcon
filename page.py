__author__ = 'moisessiles'

#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.support.ui import WebDriverWait
from unittestzero import Assert


class Page(object):

    def __init__(self, selenium):
        self.selenium = selenium
        self.timeout = 20

    @property
    def is_the_current_page(self):
        if self._page_title:
            WebDriverWait(self.selenium, self.timeout).until(lambda s: s.title)

        Assert.equal(self.selenium.title, self._page_title)
        return True

    def is_element_visible(self, locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except:
            return False
