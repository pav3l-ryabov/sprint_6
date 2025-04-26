from data.test_data import URL_MAIN_PAGE, ORDER_DATA_1, ORDER_DATA_2
import pytest
import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.title('Тесты заказов')
class TestOrderPage:

    @pytest.mark.parametrize(
        'order_button_locator, order_data',
        [
            (MainPageLocators.ORDER_BUTTON_TOP, ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_BOTTOM, ORDER_DATA_2)
        ]
    )
    def test_create_order(self, driver, order_button_locator, order_data):
        driver.get(URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.scroll_to_element(order_button_locator)
        main_page.click_to_element(order_button_locator)
        order_page = OrderPage(driver)
        order_page.set_order(*order_data)
        assert order_page.check_order(OrderPageLocators.CHECK_ORDER_STATUS) == 'Посмотреть статус'
