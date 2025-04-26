from locators.order_page_locators import OrderPageLocators

ANSWERS_DATA = [
    'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
    'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
    'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
    'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
    'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
    'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
    'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
    'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
]

URL_MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'

ORDER_DATA_1 = (
    OrderPageLocators.NAME_INPUT, "Иван",
    OrderPageLocators.LAST_NAME_INPUT, "Иванов",
    OrderPageLocators.ADDRESS_INPUT, "Москва",
    OrderPageLocators.SELECTOR_METRO, OrderPageLocators.METRO_STATION_1,
    OrderPageLocators.PHONE_NUMBER_INPUT, "79999999999",
    OrderPageLocators.ENTER_BUTTON,
    OrderPageLocators.DATE_INPUT, "01.01.2026",
    OrderPageLocators.DAYS_OF_RENT_SELECTOR, OrderPageLocators.ONE_DAYS_OF_RENT,
    OrderPageLocators.ORDER_BUTTON,
    OrderPageLocators.YES_BUTTON
)

ORDER_DATA_2 = (
    OrderPageLocators.NAME_INPUT, "Пётр",
    OrderPageLocators.LAST_NAME_INPUT, "Петров",
    OrderPageLocators.ADDRESS_INPUT, "Санкт-Петербург",
    OrderPageLocators.SELECTOR_METRO, OrderPageLocators.METRO_STATION_2,
    OrderPageLocators.PHONE_NUMBER_INPUT, "78888888888",
    OrderPageLocators.ENTER_BUTTON,
    OrderPageLocators.DATE_INPUT, "02.02.2026",
    OrderPageLocators.DAYS_OF_RENT_SELECTOR, OrderPageLocators.TWO_DAYS_OF_RENT,
    OrderPageLocators.ORDER_BUTTON,
    OrderPageLocators.YES_BUTTON
)