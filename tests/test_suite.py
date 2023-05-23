import time
import string
import pytest

from pages.main_page import MainPage,Authorization, Registration, SmokeTest
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from data import data
from random import randint, randrange
class TestElements:

    """Smoke test"""
    class TestSmoke:

        # Смоук тест без авторизации
        def test_smoke_test_without_auth(self,driver):
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
            assert radiobutton_delivety_cost == delivery_cost_in_information_about_order,f"Выбранная стоимость доставки" \
                                                                                         f"{radiobutton_delivety_cost} " \
                                                                                         f"отличается от указанной в информации о товаре {delivery_cost_in_information_about_order}"
            price_product = page.information_about_order()
            delivery = page.delivery_cost_in_information_about_order().replace("RUB","")
            total_sum_math = str(int(price_product) + int(delivery))
            total_sum = page.total_sum()
            assert total_sum == total_sum_math, f"Итоговая сумма {total_sum} отличается от посчитанной суммы {total_sum_math}"
            page.button_submit()
            ykassa = page.total_ykassa().replace("₽","")
            assert total_sum == ykassa,f"Общая стоимость на Юкасса{ykassa} отличается от итого к оплате на странице инф." \
                                       f" о товаре {total_sum}"




        # Смоук тест c авторизацией
        def test_smoke_test_with_auth(self,driver):
            page = SmokeTest(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.log_in()
            page.fill_auth_fields_valid("admin@namelazz.com", "wSTaR9b5mcPuVZaJ")
            time.sleep(5)
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
            assert radiobutton_delivety_cost == delivery_cost_in_information_about_order,\
                f"Выбранная стоимость доставки" \
                f"{radiobutton_delivety_cost} отличается от указанной в информации о товаре {delivery_cost_in_information_about_order}"
            price_product = page.information_about_order()
            delivery = page.delivery_cost_in_information_about_order().replace("RUB","")
            total_sum_math = str(int(price_product) + int(delivery))
            total_sum = page.total_sum()
            assert total_sum == total_sum_math, f"Итоговая сумма {total_sum} отличается от посчитанной суммы {total_sum_math}"
            page.button_submit()
            ykassa = page.total_ykassa().replace("₽","")
            assert total_sum == ykassa,f"Общая стоимость на Юкасса{ykassa} " \
                                       f"отличается от итого к оплате на странице инф. о товаре {total_sum}"



    """Main Page"""
    class TestMainPage:

        # подписка на новости
        def test_subscription(self, driver):
            page = MainPage(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.subscription("banihe9531@jwsuns.com")
            subscription = page.text_subscription()
            assert subscription == 'СПАСИБО ЗА ПОДПИСКУ! ПОДТВЕРЖДЕНИЕ ОТПРАВЛЕНО ВАМ НА ПОЧТУ.',\
                f"Текст {subscription} не совпадает с 'СПАСИБО ЗА ПОДПИСКУ! ПОДТВЕРЖДЕНИЕ ОТПРАВЛЕНО ВАМ НА ПОЧТУ'"



        # выбор города
        def test_choose_city(self,driver):
            page = MainPage(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            city = data.city[randint(1, 19)]
            page.choose_city(city)
            time.sleep(5)
            header_city = page.text_city()
            assert city == header_city, f"Выбранный город {city} отличсется от города в хедере {header_city}"


        # переключение между каталогами
        def test_catalog_choose_and_back(self, driver):
            page = SmokeTest(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.burger_click()
            page.catalog_click_back()


        # Добавление и удаление из корзины
        def test_smoke_test_without_auth(self,driver):
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
            page.delete_from_basket()
            text_empty_basket = page.text_empty_basket().upper()
            assert text_empty_basket == "ВАША КОРЗИНА ПУСТА", f"Корзина не пуста, текст {text_empty_basket}" \
                                                              f" не соответствует 'Ваша корзина пуста'"




        # добавление в корзину нескольких товаров и проверка общей суммы
        def test_add_few_products_to_basket(self, driver):
            page = SmokeTest(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.burger_menu()
            sum_price_poducts = page.add_few_products_to_basket2()
            time.sleep(3)
            sum_price_basket = page.basket_sum()
            assert sum_price_poducts == sum_price_basket,f"Сумма добавленных товаров {sum_price_poducts} " \
                                                         f"не равна сумме в корзине {sum_price_basket}"

        """Избранное"""
        # добавление одного товара в избранное и проверка, что кол-во в избранном соответствует кол-ву добавленных товаров в избранное
        def test_add_favorites(self, driver):
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.log_in()
            page.fill_auth_fields_valid("admin@namelazz.com", "wSTaR9b5mcPuVZaJ")
            time.sleep(5)
            page.burger_menu()
            page.catalog_add_favourites()
            time.sleep(3)
            page.favorites()



        # удаление из избранного, на странице избранное
        def test_delete_from_favorites(self,driver):
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.log_in()
            page.fill_auth_fields_valid("admin@namelazz.com", "wSTaR9b5mcPuVZaJ")
            time.sleep(5)
            page.burger_menu()
            page.catalog_add_favourites()
            time.sleep(3)
            page.favorites()
            page.delete_from_favorites()



        # удаление из избранного, на странице карточки товара.
        def test_delete_from_favorites_on_card(self,driver):
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.log_in()
            page.fill_auth_fields_valid("admin@namelazz.com", "wSTaR9b5mcPuVZaJ")
            time.sleep(5)
            page.burger_menu()
            page.catalog_add_favourites()
            time.sleep(3)
            page.favorites()
            page.delete_from_favorites_on_card()


        # добавленеие в избранное 20 карточек и проверка, что при скролле карточки не удваиваются
        def test_scroll_favorites(self, driver):
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.log_in()
            page.fill_auth_fields_valid("admin@namelazz.com", "wSTaR9b5mcPuVZaJ")
            time.sleep(5)
            page.burger_menu()
            page.catalog_add_favourites_20_products()


        # добавленеие в избранное и переход на страницу избранное через сайдбар, проверка соответствия добавленных карточке и в избранном
        def test_favorites_sidebar(self, driver):
            page = Authorization(driver, "https://namelazz.com/")
            page.open()
            page.button_yes_choose_city()
            time.sleep(5)
            page.close_modal_cookie()
            page.log_in()
            page.fill_auth_fields_valid("admin@namelazz.com", "wSTaR9b5mcPuVZaJ")
            time.sleep(5)
            page.burger_menu()
            products_sum_in_catalog = page.catalog_add_favourites()
            products_sum_in_favorite = page.choose_favorite_in_sidebar()
            assert products_sum_in_catalog == products_sum_in_favorite, f"Кол-во добавленных карточек {products_sum_in_catalog}" \
                                                                        f"не равно кол-во в избранном {products_sum_in_favorite}"





