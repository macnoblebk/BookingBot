from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as constants
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

    def change_currency(self, currency=None):
        try:
            # no_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
            dismiss_sign_in_info = self.find_element(By.XPATH, "//div[@role='dialog']/div/div/div/div/button")
            dismiss_sign_in_info.click()
            print("Sign-in info")
        except NoSuchElementException:
            print("No Sign-in info")
        except StaleElementReferenceException:
            print("Element went stale")

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
        # wait = WebDriverWait(self, 10)
        # first_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='autocomplete-results-options']/ul/li[1]/div")))
        first_result = self.find_element(By.XPATH, "//div[@data-testid='autocomplete-results-options']/ul/li[1]/div")
        first_result.click()
