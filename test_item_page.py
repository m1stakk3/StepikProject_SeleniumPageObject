import pytest
import allure
from pages import ItemPage, BasketPage


@allure.suite("Тесты страницы товара и корзины")
@allure.title("Тест добавление товара в корзину")
@allure.description("Уга буга товары")
@pytest.mark.parametrize(
    'link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ]
)
def test_guest_can_add_product_to_basket(browser, link):

    with allure.step("Открытие страницы с товаром"):
        page = ItemPage(browser=browser, url=link)
        page.open()

    with allure.step("Добавление товара в корзину"):
        page.save_item_name()
        page.save_item_price()
        page.add_to_basket()

    with allure.step("Переход в корзину и сравнение данных страницы товара и в корзине"):
        page.solve_quiz_and_get_code()
        page.check_item_added_to_basket()
        page.check_item_price_in_basket()


@pytest.mark.xfail("Incorrect test")
@allure.suite("Тесты страницы товара и корзины")
@allure.title("Тест на невозможность гостем увидеть сообщение о добавлении товара в корзину")
@allure.description("Сообщение не отобразится из-за дилея без implicity wait")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    with allure.step("Подготовка - выключение ожидания"):
        page = ItemPage(browser=browser, url=link)
        page.browser.implicitly_wait(0)

    with allure.step("Добавление товара в корзину"):
        page.open()
        page.add_to_basket()

    with allure.step("Проверка, что сообщение не отобразилось"):
        page.should_not_be_success_message()


@allure.suite("Тесты страницы товара и корзины")
@allure.title("Тест на невозможность гостем увидеть сообщение")
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    with allure.step("Подготовка - выключение ожидания"):
        page = ItemPage(browser=browser, url=link)
        page.browser.implicitly_wait(0)

    with allure.step("Проверка, что сообщение не отобразилось"):
        page.open()
        page.should_not_be_success_message()


@pytest.mark.xfail("Incorrect test")
@allure.suite("Тесты страницы товара и корзины")
@allure.title("Тест на невозможность гостем увидеть сообщение")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    with allure.step("Подготовка - выключение ожидания"):
        page = ItemPage(browser=browser, url=link)
        page.browser.implicitly_wait(0)

    with allure.step("Добавление товара в корзину"):
        page.open()
        page.add_to_basket()

    with allure.step("Проверка, что сообщение не отобразилось"):
        page.should_not_be_success_message_disappeared()


@allure.suite("Тесты страницы товара и корзины")
@allure.title("Тест на невозможность гостем увидеть товар в корзине (не добавлен)")
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ItemPage(browser=browser, url=link)

    with allure.step("Гость открывает страницу товара"):
        page.open()

    with allure.step("Переходит в корзину по кнопке в шапке"):
        page.go_to_basket()

    with allure.step("Ожидаем, что в корзине нет товаров"):
        page = BasketPage(browser=browser, url=page.browser.current_url)
        page.is_basket_empty()

    with allure.step("Ожидаем, что есть текст о том что корзина пуста"):
        page = BasketPage(browser=browser, url=page.browser.current_url)
        page.is_basket_empty_message()
