import time

from pages.main_page import MainPage


#LINK = "http://selenium1py.pythonanywhere.com/"
LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.should_be_login_link()


def test_guest_can_add_product_to_basket(browser):
    page = MainPage(browser, LINK)
    page.open()
    # item_name = page.save_item_name()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # page.check_item_added_to_basket(item_name)

