import time
import pytest
import allure
from pages.main_page import MainPage, ItemPage


@allure.title("Тест на возможность перехода к странице логина")
@allure.description("Проверяет возможность перехода с главной страницы на страницу логина")
def test_guest_can_go_to_login_page(browser):

    with allure.step("Переход на главную страницу сайта"):
        page = MainPage(browser=browser, url="http://selenium1py.pythonanywhere.com/")
        page.open()

    with allure.step("Переход на страницу логина"):
        page.go_to_login_page()


# def test_guest_should_see_login_link(browser):
#     LINK = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, LINK)
#     page.open()
#     page.should_be_login_link()
#
#
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     # LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ItemPage(browser, link)
#     page.open()
#     item_name = page.save_item_name()
#     item_price = page.save_item_price()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     time.sleep(3)
#     page.check_item_added_to_basket(item_name)
#     page.check_item_price_in_basket(item_price)
#
#
#
