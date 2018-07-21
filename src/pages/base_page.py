from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

default_wait_time = 6  # seconds
default_swipe_duration = 1500  # ms


class BasePage:

    def __init__(self, **kwargs):
        self.driver = kwargs['driver']

    def explicitly_wait_for_presence(self, by=By.ID, locator=None, wait_time=default_wait_time):
        print("Explicitly waiting for element: {} by {}".format(locator, by))
        try:
            WebDriverWait(self.driver, wait_time) \
                .until(expected_conditions.presence_of_element_located((by, locator)))
            return True
        except TimeoutException as e:
            print("Element not found after waiting {} seconds".format(wait_time))
            print(e.msg)
            return False

    def wait_then_click(self, by, locator, wait_time=default_wait_time):
        is_present = self.explicitly_wait_for_presence(by, locator, wait_time)

        if not is_present:
            raise Exception("Element not present after wait")
        try:
            element = self.driver.find_element(by, locator)
            element.click()
            return True
        except NoSuchElementException as e:
            print("Error clicking element")
            print(e.msg)
            return False

    def _perform_swipe_down(self, start_x, start_y, duration=default_swipe_duration):  # Duration in ms
        self.driver.swipe(start_x, start_y + 150, start_x, start_y + 600, duration)

    def swipe_element_down(self, element):
        location = element.location
        self._perform_swipe_down(location['x'], location['y'])
