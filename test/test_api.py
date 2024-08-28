# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import time


# service = Service(r"C:\Users\H1zhina\Desktop\python\Final_Work\chromedriver.exe")
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

# try:
#     # Открытие сайта Читай-город
#     driver.get("https://www.chitai-gorod.ru/")

#     # Ожидание загрузки страницы
#     time.sleep(5)

#     # Проверка наличия текста "Читай-город" в заголовке страницы
#     assert "Читай-город" in driver.title, "Заголовок не содержит 'Читай-город'."

#     print("Сайт успешно загружен и заголовок страницы корректен.")

# finally:
#     # Закрытие браузера
#     driver.quit()
import unittest
import requests
from config import BASE_URL

class TestAPI(unittest.TestCase):
    def test_api_status(self):
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200, "API не возвращает статус 200")

if __name__ == '__main__':
    unittest.main()
