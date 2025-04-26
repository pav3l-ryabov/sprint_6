from selenium.webdriver.common.by import By

class OrderPageLocators:

    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    SELECTOR_METRO = (By.CLASS_NAME, "select-search__input")
    METRO_STATION_1 = (By.XPATH, "//li[@data-index='0']")
    METRO_STATION_2 = (By.XPATH, "//li[@data-index='1']")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    ENTER_BUTTON = (By.XPATH, "//button[text() = 'Далее']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DAYS_OF_RENT_SELECTOR = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    ONE_DAYS_OF_RENT = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    TWO_DAYS_OF_RENT = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    CHECK_ORDER_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")