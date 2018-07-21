from appium import webdriver
from pages.base_page import BasePage
from locators.landing_locators import locators
import time

API_WAIT_TIME = 3  # seconds


class LandingPage(BasePage):

    def __init__(self, driver: webdriver.Remote):
        super().__init__(driver=driver)
        self.driver = driver

    def click_drawer(self):
        """
        Clicks on the hamburger menu
        """
        self.wait_then_click(*locators['hamburger button'])

    def expand_collapse_projects(self):
        """
        Clicks on the arrow to expand or collapse project in the drawer
        """
        self.wait_then_click(*locators['collapse projects button'])

    def has_project(self, project_name: str) -> bool:
        """
        Checks if the given project is visible in the drawer
        :param project_name: the name of the project
        :return: True if visible, false otherwise
        """
        by, locator = locators['project name view']
        locator = locator.format(project_name)
        return self.explicitly_wait_for_presence(by, locator)

    def refresh(self):
        """
        Swipes down from the toolbar to refresh the page
        """
        self.explicitly_wait_for_presence(*locators['toolbar'])
        toolbar_element = self.driver.find_element(*locators['toolbar'])
        self.swipe_element_down(toolbar_element)
        time.sleep(API_WAIT_TIME)

    def select_project(self, project_name: str):
        by, locator = locators['project name view']
        locator = locator.format(project_name)
        self.wait_then_click(by, locator)

    def click_add_task_button(self):
        self.wait_then_click(*locators['add task button'])

    def enter_task_message(self, task_message: str):
        task_message_element = self.driver.find_element(*locators['task message field'])
        task_message_element.send_keys(task_message)

    def save_task(self):
        self.wait_then_click(*locators['save task'])
        self.wait_then_click(*locators['save task'])

    def click_task(self, task_message):
        by, locator = locators['task message view']
        locator = locator.format(task_message)
        self.wait_then_click(by, locator)

    def click_complete(self):
        self.wait_then_click(*locators['complete task button'])

    def click_inbox(self):
        self.wait_then_click(*locators['inbox button'])

    def has_task_with_message(self, task_message):
        """
        Checks if the landing page has a visible task with the specified message
        :param task_message: The message to look for
        :return: True if present, false otherwise
        """
        by, locator = locators['task message view']
        locator = locator.format(task_message)
        return self.explicitly_wait_for_presence(by, locator)
