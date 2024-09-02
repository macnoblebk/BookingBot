import booking.constants as constants
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)

    def land_first_page(self):
        self.get(constants.BASE_URL)