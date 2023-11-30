# StepikProject_SeleniumPageObject

Python 3.10

Проект для курса https://stepik.org/course/575/.

### Процесс запуска

* Вызвать CMD в папке с тестами
* python -m venv venv
* if linux: source venv/bin/activate -> if windows: venv\Scripts\activate
* pip install -r requirements.txt
* pytest -v --tb=line --language=en -m need_review

## Дополнительная информация
1. Проект был расширен фреймворком Allure для получения красивых отчетов.
2. Все селекторы из курса заменены на XPath (на основе данных тестировщиков VK, после перевода стабильность повысилась до 90%).
3. Добавлены доп. проверки (потому что проверки из курса не предусматривают в норм виде тайминги).
4. Добавлено логгирование.   
