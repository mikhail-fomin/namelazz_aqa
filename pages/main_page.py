import random
import time
from random import randint, randrange,random
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from .base_page import BasePage
from locators.element_page_locators import MainPageLocators

"""Главная страница"""
class MainPage(BasePage):

    # Кнопка подтвердить город
    def button_yes_choose_city(self):
        self.click_element(MainPageLocators.BUTTON_YES_CITY)

    # Закрыть модальное окно регистрации
    def close_modal_window(self):
        self.click_element(MainPageLocators.CLOSE_MODAL)

    # Закрыть модалку куки
    def close_modal_cookie(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_COOKIE)

    # Кнопка войти
    def log_in(self):
        self.click_element(MainPageLocators.BUTTON_LOG_IN)

    # Заполнение полей авторизации и нажатие кнопки войти
    def fill_auth_fields_valid(self,email, password):
        self.input_text(MainPageLocators.EMAIL_FIELD, email)
        self.input_text(MainPageLocators.PASSWORD_FIELD, password)
        self.click_element(MainPageLocators.BUTTON_SIGN_IN)

    # Подписаться на новости
    def subscription(self, email):
        self.input_text_keys_enter(MainPageLocators.SUBSCRIPTION, email)
        self.element_is_visibile(MainPageLocators.TEXT_SUBSCRIPTION)

    # Текст успешной подписки на новости
    def text_subscription(self):
        subscription = self.element_is_visibile(MainPageLocators.TEXT_SUBSCRIPTION)
        return subscription.text

    # Выбор города
    def choose_city(self, city):
        self.click_element_without_scroll(MainPageLocators.CHOOSE_CITY)
        time.sleep(3)
        self.input_text_keys_enter_time_sleep_4(MainPageLocators.FIELD_INPUT_CITY, city)

    # Текст выбранный город
    def text_city(self):
        city = self.element_is_visibile(MainPageLocators.TEXT_SELECT_CITY)
        return city.text

    # Переключение между категориями в сайдбаре
    def catalog_click_back(self):
        for indx in range(4):
            catalog_elem = self.elements_are_visibile(MainPageLocators.CATALOG_ELEMENTS)
            self.click_element(catalog_elem[indx])
            self.driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(4)
            self.driver.back()
            self.click_element(MainPageLocators.BUTTON_BURGER)

    # Добавление в избранное нескольких товаров
    def catalog_add_favourites(self):
        for indx in range(3):
            catalog_elem = self.elements_are_visibile(MainPageLocators.CARD_PRODUCT)
            self.click_element(catalog_elem[indx])
            time.sleep(3)
            self.click_element_without_scroll(MainPageLocators.ADD_FAVORITES)
            time.sleep(3)
            self.driver.back()

    # Добавление в избранное 20 товаров
    def catalog_add_favourites_20_products(self):

        amount_cards = 0
        for indx in range(20):
            catalog_elem = self.element_are_present(MainPageLocators.CARD_PRODUCT)
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, 7000);")
            time.sleep(3)
            self.click_element(catalog_elem[indx])
            amount_cards = amount_cards + 1
            time.sleep(3)
            self.click_element_without_scroll(MainPageLocators.ADD_FAVORITES)
            time.sleep(3)
            self.driver.back()
        self.click_element(MainPageLocators.FAVORITES)
        #footer = self.driver.find_element(MainPageLocators.FOOTER)
        #self.driver.execute_script("arguments[0].scrollIntoView();", footer)
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0, 7000);")
        time.sleep(3)
        favorites_elem = self.elements_are_visibile(MainPageLocators.CARD_PRODUCT)
        assert amount_cards == len(favorites_elem), f"Кол-во добавленных элементов {amount_cards} отличается от кол-ва в избранном{len(favorites_elem)}"

    # Клик на кнопку избранное в хедере и переход на страницу избранное
    def favorites(self):
        self.click_element(MainPageLocators.FAVORITES)
        favorites_elem = self.elements_are_visibile(MainPageLocators.CARD_PRODUCT)

    # Удалить из избранного, на странице избранное
    def delete_from_favorites(self):
        list_cards = self.elements_are_visibile(MainPageLocators.DELETE_FROM_FAVORITES)
        sum_cards = len(list_cards)
        self.click_element(list_cards[randint(0, sum_cards)])
        self.driver.refresh()
        new_list_cards = self.elements_are_visibile(MainPageLocators.DELETE_FROM_FAVORITES)
        assert len(new_list_cards) == len(list_cards) - 1, f"Количество карточек в избранном не уменьшилось на 1"

    # Удалить товар из избранного на странице товара
    def delete_from_favorites_on_card(self):

        catalog_elem = self.elements_are_visibile(MainPageLocators.CARD_PRODUCT)
        sum_elem = len(catalog_elem)
        self.click_element(catalog_elem[randint(0, len(catalog_elem) - 1)])
        self.click_element_without_scroll(MainPageLocators.ACTIVE_BUTTON_ADD_FAVORITES)
        self.click_element(MainPageLocators.FAVORITES)
        updated_catalog_elem = self.elements_are_visibile(MainPageLocators.CARD_PRODUCT)
        assert sum_elem - 1 == len(updated_catalog_elem),f"Первоначальное кол-во карточек в избранном {sum_elem}, отличается от кол-ва после удаления {len(updated_catalog_elem)}"



"""Авторизация"""
class Authorization(MainPage):

    # заполнение полей авторизации email, пароль и клик по кнопке войти
    def fill_auth_fields_valid(self,email, password):
        self.input_text(MainPageLocators.EMAIL_FIELD, email)
        self.input_text(MainPageLocators.PASSWORD_FIELD, password)
        self.click_element(MainPageLocators.BUTTON_SIGN_IN)

    # клик по кнопке войти в хедере, если пользователь авторизован
    def log_in_whan_auth(self):
        self.click_element(MainPageLocators.BUTTON_LOG_IN_WHEN_AUTH_USER)

    # получаем текст приветствия в ЛК пользователя
    def check_greeting(self):
        greeting = self.is_element_present(MainPageLocators.GET_GREETING)
        return greeting.text

    # получаем текст ошибки, при невалидной авторизации
    def text_error_auth(self):
        text_error = self.is_element_present(MainPageLocators.TEXT_ERROR_AUTH)
        return text_error.text

    # клик по ссылке политика
    def click_policy(self):
        click_policy = self.click_element(MainPageLocators.LINK_GO_TO_POLICY)

    # получаем текст заголовка на странице политика
    def page_policy(self):
        page_policy = self.element_is_visibile(MainPageLocators.PAGE_POLICY)
        return page_policy.text

    # клик по кнопке забыл пароль
    def click_forgot_password(self):
        self.click_element(MainPageLocators.BUTTON_FORGOT_PASSWORD)

    # ввод email и клик по кнопке восстановить
    def restore_password(self,email):
        self.input_text(MainPageLocators.FIELD_EMAIL_RESTORE_PASSWORD,email)
        self.click_element(MainPageLocators.BUTTON_RESTORE)

    # получаем текст об успешной отправке письма с восстановлением на почту
    def restore_text(self):
        text_password_recovery = self.is_element_present(MainPageLocators.TEXT_PASSWORD_RECOVERY)
        return text_password_recovery.text


    def text_restore(self):
        text_rest = self.element_is_visibile(MainPageLocators.TEXT_PASSWORD_RECOVERY)
        return text_rest.text()

    # получаем текст ошибки восстановления, при вводе незарегестрированного email
    def restore_error_text(self):
        text_error_password_recovery = self.element_is_visibile(MainPageLocators.TEXT_ERROR_PASSWORD_RECOVERY)
        return text_error_password_recovery.text

    # клик по бургер меню
    def burger_click(self):
        self.click_element(MainPageLocators.BUTTON_BURGER)

    # Клик бургер меню->одежда->показать всё
    def burger_menu(self):
        self.click_element(MainPageLocators.BUTTON_BURGER)
        self.click_element(MainPageLocators.BUTTON_CLOTHES)
        self.click_element(MainPageLocators.BUTTON_LOOK_ALL)


    """Каталог"""

    # находим карточки продукта и кликаем по ним
    def catalog(self):
        cards_product = self.elements_any_are_visibile(MainPageLocators.CARD_PRODUCT)
        self.click_element(cards_product[randint(0, 10)])
        print(f"Кол-во видимых элементов:{len(cards_product)}")



"""Регистрация"""
class Registration(MainPage):

    # клик регистрация в сайдбаре
    def click_go_to_registration(self):
        self.click_element(MainPageLocators.BUTTON_GO_TO_REGISTRATION)

    # заполнение полей регистрации
    def fill_registration_fields_with_param(self, first_name, last_name, email, date_of_birth, password):
        self.input_text(MainPageLocators.FIRST_NAME_FIELD, first_name)
        self.input_text(MainPageLocators.LAST_NAME_FIELD, last_name)
        self.input_text(MainPageLocators.EMAIL_REGISTRATION_FIELD, email)
        self.input_text(MainPageLocators.DATE_OF_BIRTH, date_of_birth)
        self.input_text(MainPageLocators.PASSWORD_REGISTRATION_FIELD1, password)
        self.input_text(MainPageLocators.PASSWORD_REGISTRATION_FIELD2, password)

    # заполнение полей регистрации
    def fill_registration_fields(self, first_name, last_name, email, date_of_birth, password):
        self.input_text(MainPageLocators.FIRST_NAME_FIELD, first_name)
        self.input_text(MainPageLocators.LAST_NAME_FIELD, last_name)
        self.input_text(MainPageLocators.EMAIL_REGISTRATION_FIELD, email)
        self.input_text(MainPageLocators.DATE_OF_BIRTH, date_of_birth)
        self.input_text(MainPageLocators.PASSWORD_REGISTRATION_FIELD1, password)
        self.input_text(MainPageLocators.PASSWORD_REGISTRATION_FIELD2, password)

    # клик по чекбоксу принять лояльность
    def chekbox_sig_in_loyal(self,number):
        self.click_element(MainPageLocators.CHECKBOX_SIG_IN_LOYALTY)
        self.input_text(MainPageLocators.ENTER_NUMBER, number)
        self.click_element(MainPageLocators.BUTTON_CONFIRM_LOYALTY)

    # кнопка создать аккаунт
    def button_create_account(self):
        self.click_element(MainPageLocators.BUTTON_CREATE_ACCOUNT)

    # получаем текст ошибки, при вводе зарегестрированного email
    def text_error_mail(self):
        error_mail_text = self.is_element_present(MainPageLocators.TEXT_ERROR_MAIL)
        return error_mail_text.text

    # получаем текст об успешной регистрации
    def text_successful_reg(self):
        text_succ_reg = self.element_is_visibile(MainPageLocators.TEXT_SUCCESSFUL_REGISTRATION)
        return text_succ_reg.text

"""Смоук тест"""
class SmokeTest(MainPage):

    """Бургер меню"""

    # клик по кнопке бургер меню
    def burger_click(self):
        self.click_element(MainPageLocators.BUTTON_BURGER)

    # Клик бургер меню->одежда->показать всё
    def burger_menu(self):
        self.click_element(MainPageLocators.BUTTON_BURGER)
        self.click_element(MainPageLocators.BUTTON_CLOTHES)
        self.click_element(MainPageLocators.BUTTON_LOOK_ALL)

    """Каталог"""
    # находим список продуктов и кликаем по случайной карточке
    def catalog(self):
        cards_product = self.elements_any_are_visibile(MainPageLocators.CARD_PRODUCT)
        self.click_element(cards_product[randint(0, 9)])
        print(f"Кол-во видимых элементов:{len(cards_product)}")



    """Страница продукта"""

    # получаем список доступных размеров для товара и кликаем по случайному размеру
    def choose_size(self):
        choose_size = self.elements_are_visibile(MainPageLocators.CHOOSE_SIZE)
        self.click_element(choose_size[randrange(len(choose_size))])
        print(f"Кол-во доступных размеров:{len(choose_size)}")

    # получаем текст названия продукта, цены, цвета, активного размера
    def text_name_price_color_size_page_product(self):
        text_name_product = self.is_element_present(MainPageLocators.NAME_PRODUCT)
        text_price_product = self.is_element_present(MainPageLocators.PRICE_PRODUCT)
        product_color = self.is_element_present(MainPageLocators.ACTIVE_COLOR)
        active_size = self.is_element_present(MainPageLocators.ACTIVE_SIZE)
        return text_name_product.text.upper(), text_price_product.text, product_color.get_attribute("title"), active_size.text

    # клик по кнопке добавить в корзину
    def button_add_basket(self):
        self.click_element_without_scroll(MainPageLocators.BUTTON_ADD_BASKET)


    """Корзина"""

    # получаем в корзине текст названия продукта, цены, цвета, размера
    def text_name_price_color_size_in_basket(self):
        text_name_product_in_basket = self.element_is_visibile(MainPageLocators.NAME_PRODUCT_BASKET) #для одного товара в корзине
        text_price_product_in_basket = self.element_is_visibile(MainPageLocators.PRICE_PRODUCT_BASKET) #для одного товара в корзине
        text_color_product_in_basket = self.element_is_visibile(MainPageLocators.COLOR_PRODUCT_BASKET)#для одного товара в корзине
        text_size_product_in_basket = self.element_is_visibile(MainPageLocators.SIZE_PRODUCT_BASKET)#для одного товара в корзине
        return text_name_product_in_basket.text, text_price_product_in_basket.text,\
            text_color_product_in_basket.get_attribute("title"),text_size_product_in_basket.text.replace('Размер\n', '').upper()

    # клик по кнопке оформить заказ
    def button_checkout(self):
        self.click_element_without_scroll(MainPageLocators.BUTTON_CHECKOUT)

    # кнопка удалить из корзины
    def delete_from_basket(self):
        self.click_element(MainPageLocators.BUTTON_DELETE_PRODUCT_FROM_BASKET)

    # получаем текст корзина пуста
    def text_empty_basket(self):
        empty_basket = self.element_is_visibile(MainPageLocators.TEXT_EMPTY_BASKET)
        return empty_basket.text

    # 1цикл добавления нескольких продуктов в корзину и проверка соответствия суммы добавленных товаров с итоговой суммой в корзине
    def add_few_products_to_basket(self):

        count_products = []
        for indx in range(5):
            catalog_elem = self.elements_are_visibile(MainPageLocators.CARD_PRODUCT)
            self.click_element(catalog_elem[indx])
            product_price = self.element_is_visibile(MainPageLocators.PRICE_PRODUCT).text
            count_products.append(int(product_price.replace(" RUB", "")))
            choose_size = self.elements_are_visibile(MainPageLocators.CHOOSE_SIZE)
            self.click_element(choose_size[randrange(len(choose_size))])
            self.click_element_without_scroll(MainPageLocators.BUTTON_ADD_BASKET)
            self.driver.back()
        print(count_products)
        sum_price = sum(count_products)
        return str(sum_price)

    # 2цикл добавления нескольких продуктов в корзину и проверка соответствия суммы добавленных товаров с итоговой суммой в корзине
    def add_few_products_to_basket2(self):

        count_products = []
        while len(count_products) != 5:
            catalog_elem = self.element_are_present(MainPageLocators.CARD_PRODUCT)
            indexes = list(range(len(catalog_elem)))
            for i in indexes:
                    self.click_element(catalog_elem[randint(0,i)])
                    #used_indexes.append(i)
                    product_price = self.element_is_visibile(MainPageLocators.PRICE_PRODUCT).text
                    count_products.append(int(product_price.replace(" RUB", "")))
                    choose_size = self.elements_are_visibile(MainPageLocators.CHOOSE_SIZE)
                    self.click_element(choose_size[randrange(len(choose_size))])
                    self.click_element_without_scroll(MainPageLocators.BUTTON_ADD_BASKET)
                    self.driver.back()
                    catalog_elem = self.elements_any_are_visibile(MainPageLocators.CARD_PRODUCT)
                    if len(count_products) == 5:
                        break
        sum_price = sum(count_products)
        return str(sum_price)


    # получаем текст суммы итого в корзине
    def basket_sum(self):
        self.click_element(MainPageLocators.BUTTON_BASKET)
        sum_basket = self.element_is_visibile(MainPageLocators.SUM_PRICE_BASKET)
        return sum_basket.text.replace(" RUB", "")

    """"Оформление заказа """

    # получаем текст названия продкутка, цены, цвета, размера на странице оформления заказ
    def name_price_color_size_text_checkout(self):
        name_product_checkout = self.element_is_visibile(MainPageLocators.NAME_PRODUCT_CHECKOUT)
        price_checkout = self.element_is_visibile(MainPageLocators.PRICE_PRODUCT_CHECKOUT)
        color_checkout = self.element_is_visibile(MainPageLocators.COLOR_PRODUCT_CHECHOUT)
        size_checkot = self.element_is_visibile(MainPageLocators.SIZE_PRODUCT_CHECHOUT)
        return name_product_checkout.text, price_checkout.text,color_checkout.get_attribute("title"),size_checkot.text.replace('Размер\n', '').upper()

    # заполнение полей оформления заказа
    def data_filling(self, country, city, index, street, house, apartment,name, first_name, email, number, comment):
        time.sleep(3)
        fill_country = self.input_text(MainPageLocators.COUNTRY, country)
        time.sleep(3)
        self.click_element_without_scroll(MainPageLocators.COUNTRY)
        time.sleep(5)
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

    # выбираем тип доставки
    def radiobutton_choose_delivery(self):
        radiobutton = self.click_element(MainPageLocators.RADIOBUTTON_ORDER)

    # получаем текст цены доставки
    def radiobutton_delivety_cost(self):
        radiobutton_delivety_cost = self.element_is_visibile(MainPageLocators.RADIOBUTTON_DELIVERY_COST)
        return radiobutton_delivety_cost.text

    # получаем текст цены продукта на странице оформления заказа в списке товаров
    def price_checkout(self):
        price_checkout = self.element_is_visibile(MainPageLocators.PRICE_PRODUCT_CHECKOUT)
        return price_checkout.text.replace(' RUB', '')

    # получаем текст стоимости товара в информации о заказе
    def information_about_order(self):
        cost_of_goods = self.element_is_visibile(MainPageLocators.COST_OF_GOODS)
        return cost_of_goods.text

    # получаем текст стоимость доставки в информации о заказе
    def delivery_cost_in_information_about_order(self):
        delivery_cost_information_order = self.element_is_visibile(MainPageLocators.DELIVERY)
        return delivery_cost_information_order.text

    # получаем текст итоговой суммы к оплате
    def total_sum(self):
        total_sum = self.element_is_visibile(MainPageLocators.TOTAL_SUM)
        return total_sum.text

    # клик по кнопке сделать заказ
    def button_submit(self):
        self.click_element(MainPageLocators.BUTTON_ORDER_SUBMIT)

    # получаем текст итоговой суммы заказа на странцие платёжной системы
    def total_ykassa(self):
        ykassa_total = self.element_is_visibile(MainPageLocators.TOTAL_SUM_Y_KASSA)
        return ykassa_total.get_attribute('aria-label')









