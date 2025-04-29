from data.test_data import URL_MAIN_PAGE, ORDER_1, ORDER_2
import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Тесты заказов')
    @pytest.mark.parametrize(
        'click_order_button, order_data',
        [
            (MainPage.click_top_order_button, ORDER_1),
            (MainPage.click_bottom_order_button, ORDER_2)
        ]
    )
    def test_create_order(self, driver, click_order_button, order_data):
        driver.get(URL_MAIN_PAGE)
        main_page = MainPage(driver)
        click_order_button(main_page)
        order_page = OrderPage(driver)
        order_page.set_order(order_data)
        assert order_page.get_order_status() == 'Посмотреть статус'
