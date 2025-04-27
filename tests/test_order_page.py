from data.test_data import URL_MAIN_PAGE, ORDER_1, ORDER_2
import pytest
import allure
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Тесты заказов')
    @pytest.mark.parametrize(
        'order_button, order_data',
        [
            ('top', ORDER_1),
            ('bottom', ORDER_2)
        ]
    )
    def test_create_order(self, driver, order_button, order_data):
        driver.get(URL_MAIN_PAGE)
        main_page = MainPage(driver)
        if order_button == 'top':
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()
        order_page = OrderPage(driver)
        order_page.set_order(order_data)
        assert order_page.check_order(OrderPageLocators.CHECK_ORDER_STATUS) == 'Посмотреть статус'
