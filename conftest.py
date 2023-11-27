import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # создание опции для выбора языка
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="select language to launch Chrome"
    )


@pytest.fixture
def language(pytestconfig):
    # получение опции языка из CMD
    return pytestconfig.getoption("language")


@pytest.fixture(scope="function")
def browser(language):

    # получение настроек и установка языка по-умолчанию
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    # запуск браузера с языковыми настройками и работа до прекращения использования
    browser = webdriver.Chrome(options=options)
    yield browser

    browser.quit()
