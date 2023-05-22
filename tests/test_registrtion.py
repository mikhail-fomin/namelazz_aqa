import time
from pages.main_page import MainPage,Authorization, Registration, SmokeTest
import pytest





"""Регистрация"""
class TestRegistration:
        # Регистрация с валидными данными с лояльностью
        def test_registrtion_with_loyal(self, driver):
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


        # Регистрация с валидными данными без лояльности с параметризацией
        @pytest.mark.parametrize("first_name, last_name, email, date_of_birth, password",
                                 [("Пётр", "345678990ht", "yi22ertyu1@syinxun.com", "24.12.1991", "Test1Test1"),
                                  ("Кирилл2", "Курочкин", "yi222muuy98+2@syinxun.com", "04.05.2002", "Test2Test2"),
                                  ("Олег", "Васильев", "yi222rrrrrrrrrrlev798+3@syinxun.com", "15.05.1980", "Test03Test3")])
        def test_registrtion_param(self, driver, first_name, last_name, email, date_of_birth, password):
            page = Registration(driver, "https://namelazz.com/")
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.click_go_to_registration()
            time.sleep(4)
            page.fill_registration_fields_with_param(first_name, last_name, email, date_of_birth, password)
            page.button_create_account()
            time.sleep(5)
            text_reg_successful = page.text_successful_reg()
            print(text_reg_successful)
            time.sleep(5)

        # Регистрация с валидными данными без лояльности
        def test_registrtion_witout_loyal(self, driver):
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

        # Регистрация с вводом зарегестрированного email
        def test_registrtion_witout_loyal_no_valid(self, driver):
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
            assert text_error_mail == 'Пользователь с такой почтой уже существует',\
                f"Текст ошибки {text_error_mail} не свопадает с 'Пользователь с такой почтой уже существует'"
            time.sleep(5)