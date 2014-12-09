__author__ = 'moisessiles'

from pages.home import HomePage
import variables as var


class Utilities(object):

    @staticmethod
    def open_homepage(selenium):
        selenium.get(var.testing_url)
        return HomePage(selenium)