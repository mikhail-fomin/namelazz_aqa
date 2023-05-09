import time
from random import randint, randrange

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from .base_page import BasePage
from locators.element_page_locators import MainPageLocators

"""Главная страница"""
class MainPage(BasePage):
    def button_yes_choose_city(self):
        self.click_element2(MainPageLocators.BUTTON_YES_CITY)

    def close_modal_window(self):
        self.click_element(MainPageLocators.CLOSE_MODAL)

    def close_modal_cookie(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_COOKIE)

    def log_in(self):
        self.click_element(MainPageLocators.BUTTON_LOG_IN)

    def subscription(self, email):
        self.input_text_keys_enter(MainPageLocators.SUBSCRIPTION, email)
        self.element_is_visibile(MainPageLocators.TEXT_SUBSCRIPTION)

    def text_subscription(self):
        subscription = self.element_is_visibile(MainPageLocators.TEXT_SUBSCRIPTION)
        return subscription.text

    def choose_city(self, city):
        self.click_element_without_scroll(MainPageLocators.CHOOSE_CITY)
        time.sleep(3)
        self.input_text_keys_enter_time_sleep_4(MainPageLocators.FIELD_INPUT_CITY, city)


    def text_city(self):
        city = self.element_is_visibile(MainPageLocators.TEXT_SELECT_CITY)
        return city.text

    def catalog_click_back(self):
        for indx in range(4):
            catalog_elem = self.elements_are_visibile(MainPageLocators.CATALOG_ELEMENTS)
            self.click_element(catalog_elem[indx])
            self.driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(4)
            self.driver.back()
            self.click_element(MainPageLocators.BUTTON_BURGER)


"""Авторизация"""
class Authorization(MainPage):
    def fill_auth_fields_valid(self,email, password):
        self.input_text(MainPageLocators.EMAIL_FIELD, email)
        self.input_text(MainPageLocators.PASSWORD_FIELD, password)
        self.click_element(MainPageLocators.BUTTON_SIGN_IN)

    def log_in_when_auth(self):
        self.click_element(MainPageLocators.BUTTON_LOG_IN_WHEN_AUTH_USER)

    def check_greeting(self):
        greeting = self.is_element_present(MainPageLocators.GET_GREETING)
        return greeting.text

    def text_error_auth(self):
        text_error = self.is_element_present(MainPageLocators.TEXT_ERROR_AUTH)
        return text_error.text

    def click_policy(self):
        click_policy = self.click_element(MainPageLocators.LINK_GO_TO_POLICY)

    def page_policy(self):
        page_policy = self.element_is_visibile(MainPageLocators.PAGE_POLICY)
        return page_policy.text

    def click_forgot_password(self):
        self.click_element(MainPageLocators.BUTTON_FORGOT_PASSWORD)

    def restore_password(self,email):
        self.input_text(MainPageLocators.FIELD_EMAIL_RESTORE_PASSWORD,email)
        self.click_element(MainPageLocators.BUTTON_RESTORE)

    def restore_text(self):
        text_password_recovery = self.is_element_present(MainPageLocators.TEXT_PASSWORD_RECOVERY)
        return text_password_recovery.text


    def text_restore(self):
        text_rest = self.element_is_visibile(MainPageLocators.TEXT_PASSWORD_RECOVERY)
        return text_rest.text()
    def restore_error_text(self):
        text_error_password_recovery = self.element_is_visibile(MainPageLocators.TEXT_ERROR_PASSWORD_RECOVERY)
        return text_error_password_recovery.text

"""Регистрация"""
class Registration(MainPage):

    def click_go_to_registration(self):
        self.click_element(MainPageLocators.BUTTON_GO_TO_REGISTRATION)

    def fill_registration_fields(self, first_name, last_name, email, date_of_birth, password):
        self.input_text(MainPageLocators.FIRST_NAME_FIELD, first_name)
        self.input_text(MainPageLocators.LAST_NAME_FIELD, last_name)
        self.input_text(MainPageLocators.EMAIL_REGISTRATION_FIELD, email)
        self.input_text(MainPageLocators.DATE_OF_BIRTH, date_of_birth)
        self.input_text(MainPageLocators.PASSWORD_REGISTRATION_FIELD1, password)
        self.input_text(MainPageLocators.PASSWORD_REGISTRATION_FIELD2, password)
    def chekbox_sig_in_loyal(self,number):
        self.click_element(MainPageLocators.CHECKBOX_SIG_IN_LOYALTY)
        self.input_text(MainPageLocators.ENTER_NUMBER, number)
        self.click_element(MainPageLocators.BUTTON_CONFIRM_LOYALTY)
    def button_create_account(self):
        self.click_element(MainPageLocators.BUTTON_CREATE_ACCOUNT)

    def text_error_mail(self):
        error_mail_text = self.is_element_present(MainPageLocators.TEXT_ERROR_MAIL)
        return error_mail_text.text

    def text_successful_reg(self):
        text_succ_reg = self.element_is_visibile(MainPageLocators.TEXT_SUCCESSFUL_REGISTRATION)
        return text_succ_reg.text

"""Смоук тест"""
class SmokeTest(MainPage):

    """Бургер меню"""
    def burger_click(self):
        self.click_element(MainPageLocators.BUTTON_BURGER)
    def burger_menu(self):
        self.click_element(MainPageLocators.BUTTON_BURGER)
        self.click_element(MainPageLocators.BUTTON_CLOTHES)
        self.click_element(MainPageLocators.BUTTON_LOOK_ALL)
    """Каталог"""

    def catalog(self):
        cards_product = self.elements_any_are_visibile(MainPageLocators.CARD_PRODUCT)
        self.click_element(cards_product[randint(0, 10)])
        print(f"Кол-во видимых элементов:{len(cards_product)}")



    """Страница продукта"""
    def choose_size(self):
        choose_size = self.elements_are_visibile(MainPageLocators.CHOOSE_SIZE)
        self.click_element(choose_size[randrange(len(choose_size))])#клик по выбранному размер
        print(f"Кол-во доступных размеров:{len(choose_size)}")

    def text_name_price_color_size_page_product(self):
        text_name_product = self.is_element_present(MainPageLocators.NAME_PRODUCT)
        text_price_product = self.is_element_present(MainPageLocators.PRICE_PRODUCT)
        product_color = self.is_element_present(MainPageLocators.ACTIVE_COLOR)
        active_size = self.is_element_present(MainPageLocators.ACTIVE_SIZE)
        return text_name_product.text, text_price_product.text, product_color.get_attribute("title"), active_size.text

    def button_add_basket(self):
        self.click_element_without_scroll(MainPageLocators.BUTTON_ADD_BASKET)


    """Корзина"""
    def text_name_price_color_size_in_basket(self):
        text_name_product_in_basket = self.element_is_visibile(MainPageLocators.NAME_PRODUCT_BASKET) #для одного товара в корзине
        text_price_product_in_basket = self.element_is_visibile(MainPageLocators.PRICE_PRODUCT_BASKET) #для одного товара в корзине
        text_color_product_in_basket = self.element_is_visibile(MainPageLocators.COLOR_PRODUCT_BASKET)#для одного товара в корзине
        text_size_product_in_basket = self.element_is_visibile(MainPageLocators.SIZE_PRODUCT_BASKET)#для одного товара в корзине
        return text_name_product_in_basket.text, text_price_product_in_basket.text,\
            text_color_product_in_basket.get_attribute("title"),text_size_product_in_basket.text.replace('Размер\n', '').upper()

    def button_checkout(self):
        self.click_element_without_scroll(MainPageLocators.BUTTON_CHECKOUT)

    """"Оформление заказа """
    def name_price_color_size_text_checkout(self): #название, цена, цвет, размер продукта в оформлении заказа
        name_product_checkout = self.element_is_visibile(MainPageLocators.NAME_PRODUCT_CHECKOUT)
        price_checkout = self.element_is_visibile(MainPageLocators.PRICE_PRODUCT_CHECKOUT)
        color_checkout = self.element_is_visibile(MainPageLocators.COLOR_PRODUCT_CHECHOUT)
        size_checkot = self.element_is_visibile(MainPageLocators.SIZE_PRODUCT_CHECHOUT)
        return name_product_checkout.text, price_checkout.text,color_checkout.get_attribute("title"),size_checkot.text.replace('Размер\n', '').upper()

    def data_filling(self, country, city, index, street, house, apartment,name, first_name, email, number, comment):#заполняем поля
        time.sleep(3)
        fill_country = self.input_text(MainPageLocators.COUNTRY, country)
        time.sleep(3)
        fill_city = self.input_text(MainPageLocators.CITY, city)
        time.sleep(3)
        fill_index = self.input_text(MainPageLocators.INDEX, index)
        fill_street = self.input_text(MainPageLocators.STREET, street)
        time.sleep(3)
        fill_house = self.input_text(MainPageLocators.HOUSE, house)
        fill_apartment = self.input_text(MainPageLocators.APARTMENT, apartment)
        fill_name = self.input_text(MainPageLocators.NAME_ORDER, name)
        fill_first_name = self.input_text(MainPageLocators.FIRST_NAME_ORDER, first_name)
        fill_email = self.input_text(MainPageLocators.EMAIL_ORDER, email)
        fill_number = self.input_text(MainPageLocators.NUMBER_ORDER, number)
        fill_comment = self.input_text(MainPageLocators.COMMENT_ORDER, comment)

    def radiobutton_choose_delivery(self):#выбираем тип доставки
        radiobutton = self.click_element(MainPageLocators.RADIOBUTTON_ORDER)

    def radiobutton_delivety_cost(self):#текст цены доставки
        radiobutton_delivety_cost = self.element_is_visibile(MainPageLocators.RADIOBUTTON_DELIVERY_COST)
        return radiobutton_delivety_cost.text

    def price_checkout(self):#получаем текст цены продукта на странице оформления заказа в списке товаров
        price_checkout = self.element_is_visibile(MainPageLocators.PRICE_PRODUCT_CHECKOUT)
        return price_checkout.text.replace(' RUB', '')

    def information_about_order(self):#Получаем текст стоимости товара в информации о заказе
        cost_of_goods = self.element_is_visibile(MainPageLocators.COST_OF_GOODS)
        return cost_of_goods.text

    def delivery_cost_in_information_about_order(self):#Получаем текст стоимость доставки в информации о заказе
        delivery_cost_information_order = self.element_is_visibile(MainPageLocators.DELIVERY)
        return delivery_cost_information_order.text

    def total_sum(self):#Получаем текст итоговой суммы к оплате
        total_sum = self.element_is_visibile(MainPageLocators.TOTAL_SUM)
        return total_sum.text

    def button_submit(self):
        self.click_element(MainPageLocators.BUTTON_ORDER_SUBMIT)

    def total_ykassa(self):
        ykassa_total = self.element_is_visibile(MainPageLocators.TOTAL_SUM_Y_KASSA)
        return ykassa_total.get_attribute('aria-label')






