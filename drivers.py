from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless")  # Запуск в фоновом режиме
    service = Service(r"C:\Users\H1zhina\Desktop\python\Final_Work\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    return driver
