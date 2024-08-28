from selenium.webdriver.common.by import By

class Locators:
    CHITAI_GOROD_HOME_TEXT = (By.XPATH, "//div[text()='Книжный интернет-магазин «Читай-город»']")
    BEST_OF_BEST_LINK = (By.XPATH, "//a[@class='app-title--link' and contains(text(), 'Лучшие из лучших')]")
    BEST_OF_THE_BEST = (By.XPATH, "//h1[@class='app-catalog-page__title' and text()='Лучшие из лучших']")
    SEARCH_BOX = (By.XPATH, "//input[@class='header-search__input' and @name='phrase']")
    ERROR_404_BOOK = (By.XPATH, "//div[@class='product-title__head' and contains(text(), 'Ошибка 404')]")
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@class='chg-app-button__content' and contains(text(), 'Купить')]")
    CHECKOUT_BUTTON = (By.XPATH, "//div[@class='chg-app-button__content' and contains(text(), 'Оформить')]")
    CART_BUTTON = (By.XPATH, "//span[@class='badge-notice header-cart__badge' and contains(text(), '1')]")
