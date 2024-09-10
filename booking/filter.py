from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Filter:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_property_rating(self, star_value):
        property_rating_box = self.driver.find_element(By.XPATH, '//div[@data-testid="filters-group"]')
        property_rating_child_elements = property_rating_box.find_elements(By.XPATH, '//div[contains(@data-filters-item, "class:class")]')

        for property_rating_element in property_rating_child_elements:
            rating_text = property_rating_element.text.strip()
            print(rating_text)
            if rating_text == star_value:
                property_rating_element.click()

