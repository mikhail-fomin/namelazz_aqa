from pages.main_page import MainPage,Authorization, Registration, SmokeTest
import time
from data.generator import Generator

"""Авторизация"""
class TestAuthorization:
    # ввод валидных данных для авторизации
    def test_auth_valid_data(self, driver):
        page = Authorization(driver, "https://namelazz.com/")
        page.open()
        time.sleep(3)
        page.close_modal_window()
        page.log_in()
        page.fill_auth_fields_valid("admin@namelazz.com", "wSTaR9b5mcPuVZaJ")
        time.sleep(5)
        page.log_in_whan_auth()
        greeting = page.check_greeting()
        assert greeting == "ПРИВЕТ, АННА!", f"Приветствие в ЛК {greeting} не совпадает с 'ПРИВЕТ, АННА!'"


    # ввод не валидного email
    def test_auth_no_valid_email(self, driver):
        page = Authorization(driver, "https://namelazz.com/")
        generator = Generator
        page.open()
        time.sleep(3)
        page.close_modal_window()
        page.log_in()
        page.fill_auth_fields_valid(generator.password,"wSTaR9b5mcPuVZaJ")
        time.sleep(5)
        text_error = page.text_error_auth()
        assert text_error == "Пожалуйста, введите правильные E-mail и пароль. Оба поля могут быть чувствительны к регистру.", \
            f'Нет текста ошибки авторизации или текст ошибки {text_error} не совпадает '


    # ввод не валидного пароля
    def test_auth_no_valid_password(self, driver):
        page = Authorization(driver, "https://namelazz.com/")
        generator = Generator
        page.open()
        time.sleep(3)
        page.close_modal_window()
        page.log_in()
        page.fill_auth_fields_valid("admin@namelazz.com", generator.password)
        time.sleep(5)
        text_error = page.text_error_auth()
        assert text_error == "Пожалуйста, введите правильные E-mail и пароль. Оба поля могут быть чувствительны к регистру.", \
            f'Нет текста ошибки авторизации или текст ошибки {text_error} не совпадает '


    # переход с авторизации по ссылке на политику персональных данных
    def test_auth_go_to_page_policy(self, driver):
        page = Authorization(driver, "https://namelazz.com/")
        page.open()
        time.sleep(3)
        page.close_modal_window()
        page.log_in()
        page.click_policy()
        page_policy = page.page_policy()
        assert page_policy == "ПОЛИТИКА В ОТНОШЕНИИ ОБРАБОТКИ ПЕРСОНАЛЬНЫХ ДАННЫХ", f"Текст {page_policy} не совпадает с " \
                                                                                    f"'ПОЛИТИКА В ОТНОШЕНИИ ОБРАБОТКИ ПЕРСОНАЛЬНЫХ ДАННЫХ'"

    # ОШИБКА С локатором, текст не возвращается
    def test_forgot_password(self, driver):
        page = Authorization(driver, "https://namelazz.com/")
        page.open()
        time.sleep(3)
        page.close_modal_window()
        page.log_in()
        page.click_forgot_password()
        page.restore_password("admin@namelazz.com")
        time.sleep(5)
        text_password_recovery = page.text_restore
        assert text_password_recovery == "E-mail с восстановлением отправлен", f"Текст {text_password_recovery} не совпадает с 'E-mail с восстановлением отправлен'"
        time.sleep(5)

    # Ввести email не зарегестрированного пользователя
    def test_forgot_password_no_valid_email(self, driver):
        page = Authorization(driver, "https://namelazz.com/")
        page.open()
        time.sleep(3)
        page.close_modal_window()
        page.log_in()
        page.click_forgot_password()
        page.restore_password("test1@test.com")
        restore_error_text = page.restore_error_text()
        assert restore_error_text == "Данный e-mail не зарегистрирован", f"Текст ошибки{restore_error_text} не совпадает с 'Данный e-mail не зарегистрирован'"
