import allure
from pages import MainPage, LoginPage, BasketPage


class TestLoginFromMainPage:

    @allure.suite("Тесты основной страницы")
    @allure.title("Тест на отображение ссылки к странице логина")
    @allure.description("Проверяет возможность перехода с главной страницы на страницу логина")
    def test_guest_should_see_login_link(self, browser):

        with allure.step("Переход на главную страницу сайта"):
            page = MainPage(browser=browser, url="http://selenium1py.pythonanywhere.com/")
            page.open()

        with allure.step("Проверка ссылки на страницу логин"):
            page.should_be_login_link()

    @allure.suite("Тесты основной страницы")
    @allure.title("Тест на возможность перехода к странице логина")
    @allure.description("Проверяет возможность перехода с главной страницы на страницу логина")
    def test_guest_can_go_to_login_page(self, browser):

        with allure.step("Переход на главную страницу сайта"):
            page = MainPage(browser=browser, url="http://selenium1py.pythonanywhere.com/")
            page.open()

        with allure.step("Переход на страницу логина"):
            page.go_to_login_page()

    @allure.suite("Тесты страницы логина")
    @allure.title("Тест содержания страницы логина")
    @allure.description("Проверяет содержание страницы логина")
    def test_login_page_content(self, browser):

        with allure.step("Переход на главную страницу сайта"):
            page = LoginPage(browser=browser, url="http://selenium1py.pythonanywhere.com/")
            page.open()

        with allure.step("Переход на страницу логина"):
            page.go_to_login_page()

        with allure.step("Проверка содержимого страницы"):
            page.should_be_login_link()


class TestItemFromMainPage:

    @allure.suite("Тесты основной страницы")
    @allure.title("Тест переход в корзину")
    @allure.description("Переходит в пустую корзину и ожидает текст, что корзина пуста")
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):

        with allure.step("Переход на главную страницу сайта"):
            page = MainPage(browser=browser, url="http://selenium1py.pythonanywhere.com/")
            page.open()

        with allure.step("Переход в корзину"):
            page.go_to_basket()

        with allure.step("Ожидаем, что в корзине нет товаров"):
            page = BasketPage(browser=browser, url=page.browser.current_url)
            page.is_basket_empty()

        with allure.step("Ожидаем, что есть текст о том что корзина пуста"):
            page = BasketPage(browser=browser, url=page.browser.current_url)
            page.is_basket_empty_message()
