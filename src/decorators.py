import os

from pages.landing_page import LandingPage
from pages.login_page import LoginPage


def login_if_necessary(test_function):
    def wrapper(landing_page: LandingPage):
        login_page = LoginPage(landing_page.driver)
        print("Checking if user needs to be logged in")
        if not login_page.is_logged_in():
            email = os.getenv('email')
            password = os.getenv('password')
            print("User needs to be logged in")
            login_page.attempt_login(email, password)
            if not login_page.is_logged_in():
                raise Exception(
                    "Could not log in with credentials email: "+email+" and password: "+password+"")
            print("Successfully logged in")
        test_function(landing_page)
    return wrapper
