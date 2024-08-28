# Final_Work
# BookStore Tests

## Описание проекта

Этот проект содержит UI и API тесты для интернет-магазина "Читай-город".

## Установка

Установите зависимости:
```bash
pip install -r requirements.txt

Запуск тестов
UI тесты:
bash
Копировать код
pytest -m ui tests/test_ui.py
API тесты:
bash
Копировать код
pytest -m api tests/test_api.py
Все тесты:
bash
Копировать код
pytest tests/
Структура проекта
tests/test_ui.py - UI тесты
tests/test_api.py - API тесты
config/settings.py - конфигурация