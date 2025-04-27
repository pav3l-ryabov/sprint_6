from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.test_data import URL_MAIN_PAGE
import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestRedirectPage:

    @allure.title('Тест перехода на домашнюю страницу')
    def test_redirect_to_home(self, driver):
        driver.get(URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_to_element(MainPageLocators.ORDER_BUTTON_TOP)
        main_page.click_to_element(MainPageLocators.HOME_BUTTON)
        assert 'Привезём его прямо к вашей двери' in main_page.get_text_from_element(MainPageLocators.HOME_TEXT)

    @allure.title('Тест перехода на главную страницу Яндекс')
    def test_redirect_to_dzen(self, driver):
        driver.get(URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_to_element(MainPageLocators.YANDEX_LOGO)
        main_page.switch_to()
        main_page.wait_for_url_to_be("https://dzen.ru/?yredirect=true")
        assert main_page.get_current_url() == "https://dzen.ru/?yredirect=true"

