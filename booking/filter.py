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

    def apply_property_rating(self, star_value):
        property_rating_element = self.driver.find_element(By.XPATH,f'//div[@data-filters-item="class:class={star_value}"]')
        property_rating_element.click()
        # self.driver.execute_script("arguments[0].click();", property_rating_element)






