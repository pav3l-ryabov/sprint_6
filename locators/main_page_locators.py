from selenium.webdriver.common.by import By

class MainPageLocators:

    QUESTION = (By.XPATH, '//*[@id="accordion__heading-{}"]')
    ANSWER = (By.XPATH, '//*[@id="accordion__panel-{}"]')
    LAST_QUESTION = (By.XPATH, '//*[@id="accordion__heading-7"]')

    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CLASS_NAME, "Button_UltraBig__UU3Lp")

    HOME_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    HOME_TEXT = (By.XPATH, "//div[contains(text(), 'Привезём его прямо к вашей двери')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex') and contains(@href, 'yandex.ru')]")
