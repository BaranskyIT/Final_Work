import unittest
import sys
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from driver_setup import get_driver
from utility import scroll_to_element
from locators import Locators
from constants import BASE_URL, ERROR_404_SEARCH_TERM

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestChitaiGorodUI(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_homepage_scroll(self):
        self.driver.get(BASE_URL)
        element = scroll_to_element(self.driver, Locators.CHITAI_GOROD_HOME_TEXT)
        self.assertIsNotNone(element, "Элемент 'Книжный интернет-магазин «Читай-город»' не найден на странице")

    def test_best_of_best_scroll(self):
        self.driver.get(BASE_URL)

        best_of_best_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.BEST_OF_BEST_LINK)
        )
        try:
            best_of_best_link.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", best_of_best_link)

        scroll_to_element(self.driver, Locators.BEST_OF_THE_BEST)
    
    def test_search_error_404(self):
        self.driver.get(BASE_URL)

        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.SEARCH_BOX)
        )
        search_box.click()
        search_box.send_keys(ERROR_404_SEARCH_TERM)
        search_box.send_keys(Keys.ENTER)
        
        error_404 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.ERROR_404_BOOK)
        )
        error_404.click()
    
    def test_open_cart(self):
        self.driver.get(BASE_URL)

        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.CART_BUTTON_HEADER)
        )
        try:
            cart_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", cart_button)
    

    def test_add_book_to_cart(self):
        self.driver.get(BASE_URL)

    # Найти и кликнуть на поисковое поле
        search_box = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(Locators.SEARCH_BOX)
    )
        search_box.click()
        search_box.send_keys(ERROR_404_SEARCH_TERM)
        search_box.send_keys(Keys.ENTER)

    # Найти и кликнуть на книгу
        error_404 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickClickable(Locators.ERROR_404_BOOK)
    )
        error_404.click()

    # Найти и кликнуть на кнопку "Добавить в корзину"
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickClickable(Locators.ADD_TO_CART_BUTTON)
    )
        add_to_cart_button.click()

    # Проверка, что книга добавлена в корзину
        self.assertIn("Ошибка 404", self.driver.page_source, "Книга не добавлена в корзину")

if __name__ == "__main__":
    unittest.main()