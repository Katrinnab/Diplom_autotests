# Diplom_autotests

# Автотесты для Кинопоиска

Этот проект содержит автотесты для проверки функциональности API и веб-интерфейса Кинопоиска. Тесты разделены на две категории: API-тесты и UI-тесты.

## Стек
- pytest
- selenium
- requests
- allure

## Структура проекта

- **`pages/`**: Содержит классы для работы с API и веб-интерфейсом.
  - `authpage.py`: Класс `AuthPage` для работы с API Кинопоиска.
  - `uipage.py`: Класс `KinoPage` для работы с веб-интерфейсом Кинопоиска.
- **`tests/`**: Содержит тесты.
  - `test_api.py`: API-тесты.
  - `test_ui.py`: UI-тесты.
- **`conftest.py`**: Содержит фикстуры для тестов.
- **`README.md`**: Документация проекта.
- **`requirements.txt`**: Файл с содержащимися зависимостями

## Установка и запуск

### Требования
- Python 3.9 или выше.
- Установленные зависимости из `requirements.txt`.
- Браузер Chrome и ChromeDriver для UI-тестов.

### Установка зависимостей
1. Установите зависимости:
   pip install -r requirements.txt

### Запуск тестов pytest
1. Запуск test_api.py - python -m pytest test_api.py
2. Запуск test_ui.py - python -m pytest test_ui.py
3. Запуск всех тестов - python -m pytest

### Запуск тестов allure и формирование результатов прогона
1. Запуск test_api.py - python -m pytest test_api.py --alluredir allure-result
2. Запуск test_ui.py - python -m pytest test_ui.py --alluredir allure-result
3. Запуск всех тестов - python -m pytest --alluredir allure-result

### Формирование отчета
После выполнения тестов можно получить отчет с помощью команды allure serve allure-result

### Создание файла с отчетом
Чтобы сгенерировать файл с тестом выполните следующую команду в терминале: allure generate allure-results
После того как отчет будет сформирован, он будет автоматически открыт в вашем браузере.