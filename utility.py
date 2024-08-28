import time

def scroll_to_element(driver, locator):
    """Прокручивает страницу вниз до элемента, если он не найден сразу."""
    element = None
    while not element:
        try:
            element = driver.find_element(*locator)
        except:
            driver.execute_script("window.scrollBy(0, 500);")  # Скроллим на 500 пикселей
            time.sleep(1)  # Краткая пауза для загрузки контента
    return element
