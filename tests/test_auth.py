import time
import string
import pytest

from pages.main_page import MainPage,Authorization, Registration, SmokeTest
from pages.base_page import BasePage


class TestElements:
    """Авторизация"""
    class TestAuthorization:
        def test_auth_valid_main_page(self, driver): #ввод валидных данных для авторизации
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.fill_auth_fields_valid("admin@namelazz.com", "wSTaR9b5mcPuVZaJ")
            time.sleep(5)
            page.log_in_when_auth()
            greeting = page.check_greeting()
            assert greeting == "ПРИВЕТ, АННА!", f"Приветствие в ЛК {greeting} не совпадает с 'ПРИВЕТ, АННА!'"


        def test_auth_no_valid_email_main_page(self,driver): #ввод не валидного email
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.fill_auth_fields_valid("notvalid@namelazz.com", "wSTaR9b5mcPuVZaJ")
            time.sleep(5)
            text_error = page.text_error_auth()
            assert text_error == "Пожалуйста, введите правильные E-mail и пароль. Оба поля могут быть чувствительны к регистру.", f'Нет текста ошибки авторизации или текст ошибки {text_error} не совпадает '

        def test_auth_no_valid_password_main_page(self,driver): #ввод не валидного пароля
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.fill_auth_fields_valid("admin@namelazz.com", "788545599855")
            time.sleep(5)
            text_error = page.text_error_auth()
            assert text_error == "Пожалуйста, введите правильные E-mail и пароль. Оба поля могут быть чувствительны к регистру.", f'Нет текста ошибки авторизации или текст ошибки {text_error} не совпадает '

    """Регистрация"""
    class TestRegistration:
        def test_registrtion_valid(self,driver):#Регистрация с валидными данными
            page = Registration(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.click_go_to_registration()
            time.sleep(4)
            page.fill_registration_fields("Тест", "Проверочкин","vogowiw444@soombo.com","24091996", "Test1Test1")
            page.chekbox_sig_in_loyal("+79998885544")
            page.button_create_account()
            time.sleep(5)
    """Smoke test"""
    class TestSmoke:
        def test_smoke_test(self,driver):
            page = SmokeTest(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.burger_menu()
            page.catalog()
            page.choose_size()
            text_name_product_price_color_size = page.text_name_price_color_size_page_product()
            page.button_add_basket()
            text_name_product_price_color_size_basket = page.text_name_price_color_size_in_basket()
            print(f"Название,цена,цвет,размер на странице продукта: {text_name_product_price_color_size}")
            print(f"Название,цена,цвет,размер в корзине:{text_name_product_price_color_size_basket}")
            assert text_name_product_price_color_size == text_name_product_price_color_size_basket, f"Отличаются данные на странице продукта{text_name_product_price_color_size} от данных в корзине{text_name_product_price_color_size_basket}"
            page.button_checkout()
            name_price_color_size_text_checkout = page.name_price_color_size_text_checkout()
            assert text_name_product_price_color_size_basket == name_price_color_size_text_checkout, f"Отличаются данные в корзине {text_name_product_price_color_size_basket} от данных на странице оформления {name_price_color_size_text_checkout}"
            print(f"Название,цена,цвет,размер на странцие оформления: {name_price_color_size_text_checkout}")
            page.data_filling("Россия\n","Санкт-Петербург\n","190013","Невский пр-кт\n","12","556","Олег","Тестович","test@mail.ru", "+79998885544", "Тестовый текст для проверки поля коммент")
            page.radiobutton_choose_delivery()
            price_checkout = page.price_checkout()
            cost_of_goods = page.information_about_order()
            print(f"цена товара:{price_checkout} цена в информации:{cost_of_goods}")
            radiobutton_delivety_cost = page.radiobutton_delivety_cost()
            delivery_cost_in_information_about_order = page.delivery_cost_in_information_about_order()
            print(f"Стоимость выбранной доставки:{radiobutton_delivety_cost}, стоимость в информации о товаре{delivery_cost_in_information_about_order}")
            assert radiobutton_delivety_cost == delivery_cost_in_information_about_order,f"Выбранная стоимость доставки{radiobutton_delivety_cost} отличается от указанной в информации о товаре {delivery_cost_in_information_about_order}"



            time.sleep(10)