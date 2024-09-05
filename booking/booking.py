from datetime import datetime

from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import booking.constants as constants
import time
from selenium import webdriver

WAIT_TIME = 3


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

    def close_sign_in_info(self):
        try:
            # no_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
            dismiss_sign_in_info = self.find_element(By.XPATH, "//div[@role='dialog']/div/div/div/div/button")
            dismiss_sign_in_info.click()
            print("Sign-in info")
        except NoSuchElementException:
            print("No Sign-in info")
        except StaleElementReferenceException:
            print("Element went stale")

    def change_currency(self, currency="USD"):
        # currency_element = self.find_element(By.CSS_SELECTOR,
        #                                      'button[aria-label="Prices in U.S. Dollar"]')

        defualt_to_USD = self.find_element(By.XPATH,
                                           "//nav[@class='Header_bar']/div/span[1]/button")
        defualt_to_USD.click()

        selected_currency = self.find_element(By.XPATH,
                                              f"//div[@data-testid='All currencies']//ul/li//span/div[text()='{currency}']//ancestor::button")

        selected_currency.click()

    def set_destination(self, destination):
        destination_field = self.find_element(By.XPATH, "//div[@data-testid='destination-container']/div/div/div/input")
        destination_field.clear()
        destination_field.send_keys(destination)
        time.sleep(1)  # Ensure search result is successful
        first_result = self.find_element(By.XPATH, "//div[@data-testid='autocomplete-results-options']/ul/li[1]/div")
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_date_element = self.find_element(By.XPATH, f"//span[@data-date='{check_in_date}']")
        # check_in_date_element = self.find_element(By.CSS_SELECTOR, f"span[data-date='{check_in_date}']")
        check_in_date_element.click()
        check_out_date_element = self.find_element(By.XPATH, f"//span[@data-date='{check_out_date}']")
        check_out_date_element.click()

    def format_date(self, date_str):
        # List of common date formats to attempt parsing
        possible_formats = [
            "%Y-%m-%d",
            "%d-%m-%Y",
            "%m-%d-%Y",
            "%m/%d/%Y",
            "%d/%m/%Y",
            "%Y/%m/%d"
        ]

        for date_format in possible_formats:
            try:
                # Try to parse the input date with the current format
                date = datetime.strptime(date_str, date_format)
                # Return the formatted date string as 'YYYY-MM-DD'
                return date.strftime("%Y-%m-%d")
            except ValueError:
                # If the format doesn't match, continue trying other formats
                continue

        raise ValueError(f"Incorrect date format: '{date_str}'. Supported formats are: YYYY-MM-DD, DD-MM-YYYY, "
                         f"MM/DD/YYYY, etc.")
