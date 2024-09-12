from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import booking.constants as constants
from booking.filter import Filter
from datetime import datetime, timedelta
import time


def format_date(date_str):
    possible_formats = ["%Y-%m-%d", "%d-%m-%Y", "%m-%d-%Y", "%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d"]

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


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(constants.WAIT_DURATION)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(constants.BASE_URL)

    def close_sign_in_info(self):
        try:
            dismiss_sign_in_info = self.find_element(By.XPATH, "//div[@role='dialog']/div/div/div/div/button")
            dismiss_sign_in_info.click()
            print("Sign-in info")
        except NoSuchElementException:
            print("No Sign-in info")

    def change_currency(self, currency="USD"):
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
        time.sleep(constants.SLEEP_DURATION)  # Ensure search result is successful
        first_result = self.find_element(By.XPATH, "//div[@data-testid='autocomplete-results-options']/ul/li[1]/div")
        first_result.click()

    def select_dates(self, check_in_date=None, check_out_date=None):
        if check_in_date is None:
            check_in_date = datetime.today().strftime("%Y-%m-%d")

        if check_out_date is None:
            check_out_date = (datetime.today() + timedelta(days=3)).strftime("%Y-%m-%d")

        formatted_check_in_date = format_date(check_in_date)
        formatted_check_out_date = format_date(check_out_date)

        check_in_date_element = self.find_element(By.XPATH, f"//span[@data-date='{formatted_check_in_date}']")
        check_in_date_element.click()
        check_out_date_element = self.find_element(By.XPATH, f"//span[@data-date='{formatted_check_out_date}']")
        check_out_date_element.click()

    def select_party_size(self, count=1):
        if count < constants.MIN_ADULT_COUNT:
            raise ValueError(f"Count must be at least: '{constants.MIN_ADULT_COUNT}'")

        selection_element = self.find_element(By.XPATH, '//button[@data-testid="occupancy-config"]')
        selection_element.click()

        increase_adult_element = self.find_element(By.XPATH,
                                                   '//div[@data-testid="occupancy-popup"]/div[1]/div[1]/div[2]/button[2]')
        decrease_adult_count_element = self.find_element(By.XPATH,
                                                         '//div[@data-testid="occupancy-popup"]/div[1]/div[1]/div[2]/button[1]')

        adult_value_element = self.find_element(By.XPATH, '//input[@id="group_adults"]')
        adult_count = int(adult_value_element.get_attribute("value"))

        while adult_count != count:
            if adult_count < count:
                increase_adult_element.click()
            elif adult_count > count and adult_count > constants.MIN_ADULT_COUNT:
                decrease_adult_count_element.click()

            adult_count = int(adult_value_element.get_attribute("value"))

    def click_search(self):
        search_button = self.find_element(By.XPATH, '//div[@data-testid="searchbox-layout-wide"]/div[4]//button')
        search_button.click()

    def apply_filter(self):
        search_filter = Filter(driver=self)
        search_filter.apply_property_rating(4, 5)
        search_filter.sort_price_ascending()
