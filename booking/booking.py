from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

import booking.constants as constants
from selenium import webdriver

WAIT_TIME = 10


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(WAIT_TIME)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(constants.BASE_URL)

    def change_currency(self, currency=None):
        # Select currency -- fickle sign-in pop-up
        try:
            no_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
            no_button.click()
        except NoSuchElementException as e:
            print("Sign-in info pop-up absent")

        currency_element = self.find_element(By.CSS_SELECTOR,
                                             'button[aria-label="Prices in U.S. Dollar"]')

        currency_element.click()
