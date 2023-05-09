import time
import string
import pytest

from pages.main_page import MainPage,Authorization, Registration, SmokeTest
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from data import data
from random import randint, randrange
class TestElements:
    """Регистрация"""
    class TestRegistration:
        def test_registrtion_with_loyal(self, driver):  # Регистрация с валидными данными с лояльностью
            page = Registration(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.click_go_to_registration()
            time.sleep(4)
            page.fill_registration_fields("Тест", "Проверочкин", "vogowiw444@soombo.com", "24091996", "Test1Test1")#надо менять email на не зарегестрированный
            page.chekbox_sig_in_loyal("+79998885544")
            page.button_create_account()
            time.sleep(5)

        def test_registrtion_witout_loyal(self, driver):  # Регистрация с валидными данными
            page = Registration(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.click_go_to_registration()
            time.sleep(4)
            page.fill_registration_fields("Тест", "Проверочкин", "yi222lev798@syinxun.com", "24051990", "Test1Test1")#надо менять email на тот что не зарегестрирован
            page.button_create_account()
            time.sleep(5)
            text_reg_successful = page.text_successful_reg()
            print(text_reg_successful)
            time.sleep(5)


        def test_registrtion_witout_loyal_no_valid(self, driver):#Регистрация с вводом зарегестрированного email
            page = Registration(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.click_go_to_registration()
            time.sleep(4)
            page.fill_registration_fields("Тест", "Проверочкин", "admin@namelazz.com", "24051990", "Test1Test1")
            page.button_create_account()
            time.sleep(5)
            text_error_mail = page.text_error_mail()
            assert text_error_mail == 'Пользователь с такой почтой уже существует', f"Текст ошибки {text_error_mail} не свопадает с 'Пользователь с такой почтой уже существует'"
            time.sleep(5)


    """Авторизация"""
    class TestAuthorization:
        def test_auth_valid_data(self, driver): #ввод валидных данных для авторизации
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


        def test_auth_no_valid_email(self,driver): #ввод не валидного email
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.fill_auth_fields_valid("notvalid@namelazz.com", "wSTaR9b5mcPuVZaJ")
            time.sleep(5)
            text_error = page.text_error_auth()
            assert text_error == "Пожалуйста, введите правильные E-mail и пароль. Оба поля могут быть чувствительны к регистру.", f'Нет текста ошибки авторизации или текст ошибки {text_error} не совпадает '


        def test_auth_no_valid_password(self,driver): #ввод не валидного пароля
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.fill_auth_fields_valid("admin@namelazz.com", "7885ewfwefew455855")
            time.sleep(5)
            text_error = page.text_error_auth()
            assert text_error == "Пожалуйста, введите правильные E-mail и пароль. Оба поля могут быть чувствительны к регистру.", f'Нет текста ошибки авторизации или текст ошибки {text_error} не совпадает '

        def test_auth_go_to_page_policy(self,driver):#переход с авторизации по ссылке на политику персональных данных
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.click_policy()
            page_policy = page.page_policy()
            assert page_policy == "ПОЛИТИКА В ОТНОШЕНИИ ОБРАБОТКИ ПЕРСОНАЛЬНЫХ ДАННЫХ", f"Текст {page_policy} не совпадает с 'ПОЛИТИКА В ОТНОШЕНИИ ОБРАБОТКИ ПЕРСОНАЛЬНЫХ ДАННЫХ'"

        def test_forgot_password(self,driver):  #ОШИБКА С локатором, текст не возвращается
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.click_forgot_password()
            page.restore_password("admin@namelazz.com")
            time.sleep(5)
            text_password_recovery = page.text_restore
            assert text_password_recovery == "E-mail с восстановлением отправлен",f"Текст {text_password_recovery} не совпадает с 'E-mail с восстановлением отправлен'"
            time.sleep(5)

        def test_forgot_password_no_valid_email(self,driver):#Ввести email не зарегестрированного пользователя
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.click_forgot_password()
            page.restore_password("test@test.com")
            restore_error_text = page.restore_error_text()
            assert restore_error_text == "Данный e-mail не зарегистрирован", f"Текст ошибки{restore_error_text} не совпадает с 'Данный e-mail не зарегистрирован'"

    """Smoke test"""
    class TestSmoke:
        def test_smoke_test(self,driver):#Смоук тест
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
            assert text_name_product_price_color_size == text_name_product_price_color_size_basket, f"Отличаются данные на странице продукта{text_name_product_price_color_size} от данных в корзине{text_name_product_price_color_size_basket}"
            page.button_checkout()
            name_price_color_size_text_checkout = page.name_price_color_size_text_checkout()
            assert text_name_product_price_color_size_basket == name_price_color_size_text_checkout, f"Отличаются данные в корзине {text_name_product_price_color_size_basket} от данных на странице оформления {name_price_color_size_text_checkout}"
            page.data_filling("Россия\n","Санкт-Петербург\n","190013","Невский пр-кт\n","12","556","Олег","Тестович","test@mail.ru", "+79998885544", "Тестовый текст для проверки поля коммент")
            page.radiobutton_choose_delivery()
            price_checkout = page.price_checkout()
            price_products = page.information_about_order()
            assert price_checkout == price_products,f"Цена в списке товаров {price_checkout} отличается от цены в информации о товарах {price_products} "
            radiobutton_delivety_cost = page.radiobutton_delivety_cost()
            delivery_cost_in_information_about_order = page.delivery_cost_in_information_about_order()
            assert radiobutton_delivety_cost == delivery_cost_in_information_about_order,f"Выбранная стоимость доставки{radiobutton_delivety_cost} отличается от указанной в информации о товаре {delivery_cost_in_information_about_order}"
            price_product = page.information_about_order()
            delivery = page.delivery_cost_in_information_about_order().replace("RUB","")
            total_sum_math = str(int(price_product) + int(delivery))
            total_sum = page.total_sum()
            assert total_sum == total_sum_math, f"Итоговая сумма {total_sum} отличается от посчитанной суммы {total_sum_math}"
            page.button_submit()
            ykassa = page.total_ykassa().replace("₽","")
            assert total_sum == ykassa,f"Общая стоимость на Юкасса{ykassa} отличается от итого к оплате на странице инф. о товаре {total_sum}"

            time.sleep(10)

    """Main Page"""
    class TestMainPage:
        def test_subscription(self, driver):#подписка на новости
            page = MainPage(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.subscription("banihe9531@jwsuns.com")
            subscription = page.text_subscription()
            assert subscription == 'СПАСИБО ЗА ПОДПИСКУ! ПОДТВЕРЖДЕНИЕ ОТПРАВЛЕНО ВАМ НА ПОЧТУ.', f"Текст {subscription} не совпадает с 'СПАСИБО ЗА ПОДПИСКУ! ПОДТВЕРЖДЕНИЕ ОТПРАВЛЕНО ВАМ НА ПОЧТУ'"
            time.sleep(5)

        def test_choose_city(self,driver):#выбор города
            page = MainPage(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            city = data.city[randint(1, 19)]
            page.choose_city(city)
            time.sleep(5)
            header_city = page.text_city()
            assert city == header_city, f"Выбранный город {city} отличсется от города в хедере {header_city}"

        def test_catalog_choose_and_back(self, driver):#переключение между каталогами
            page = SmokeTest(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.burger_click()
            page.catalog_click_back()

