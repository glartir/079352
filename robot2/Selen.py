from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword


class Selen(SeleniumLibrary):

    @keyword
    def get_driver(self):
        return self.driver
