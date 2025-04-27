from data.test_data import ANSWERS_DATA, URL_MAIN_PAGE
import allure
import pytest
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Тесты вопросов о важном')
    @pytest.mark.parametrize('num', range(len(ANSWERS_DATA)))
    def test_questions_and_answers(self, driver, num):
        driver.get(URL_MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_to_question(num)
        actual = main_page.get_answer_text(num)
        assert actual == ANSWERS_DATA[num]

