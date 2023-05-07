from selenium.webdriver.common.by import By


class MainPageLocators:

        """MainPage"""
        CLOSE_MODAL = (By.CSS_SELECTOR, '[class="modal-welcome__close  modal_close  close-btn"]')
        BUTTON_YES_CITY = (By.XPATH,'/html/body/header/div/div[3]/div/div/div[1]/div[2]/div[2]/a[1]')#Подтвердить город
        CLOSE_MODAL_COOKIE = (By.CSS_SELECTOR,'[class="n-cookie-modal__close"]')

        BUTTON_LOG_IN = (By.CSS_SELECTOR,'button[class="header__icons-item  header__icons-auth  auth_open"]')#не авторизован
        BUTTON_LOG_IN_WHEN_AUTH_USER = (By.CSS_SELECTOR,'[class="header__icons-item  header__icons-auth"]')#авторизован
        BUTTON_BURGER = (By.CSS_SELECTOR, "[class='header__btn  menu-btn-open']")
        BUTTON_CLOTHES = (By.CSS_SELECTOR, 'div.burger__wrapper > ul.burger__menu:nth-of-type(1) > li:nth-of-type(5)>[class="burger__menu-link  submenu-open"]')
        BUTTON_LOOK_ALL = (By.CSS_SELECTOR, 'div.burger__submenu:nth-of-type(1)>ul.burger__menu:nth-of-type(1)>li:nth-of-type(2)>[class="burger__menu-link"]:nth-of-type(1)')


        """Authorization"""
        EMAIL_FIELD = (By.ID,'id_username')
        PASSWORD_FIELD = (By.ID,'id_password')
        BUTTON_SIGN_IN = (By.CSS_SELECTOR, '[class*="modal-login__btn  btn  btn-login"]')
        TEXT_ERROR_AUTH = (By.CSS_SELECTOR,'[class="errorlist nonfield"]')

        """Registration"""
        BUTTON_GO_TO_REGISTRATION = (By.CSS_SELECTOR, '[class="modal-login__link-box"]')
        FIRST_NAME_FIELD = (By.ID, "first_name")
        LAST_NAME_FIELD = (By.ID, 'last_name_sign')
        EMAIL_REGISTRATION_FIELD = (By.CSS_SELECTOR, '[id="email"][class="custom_input"]')
        DATE_OF_BIRTH = (By.ID, "birthday_sign")
        PASSWORD_REGISTRATION_FIELD1 = (By.ID, "password1")
        PASSWORD_REGISTRATION_FIELD2 = (By.ID, "password2")
        CHECKBOX_SIG_IN_LOYALTY = (By.ID,"is_sign_loyalty") #чекбокс лояльность
        ENTER_NUMBER = (By.ID,"loyalty-phone")#поле номера для лояльности
        BUTTON_CONFIRM_LOYALTY = (By.ID, "loyalty-phone-confirm")#кнопка подтвержденя лояльности
        BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR,'[class="modal-login__btn  btn  btn-registration"]')


        """Personal Profile"""
        GET_GREETING = (By.CSS_SELECTOR,'[class="profile__name"]')#получить текст приветствия в профиле

        """Catalog page"""
        CARD_PRODUCT = (By.CSS_SELECTOR, '[class="like-good-img1 img-height-box"]')  #карточка товара


        """Product page"""
        CHOOSE_SIZE = (By.CSS_SELECTOR, '[class="size-item "]')  # выбрать размер
        BUTTON_ADD_BASKET = (By.CSS_SELECTOR, '[class="n-product__add-button add"]')

        NAME_PRODUCT = (By.CSS_SELECTOR,'[class="n-product__title"]')#получаем текс название товара
        PRICE_PRODUCT = (By.CSS_SELECTOR,'[class="n-product__price"]')#получаем текст цена товара
        ACTIVE_SIZE = (By.XPATH,"//div[contains(@class, 'size-item') and contains(@class, 'active')]/label") #получаем текст
        ACTIVE_COLOR = (By.XPATH,"//div[contains(@class, 'n-product__color-item') and contains(@class, 'active')]/div")#получаем цвет товара


        """Basket page"""
        NAME_PRODUCT_BASKET = (By.CSS_SELECTOR, '[class="cart_title"]')  # получаем текст название товара в корзине
        PRICE_PRODUCT_BASKET = (By.CSS_SELECTOR, '[class="cart_price"]') #получаем текс цена товара в корзине
        SIZE_PRODUCT_BASKET = (By.CSS_SELECTOR,'[class="cart_option"]:nth-of-type(2)')#получаем текст размера товара в корзине
        COLOR_PRODUCT_BASKET = (By.XPATH,"//div[contains(@class, 'cart_option')]/div/div[contains(@title, '')]")#получаем текст цвета товара в корзине
        BUTTON_CHECKOUT =  (By.CSS_SELECTOR,'[class="ajax-cart-buttons"]>[class="btn"]')#Кнопка оформить заказ

        """Checkout page"""
        NAME_PRODUCT_CHECKOUT = (By.CSS_SELECTOR,'[class="cart_title"]')#получаем текст название продукта на странице оформления заказа
        PRICE_PRODUCT_CHECKOUT = (By.CSS_SELECTOR,'[class="cart_price"]')#получаем текст цены продукта на странице оформления заказа
        COLOR_PRODUCT_CHECHOUT = (By.XPATH,'//div[contains (@class, "cart_option")]/div/div[contains(@title,"")]')#получаем текст цвет продукта на странице оформления заказа
        SIZE_PRODUCT_CHECHOUT = (By.CSS_SELECTOR,'[class="cart_option"]:nth-of-type(2)')#получаем текст размер продукта на странице оформления заказа

        #Filling date
        #Данные адреса
        COUNTRY = (By.ID,"country")
        CITY = (By.ID,"city")
        INDEX = (By.ID,"postal_code")
        STREET = (By.ID,"street")
        HOUSE = (By.ID,"building")
        APARTMENT = (By.ID,"room")

        #Данные получателя
        NAME_ORDER = (By.ID,"receiver")
        FIRST_NAME_ORDER = (By.ID,"surname")
        EMAIL_ORDER = (By.ID,"email_order")
        NUMBER_ORDER = (By.ID,"phone_order")
        COMMENT_ORDER = (By.ID,"comment")

        #Радиобаттон доставка
        RADIOBUTTON_ORDER = (By.CSS_SELECTOR,'[id="cdekCoruier"]>[class="delivery input-parent courier"]>[class="radio"]')
        RADIOBUTTON_DELIVERY_COST = (By.CSS_SELECTOR,'[id="cdekCoruier"]>[class="delivery input-parent courier"]>[class="delivery-details"]>[class="delivery_cost"]')

        #Информация о заказе
        COST_OF_GOODS = (By.CSS_SELECTOR,'[class="real_total_cost"]')
        DISCOUNT = (By.CSS_SELECTOR,'[class="ms2_promocode_discount"]')
        DELIVERY = (By.CSS_SELECTOR, '[class="ms2_delivery_cost"]') #стоимость с RUB
        TOTAL_PAYABLE = (By.CSS_SELECTOR,'[id="ms2_order_cost"]')#стоимость c RUB