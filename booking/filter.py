from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

ONE_STAR = 1
TWO_STARS = 2
THREE_STARS = 3
FOUR_STARS = 4
FIVE_STARS = 5


class Filter:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_property_rating(self, *star_values):
        property_rating_box = self.driver.find_element(By.XPATH, '//div[@data-testid="filters-group"]')

        property_rating_elements = property_rating_box.find_elements(By.XPATH,
                                                                     '//div[contains(@data-filters-item, "class:class=")]')

        for star_value in star_values:
            for property_rating_element in property_rating_elements:
                rating_text = property_rating_element.text
                # print(rating_text)
                rating_parts = rating_text.split()
                # print(rating_parts)
                if rating_parts and rating_parts[0].isdigit() and int(rating_parts[0]) == star_value:
                    checkbox = property_rating_element.find_element(By.XPATH, './/input[@type="checkbox"]')
                    if not checkbox.is_selected():
                        checkbox.click()

