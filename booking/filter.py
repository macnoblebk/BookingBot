from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Filter:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # def apply_property_rating(self, star_value):
    #     property_rating_box = self.driver.find_element(By.XPATH, '//div[@data-testid="filters-group"]')
    #
    #     property_rating_elements = property_rating_box.find_elements(By.XPATH,
    #                                                                  '//div[contains(@data-filters-item, "class:class=")]')
    #
    #     # TODO: Fix bug where checkboxes are clicked multiple times
    #     # for star_value in star_values:
    #     for property_rating_element in property_rating_elements:
    #         checkbox = property_rating_element.find_element(By.XPATH, './/input[@type="checkbox"]')
    #         rating_text = property_rating_element.text.strip()
    #         rating_parts = rating_text.split()
    #         print(rating_parts)
    #         if rating_parts and rating_parts[0].isdigit() and int(rating_parts[0]) == star_value:
    #             if not checkbox.is_selected():
    #                 checkbox.click()

    # def apply_property_rating(self, star_value):
    #     property_rating_box = self.driver.find_element(By.XPATH, '//div[@data-testid="filters-group"]')
    #     # property_rating_element = property_rating_box.find_element(By.XPATH,
    #     #                                                                   f'//div[contains(@data-filters-item, "class:class={star_value}")]')
    #     property_rating_element = property_rating_box.find_element(By.XPATH, f'//input[@type="checkbox" and contains(@name, "class={star_value}")]')
    #     if not property_rating_element.is_selected():
    #         property_rating_element.click()

    def apply_property_rating(self, star_value):
        property_rating_box = self.driver.find_element(By.XPATH, '//div[@data-testid="filters-group"]')
        property_rating_elements = property_rating_box.find_elements(By.CSS_SELECTOR,
                                                                     '//input[type="checkbox")]')
        for checkbox in property_rating_elements:
            print(checkbox.text)
            checkbox.click()

    # def sort_price_ascending(self):
    #     sort_by_element = self.driver.find_element(By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"]')
    #     sort_by_element.click()
    #     sort_by_price_element = self.driver.find_element(By.XPATH,
    #                                                      '//div[@data-testid="sorters-dropdown"]/ul/li[3]/button')
    #     sort_by_price_element.click()
