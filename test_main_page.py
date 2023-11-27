import pytest
import allure
from pages import MainPage, LoginPage, ItemPage


@allure.suite("Тесты основной страницы")
@allure.title("Тест на отображение ссылки к странице логина")
@allure.description("Проверяет возможность перехода с главной страницы на страницу логина")
def test_guest_should_see_login_link(browser):

    with allure.step("Переход на главную страницу сайта"):
        page = MainPage(browser=browser, url="http://selenium1py.pythonanywhere.com/")
        page.open()

    with allure.step("Проверка ссылки на страницу логин"):
        page.should_be_login_link()


@allure.suite("Тесты основной страницы")
@allure.title("Тест на возможность перехода к странице логина")
@allure.description("Проверяет возможность перехода с главной страницы на страницу логина")
def test_guest_can_go_to_login_page(browser):

    with allure.step("Переход на главную страницу сайта"):
        page = MainPage(browser=browser, url="http://selenium1py.pythonanywhere.com/")
        page.open()

    with allure.step("Переход на страницу логина"):
        page.go_to_login_page()


@allure.suite("Тесты страницы логина")
@allure.title("Тест содержания страницы логина")
@allure.description("Проверяет содержание страницы логина")
def test_login_page_content(browser):

    with allure.step("Переход на главную страницу сайта"):
        page = LoginPage(browser=browser, url="http://selenium1py.pythonanywhere.com/")
        page.open()

    with allure.step("Переход на страницу логина"):
        page.go_to_login_page()

    with allure.step("Проверка содержимого страницы"):
        page.should_be_login_link()


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
