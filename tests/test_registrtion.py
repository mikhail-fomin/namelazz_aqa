import time
from pages.main_page import MainPage,Authorization, Registration, SmokeTest
import pytest
from data.generator import Generator




"""Регистрация"""
class TestRegistration:
        # Регистрация с валидными данными с лояльностью
        def test_registrtion_with_loyal(self, driver):
            page = Registration(driver, "https://namelazz.com/")
            generator = Generator
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.click_go_to_registration()
            time.sleep(4)
            page.fill_registration_fields(generator.last_name, generator.first_name, generator.email,
                                          generator.date_of_birth, "Test1Test1")
            page.chekbox_sig_in_loyal("+79998885544")
            page.button_create_account()




        # Регистрация с валидными данными без лояльности
        def test_registrtion_witout_loyal(self, driver):
            page = Registration(driver, "https://namelazz.com/")
            generator = Generator
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.click_go_to_registration()
            time.sleep(4)
            page.fill_registration_fields(generator.last_name, generator.first_name, generator.email,
                                          generator.date_of_birth, "Test1Test1")
            page.button_create_account()
            time.sleep(5)
            text_reg_successful = page.text_successful_reg()
            print(text_reg_successful)


        # Регистрация с вводом зарегестрированного email
        def test_registrtion_witout_loyal_no_valid(self, driver):
            page = Registration(driver, "https://namelazz.com/")
            generator = Generator
            page.open()
            time.sleep(3)
            page.close_modal_window()
            page.log_in()
            page.click_go_to_registration()
            time.sleep(4)
            page.fill_registration_fields(generator.last_name, generator.first_name, "admin@namelazz.com",
                                          generator.date_of_birth, "Test1Test1")
            page.button_create_account()
            time.sleep(5)
            text_error_mail = page.text_error_mail()
            assert text_error_mail == 'Пользователь с такой почтой уже существует',\
                f"Текст ошибки {text_error_mail} не свопадает с 'Пользователь с такой почтой уже существует'"
