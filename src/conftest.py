import os
import subprocess
import time

import pytest
from appium import webdriver
from dotenv import load_dotenv, find_dotenv

from exceptions import EnvironmentException
from pages.landing_page import LandingPage

from api.project import Project

load_dotenv(find_dotenv())  # load environment variables

port = 4723


def start_appium_server():
    global appium
    appium = subprocess.Popen(['appium', '--port', str(port)])
    assert appium.poll() is None  # Server is running


def get_driver() -> webdriver.Remote:
    """
    Initiates the driver with the desired capabilites
    :return: The Webdriver object
    """
    root_dir = os.path.dirname(os.path.abspath(__file__))
    desired_capabilities = {
        'platformName': 'Android',
        'app': root_dir+'/apps/todoist.apk',
        'deviceName': 'Android Emulator',
        'appPackage': 'com.todoist',
        'appActivity': 'com.todoist.activity.HomeActivity'
    }
    return webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port), desired_capabilities)


@pytest.fixture
def landing_page():
    driver = get_driver()
    yield LandingPage(driver)
    driver.quit()


def pytest_sessionstart(session):
    project = Project()

    if project.token is None:
        raise EnvironmentException('No token found. Do you have a .env file in the project root with key "TOKEN"?')

    email = os.getenv('email')
    password = os.getenv('password')

    if email is None:
        raise EnvironmentException('No email found. Do you have a .env file in the project root with key "email"?')

    if password is None:
        raise EnvironmentException(
            'No password found. Do you have a .env file in the project root with key "password"?')
    print("Test Session Beginning: Starting appium server")
    start_appium_server()
    time.sleep(3)


def pytest_sessionfinish(session, exitstatus):
    print("Test Session Complete: Tearing down appium server")
    global appium
    appium.terminate()
