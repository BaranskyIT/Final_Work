import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Функция для получения настроенного драйвера
def get_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless")  # Запуск в фоновом режиме
    service = Service(r"C:\Users\H1zhina\Desktop\python\Final_Work\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def test_chitai_gorod_homepage():
    driver = get_driver()  # Используем функцию get_driver
    driver.get("https://www.chitai-gorod.ru/")

    # Пауза для загрузки страницы
    time.sleep(3)

    # Поиск элемента по локатору
    element = driver.find_element(By.XPATH, "//div[text()='Книжный интернет-магазин «Читай-город»']")
    
    # Проверка, что элемент найден
    assert element is not None

    # Пауза перед закрытием браузера
    time.sleep(2)

    # Закрытие браузера
    driver.quit()

def test_chitai_gorod_best_of_best():
    driver = get_driver()  # Используем функцию get_driver
    driver.get("https://www.chitai-gorod.ru/")
    time.sleep(3)

    # Найти и нажать на "Лучшие из лучших"
    best_of_best = driver.find_element(By.XPATH, "//a[@class='app-title--link' and text()='Лучшие из лучших']")
    best_of_best.click()
    time.sleep(3)

    # Найти и нажать на логотип
    logo = driver.find_element(By.XPATH, "//svg[@class='header-logo__icon']")
    logo.click()
    time.sleep(3)

    driver.quit()

def test_search_404_error():
    driver = get_driver()  # Используем функцию get_driver
    driver.get("https://www.chitai-gorod.ru/")
    time.sleep(3)

    # Найти строку поиска и ввести "ошибка 404"
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Хочу найти']")
    search_box.click()
    search_box.send_keys("ошибка 404")
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)

    # Найти и нажать на книгу "Ошибка 404"
    error_404 = driver.find_element(By.XPATH, "//div[@class='product-title__head' and text()='Ошибка 404']")
    error_404.click()
    time.sleep(3)

    # Нажать на кнопку "Добавить в корзину"
    add_to_cart = driver.find_element(By.XPATH, "//button[@type='button' and contains(@class, 'product-offer-button')]")
    add_to_cart.click()
    time.sleep(3)

    # Нажать на кнопку "Оформить"
    checkout_button = driver.find_element(By.XPATH, "//button[contains(@class, 'chg-app-button--green') and descendant::div[text()='Оформить']]")
    checkout_button.click()
    time.sleep(3)

    driver.quit()

if __name__ == "__main__":
    # Запуск всех тестов
    test_chitai_gorod_homepage()
    test_chitai_gorod_best_of_best()
    test_search_404_error()
