from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locator(MainPageLocators.QUESTION, num)
        self.scroll_to_element(MainPageLocators.LAST_QUESTION)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locator(MainPageLocators.ANSWER, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверка ответа')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)

    @allure.step('Нажать верхнюю кнопку "Заказать"')
    def click_top_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_TOP)
        self.click_to_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Нажать нижнюю кнопку "Заказать"')
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)