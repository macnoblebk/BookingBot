from selenium.common import NoSuchElementException, StaleElementReferenceException
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
        try:
            no_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
            no_button.click()
            print("Sign-in info")
        except NoSuchElementException:
            print("Sign-in info pop-up absent")
        except StaleElementReferenceException:
            print("Element went stale")

        currency_element = self.find_element(By.CSS_SELECTOR,
                                             'button[aria-label="Prices in U.S. Dollar"]')
        currency_element.click()

        selected_currency = self.find_element(By.XPATH,
                                              f"//div[@data-testid='All currencies']//ul/li//span/div[text()='{currency}']//ancestor::button")

        selected_currency.click()