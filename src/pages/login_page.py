from appium import webdriver

from locators.login_locators import locators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: webdriver.Remote):
        super().__init__(driver=driver)
        self.driver = driver

    def click_continue_with_email(self):
        self.wait_then_click(*locators['continue with email button'])

    def enter_email(self, email: str):
        self.explicitly_wait_for_presence(*locators['email field'])
        email_element = self.driver.find_element(*locators['email field'])
        email_element.send_keys(email)

    def click_continue(self):
        self.wait_then_click(*locators['continue button'])

    def enter_password(self, password: str):
        self.explicitly_wait_for_presence(*locators['password field'])
        password_element = self.driver.find_element(*locators['password field'])
        password_element.send_keys(password)

    def click_login_button(self):
        self.wait_then_click(*locators['login button'])

    def attempt_login(self, email: str, password: str) -> bool:
        """
        Attempts to login the user with the given credentials
        :param email: The email address to be used
        :param password: The password to be associated with the email
        :return: Was it a successful login or not
        """
        self.click_continue_with_email()
        self.enter_email(email)
        self.click_continue()
        self.enter_password(password)
        self.click_login_button()
        return self.is_logged_in()

    def is_logged_in(self) -> bool:
        return self.explicitly_wait_for_presence(*locators['toolbar'])
