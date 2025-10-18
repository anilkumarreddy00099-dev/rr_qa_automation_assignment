from selenium.webdriver.common.by import By
from utilities.api_utils import fetch_movies
from utilities.logger import get_logger

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()

    CATEGORY_BTN = "//button[text()='{}']"
    MOVIE_TITLES = "//div[@class='card-title']"

    def select_category(self, category):
        self.logger.info(f"Selecting category: {category}")
        btn = self.driver.find_element(By.XPATH, self.CATEGORY_BTN.format(category))
        btn.click()

    def get_displayed_titles(self):
        elements = self.driver.find_elements(By.XPATH, self.MOVIE_TITLES)
        titles = [el.text for el in elements]
        self.logger.info(f"Movies displayed: {titles}")
        return titles

    def get_movies_from_api(self, category):
        return fetch_movies(category.lower())
