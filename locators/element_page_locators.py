from selenium.webdriver.common.by import By


class MainPageLocators:

        """MainPage"""
        CLOSE_MODAL = (By.CSS_SELECTOR, '[class="modal-welcome__close  modal_close  close-btn"]')#закрытие модального окна
        BUTTON_YES_CITY = (By.XPATH,'/html/body/header/div/div[3]/div/div/div[1]/div[2]/div[2]/a[1]')#подтвердить город
        CLOSE_MODAL_COOKIE = (By.CSS_SELECTOR,'[class="n-cookie-modal__close"]')#закрытие модального окна куки
        BUTTON_LOG_IN = (By.CSS_SELECTOR,'button[class="header__icons-item  header__icons-auth  auth_open"]')# кнопка войти, юзер не авторизован
        BUTTON_LOG_IN_WHEN_AUTH_USER = (By.CSS_SELECTOR,'[class="header__icons-item  header__icons-auth"]')# кнопка войти, юзер авторизован
        BUTTON_BURGER = (By.CSS_SELECTOR, "[class='header__btn  menu-btn-open']")# кнопка бургер меню
        BUTTON_BASKET = (By.CSS_SELECTOR,'[id="ajaxCart2"]>svg')# кнопка корзина
        FAVORITES = (By.CSS_SELECTOR, '[class="header__icons-item  header__icons-fav  d-none  d-lg-inline"]>svg')  # кнопка избранное
        SUBSCRIPTION = (By.ID,"sbscr")# поле подписаться на новости
        TEXT_SUBSCRIPTION = (By.CSS_SELECTOR,'[class="container-fluid"]>h1')# текст успешной подписки на новости
        CHOOSE_CITY = (By.CSS_SELECTOR,'[class="d-none  d-lg-inline"]>[class="select-city"]')# выбор города
        FIELD_INPUT_CITY = (By.CSS_SELECTOR,'[class="select-city__cities fancybox-content"]>[class="select-city__cities-input suggestions-input"]')# поле ввести город
        TEXT_SELECT_CITY = (By.CSS_SELECTOR,'[class="d-none  d-lg-inline"]>[class="select-city"]>[class="select-city__wrapper"]>a')# выбранный город в хедере
        DELETE_FROM_FAVORITES = (By.CSS_SELECTOR,'[class="like-good-favorites"]')# кнопка удалить из избранного
        FOOTER = (By.CSS_SELECTOR,'[class="footer__bottom"]')# футер страницы


        """Sidebar"""
        CATALOG_ELEMENTS = (By.CSS_SELECTOR,'[class="burger__wrapper"]>ul[class="burger__menu"]>li[class="burger__menu-item"]>[class="burger__menu-link"]')  # список категорий в сайдбаре
        FAVORITES_SIDEBAR = (By.CSS_SELECTOR, '[class="burger__menu  burger__menu_last"]>li:nth-child(1)>a')  # кнопка избранное в сайдбаре
        BUTTON_CLOTHES = (By.CSS_SELECTOR,'div.burger__wrapper > ul.burger__menu:nth-of-type(1) > li:nth-of-type(6)>[class="burger__menu-link  submenu-open"]')  # Одежда и аксесуары
        LIST_CATEGORIES_LOOK_ALL = (By.CSS_SELECTOR, '[class="burger__submenu"]>[class="burger__menu"]>li>a:nth-child(1)')  # посмотреть всё в сайдбаре в разделе одежда и аксуссуары
        BUTTON_LOOK_ALL = (By.CSS_SELECTOR, 'div.burger__submenu:nth-of-type(1)>ul.burger__menu:nth-of-type(1)>li:nth-of-type(2)>[class="burger__menu-link"]:nth-of-type(1)')#Смотреть всё
        LIST_CATEGORIES_PRODUCTS = (By.CSS_SELECTOR, '[class="catalog__list-box"]>[id="category-list"]>li>a')  # список категорий товара


        """Authorization"""
        EMAIL_FIELD = (By.ID,'id_username')#поле email
        PASSWORD_FIELD = (By.ID,'id_password')#поле пароль
        BUTTON_SIGN_IN = (By.CSS_SELECTOR, '[class*="modal-login__btn  btn  btn-login"]')#кнопка войти
        TEXT_ERROR_AUTH = (By.CSS_SELECTOR,'[class="errorlist nonfield"]')#текст ошибки авторизации
        LINK_GO_TO_POLICY = (By.CSS_SELECTOR,'[class="modal-login__btn-box"]>[class="modal-login__policy  policy_links"]>[class="modal-login__policy-link"]')#ссылка переход на страницу политика и конфиденциальность
        PAGE_POLICY = (By.CSS_SELECTOR,'[class="page__title"]')#текст заголовка на странице политика и конфиденциальность
        BUTTON_FORGOT_PASSWORD = (By.CSS_SELECTOR,'[class="modal-login__link-recover"]')#кнопка забыли пароль
        FIELD_EMAIL_RESTORE_PASSWORD = (By.CSS_SELECTOR,'[class="modal-login__col  modal-login__col_recover active"]>[class="custom_form-group last-group"]>[class="custom_input"]')
        BUTTON_RESTORE = (By.CSS_SELECTOR, '[class="modal-login__btn  btn"]')
        TEXT_PASSWORD_RECOVERY = (By.ID,'[class="modal-login__col  modal-login__col_recover active"]')
        TEXT_ERROR_PASSWORD_RECOVERY = (By.CSS_SELECTOR,'[id="id-error-recover-password"]')

        """Registration"""
        BUTTON_GO_TO_REGISTRATION = (By.CSS_SELECTOR, '[class="modal-login__link-box"]')# кнопка регистрация
        FIRST_NAME_FIELD = (By.ID, "first_name")# поле имя
        LAST_NAME_FIELD = (By.ID, 'last_name_sign')# поле фамилия
        EMAIL_REGISTRATION_FIELD = (By.CSS_SELECTOR, '[id="email"][class="custom_input"]')# поле email
        DATE_OF_BIRTH = (By.ID, "birthday_sign")# поле дня рождения
        PASSWORD_REGISTRATION_FIELD1 = (By.ID, "password1")# поле пароль
        PASSWORD_REGISTRATION_FIELD2 = (By.ID, "password2")# поле повторить пароль
        CHECKBOX_SIG_IN_LOYALTY = (By.ID,"is_sign_loyalty") #чекбокс лояльность
        ENTER_NUMBER = (By.ID,"loyalty-phone")#поле номера для лояльности
        BUTTON_CONFIRM_LOYALTY = (By.ID, "loyalty-phone-confirm")#кнопка подтверждения лояльности
        BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR,'[class="modal-login__btn  btn  btn-registration"]')#кнопка создать аккаунт
        TEXT_ERROR_MAIL = (By.CSS_SELECTOR,'[class="error error-messages-registration message-top"]')#текст ошибки пользователь с такой ошибкой существует
        TEXT_SUCCESSFUL_REGISTRATION = (By.CSS_SELECTOR,'[class="modal-login__col active"]>[method="post"]')# текст успешной регистрации


        """Personal Profile"""
        GET_GREETING = (By.CSS_SELECTOR,'[class="profile__name"]')#получить текст приветствия в профиле

        """Catalog page"""
        CARD_PRODUCT = (By.CSS_SELECTOR, '[class="like-good-img1 img-height-box"]')  #карточка товара
        NAME_PRODUCT_CATALOG = (By.CSS_SELECTOR, '[class="like-good-name"]>a')#название продукта на странице каталога
        NAME_PAGE_CATEGORIY = (By.CSS_SELECTOR,'h1[class="catalog__title"]')# название страницы категории
        NAME_CATEGORY_SIDEBAR = (By.CSS_SELECTOR,'a[class="catalog__item-link"]')# название категории в сайдбаре
        PRICE_PRODUCT_CATALOG = (By.CSS_SELECTOR, '[class="like-good-price"]')# цена товара на странице каталога
        OLD_PRICE_CATALOG = (By.CSS_SELECTOR, '[class="like-good-old_price"]')  # старая цена в каталоге
        PRICE_OLD_AND_NEW = (By.CSS_SELECTOR, '[class="d-flex"]')  # цена старая и новая

        """Filter and sorting"""
        BUTTON_SOTRING = (By.CSS_SELECTOR, '[class="filter__title  filter_open"]')  # нажатие на селект сортировки
        SORTING_DESCENDING = (By.CSS_SELECTOR,'[class="filter__sort"]:nth-child(1)') # сортировка по убыванию
        SORTING_ASCENDING = (By.CSS_SELECTOR, '[class="filter__sort"]:nth-child(2)') # сортировка по возрастанию
        FILTER_PRICE = (By.CSS_SELECTOR, '[id="mse2_ms|price"]') # фильтрация по цене
        FILTER_PRICE_MIN_COST = (By.CSS_SELECTOR, '[id="min_cost"]') # поле фильтрация по цене минимальное значение
        FILTER_SIZE = (By.CSS_SELECTOR, '[id="mse2_excludesize|size"]') # фильтр по размеру
        CHECKBOX_FILTER_SIZE = (By.CSS_SELECTOR, '[class="filter__label"]') # чекбокс фильтра по размеру
        BUTTON_RESET = (By.CSS_SELECTOR, '[value="Сбросить"]')  # кнопка сбросить в фильтре


        """Product page"""
        CHOOSE_SIZE = (By.CSS_SELECTOR, '[class="size-item "]')  # выбрать размер
        BUTTON_ADD_BASKET = (By.CSS_SELECTOR, '[class="n-product__add-button add"]') #кнопка добавить в корзину
        ADD_FAVORITES = (By.CSS_SELECTOR,'[class="n-product__fixed-add"]>[class="d-none  d-lg-flex  n-product__add-favorites msfavorites "]>[fill="none"]>[fill-rule="evenodd"]')  # кнопка добавить в избранное
        ACTIVE_BUTTON_ADD_FAVORITES = (By.CSS_SELECTOR,'[class="d-none  d-lg-flex  n-product__add-favorites msfavorites load voted "]>svg')  # активная кнопка добавить в избранное
        NAME_PRODUCT = (By.CSS_SELECTOR,'[class="n-product__title"]')#получаем текс название товара
        PRICE_PRODUCT = (By.CSS_SELECTOR,'[class="n-product__price"]')#получаем текст цена товара
        ACTIVE_SIZE = (By.XPATH,"//div[contains(@class, 'size-item') and contains(@class, 'active')]/label") #получаем текст активного размера
        ACTIVE_COLOR = (By.XPATH,"//div[contains(@class, 'n-product__color-item') and contains(@class, 'active')]/div")#получаем цвет товара


        """Basket page"""
        NAME_PRODUCT_BASKET = (By.CSS_SELECTOR, '[class="cart-details-col"]>a')#[class="cart_title"]  # получаем текст название товара в корзине
        PRICE_PRODUCT_BASKET = (By.CSS_SELECTOR, '[class="cart_price"]') #получаем текс цена товара в корзине
        SIZE_PRODUCT_BASKET = (By.CSS_SELECTOR,'[class="cart_option"]:nth-of-type(2)')#получаем текст размера товара в корзине
        COLOR_PRODUCT_BASKET = (By.XPATH,"//div[contains(@class, 'cart_option')]/div/div[contains(@title, '')]")#получаем текст цвета товара в корзине
        SUM_PRICE_BASKET = (By.CSS_SELECTOR,'[class="ms2_total_cost"]')#получаем текст стоимости товаров ИТОГО
        BUTTON_CHECKOUT = (By.CSS_SELECTOR,'[class="ajax-cart-buttons"]>[class="btn"]')#Кнопка оформить заказ
        BUTTON_DELETE_PRODUCT_FROM_BASKET = (By.CSS_SELECTOR,'[class="cart_cancel"]>div')#кнопка удалить из корзины товар
        TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, '[class="empty_cart-title"]')#текст пустой корзины


        """Checkout page"""
        NAME_PRODUCT_CHECKOUT = (By.CSS_SELECTOR,'[class="cart_title"]')#получаем текст название продукта на странице оформления заказа
        PRICE_PRODUCT_CHECKOUT = (By.CSS_SELECTOR,'[class="cart_price"]')#получаем текст цены продукта на странице оформления заказа
        COLOR_PRODUCT_CHECHOUT = (By.XPATH,'//div[contains (@class, "cart_option")]/div/div[contains(@title,"")]')#получаем текст цвет продукта на странице оформления заказа
        SIZE_PRODUCT_CHECHOUT = (By.CSS_SELECTOR,'[class="cart_option"]:nth-of-type(2)')#получаем текст размер продукта на странице оформления заказа

        # Поля для заполнения данных адреса
        COUNTRY = (By.ID,"country")
        CITY = (By.ID,"city")
        INDEX = (By.ID,"postal_code")
        STREET = (By.ID,"street")
        HOUSE = (By.ID,"building")
        APARTMENT = (By.ID,"room")

        # Поля для заполнения данных пользователя
        NAME_ORDER = (By.ID,"receiver")
        FIRST_NAME_ORDER = (By.ID,"surname")
        EMAIL_ORDER = (By.ID,"email_order")
        NUMBER_ORDER = (By.ID,"phone_order")
        COMMENT_ORDER = (By.ID,"comment")

        # Радиобаттон доставка
        RADIOBUTTON_ORDER = (By.CSS_SELECTOR,'[id="cdekCoruier"]>[class="delivery input-parent courier"]>[class="radio"]')
        RADIOBUTTON_DELIVERY_COST = (By.CSS_SELECTOR,'[id="cdekCoruier"]>[class="delivery input-parent courier"]>[class="delivery-details"]>[class="delivery_cost"]')

        # Информация о заказе
        COST_OF_GOODS = (By.CSS_SELECTOR,'[class="real_total_cost"]')#стоимость товара
        DISCOUNT = (By.CSS_SELECTOR,'[class="ms2_promocode_discount"]')#стоимость доставки
        DELIVERY = (By.CSS_SELECTOR, '[class="ms2_delivery_cost"]') #стоимость с RUB
        TOTAL_PAYABLE = (By.CSS_SELECTOR,'[id="ms2_order_cost"]')#стоимость c RUB
        TOTAL_SUM = (By.CSS_SELECTOR, '[id="ms2_order_cost"]')#итого к оплате
        BUTTON_ORDER_SUBMIT = (By.ID,"order_submit")#кнопка сделать заказ

        # Страница платёжной системы
        TOTAL_SUM_Y_KASSA = (By.CSS_SELECTOR,'[class="Text__StyledTextSpan-sc-9bqqn7-0 bKjqYI Price__StyledText-sc-ymfuk6-0 jiVPLn"]>span')#стоимость товара на странице юкассы