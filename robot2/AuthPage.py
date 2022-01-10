from BasePage import BasePage
from robot.api import logger
from robot.api.deco import keyword


class AuthPage(BasePage):

    @keyword
    def some_shit(self):
        logger.info(self.driver.current_url)

