__author__ = 'moisessiles'

from pages.home import HomePage


class Utilities():

    @staticmethod
    def open_homepage(selenium):
        selenium.get("http://nerddinner.com")

        return HomePage(selenium)