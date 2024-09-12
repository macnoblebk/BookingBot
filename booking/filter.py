from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Filter:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_property_rating(self, *star_values):
        property_rating_box = self.driver.find_element(By.XPATH, '//div[@data-testid="filters-group"]')

        property_rating_elements = property_rating_box.find_elements(By.XPATH,
                                                                     '//div[contains(@data-filters-item, "class:class=")]')

        # TODO: Fix bug where checkboxes are toggled between runs
        for star_value in star_values:
            for property_rating_element in property_rating_elements:
                rating_text = property_rating_element.text
                # print(rating_text)
                rating_parts = rating_text.split()
                # print(rating_parts)
                if rating_parts and rating_parts[0].isdigit() and int(rating_parts[0]) == star_value:
                    checkbox = property_rating_element.find_element(By.XPATH, '. //input[@type="checkbox"]')
                    if not checkbox.is_selected():
                        checkbox.click()

    def sort_price_ascending(self):
        sort_by_element = self.driver.find_element(By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"]')
        sort_by_element.click()
        sort_by_price_element = self.driver.find_element(By.XPATH,
                                                         '//div[@data-testid="sorters-dropdown"]/ul/li[3]/button')
        sort_by_price_element.click()
