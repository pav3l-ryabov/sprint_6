from data.test_data import URL_MAIN_PAGE
import allure
from pages.main_page import MainPage


class TestRedirectPage:

    @allure.title('Тест перехода на домашнюю страницу')
    def test_redirect_to_home(self, driver):
        driver.get(URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_top_order_button()
        main_page.click_home_button()
        assert 'Привезём его прямо к вашей двери' in main_page.get_home_heading()

    @allure.title('Тест перехода на главную страницу Яндекс')
    def test_redirect_to_dzen(self, driver):
        driver.get(URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to()
        main_page.wait_for_url_to_be("https://dzen.ru/?yredirect=true")
        assert main_page.get_current_url() == "https://dzen.ru/?yredirect=true"

