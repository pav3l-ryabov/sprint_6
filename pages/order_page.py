import time
import allure
import pytest
from data.test_data import ORDER_DATA_1, ORDER_DATA_2
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Создание заказа')
    def set_order(self, name_locator, name_data, last_name_locator, last_name_data, address_locator,
                  address_data, selector_metro_locator, metro_station, phone_number_locator, phone_data, enter_locator,
                  date_locator, date_data, days_of_rent_selector, days_of_rent_locator, order_button, yes_button):
        self.add_text_to_element(name_locator, name_data)
        self.add_text_to_element(last_name_locator, last_name_data)
        self.add_text_to_element(address_locator, address_data)
        self.click_to_element(selector_metro_locator)
        self.click_to_element(metro_station)
        self.add_text_to_element(phone_number_locator, phone_data)
        self.click_to_element(enter_locator)
        self.add_text_to_element(date_locator, date_data)
        self.click_to_element(order_button) # Команда для того, чтобы убрать датапикер
        self.click_to_element(days_of_rent_selector)
        self.click_to_element(days_of_rent_locator)
        self.click_to_element(order_button)
        self.click_to_element(yes_button)

    @allure.step('Проверка, что заказ создался')
    def check_order(self, locator):
        return self.get_text_from_element(locator)

