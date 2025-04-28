import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Создание заказа')
    def set_order(self, order_data: dict):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, order_data["name"])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_INPUT, order_data["last_name"])
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT, order_data["address"])
        self.click_to_element(OrderPageLocators.SELECTOR_METRO)
        if order_data["metro_station_index"] == 0:
            self.click_to_element(OrderPageLocators.METRO_STATION_1)
        elif order_data["metro_station_index"] == 1:
            self.click_to_element(OrderPageLocators.METRO_STATION_2)
        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER_INPUT, order_data["phone"])
        self.click_to_element(OrderPageLocators.ENTER_BUTTON)
        self.add_text_to_element(OrderPageLocators.DATE_INPUT, order_data["date"])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON) # Команда для того, чтобы убрать датапикер
        self.click_to_element(OrderPageLocators.DAYS_OF_RENT_SELECTOR)
        if order_data["rent_time"] == "сутки":
            self.click_to_element(OrderPageLocators.ONE_DAYS_OF_RENT)
        elif order_data["rent_time"] == "двое суток":
            self.click_to_element(OrderPageLocators.TWO_DAYS_OF_RENT)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Проверка, что заказ создался')
    def get_order_status(self):
        return self.get_text_from_element(OrderPageLocators.CHECK_ORDER_STATUS)

