import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "input28")
    PASSWORD = (By.ID, "input36")
    LOGIN_BUTTON = (By.XPATH, "//input[@class='button button-primary']")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign Up")
    LOGIN = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-block']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_enabled(self.LOGIN)

    def do_login(self, username, password):
        self.do_click(self.LOGIN)
        self.do_sendkeys(self.EMAIL, username)
        self.do_sendkeys(self.PASSWORD, password)
        self.double_click(self.LOGIN_BUTTON)
