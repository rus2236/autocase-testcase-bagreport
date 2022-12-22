from config import TestData
from pages.auth_page import AuthPage
from pages.locators import AuthLocators, PassRecoveryLocators, RegistrationLocators


# Тест №1
def test_auth_page_current(init_driver):
    """Корректное отображение страницы с формой Авторизация"""
    authpage = AuthPage(init_driver)
    assert authpage.get_url() == TestData.START_URL
    assert authpage.get_element_text(AuthLocators.phone_tab) == "Номер"
    assert authpage.get_element_text(AuthLocators.mail_tab) == "Логин"
    assert authpage.get_element_text(AuthLocators.login_tab) == "Почта"
    assert authpage.get_element_text(AuthLocators.ls_tab) == "Лицевой счёт"
    assert authpage.element_are_present(AuthLocators.auth)
    assert authpage.element_are_present(AuthLocators.lk_logo)
    assert authpage.element_are_present(AuthLocators.name_field)
    assert authpage.element_are_present(AuthLocators.password_field)

# Тест №2
def test_registration_page_current(init_driver):
    """Корректное отображение страницы с формой Регистрация"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.registration)
    assert authpage.element_are_present(RegistrationLocators.reg)
    assert authpage.element_are_present(RegistrationLocators.first_name_field)
    assert authpage.element_are_present(RegistrationLocators.last_name_field)
    assert authpage.element_are_present(RegistrationLocators.region_field)
    assert authpage.element_are_present(RegistrationLocators.address_field)
    assert authpage.element_are_present(RegistrationLocators.password_reg_field)
    assert authpage.element_are_present(RegistrationLocators.password_confirm_field)
    assert authpage.get_element_text(RegistrationLocators.btn_reg) == "Продолжить"
    assert TestData.REGISTER_URL in authpage.get_url()

# Тест №3
def test_password_recovery_page_current(init_driver):
    """Корректное отображение страницы с формой Восстановление пароля"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.forgot_password)
    assert authpage.element_are_present(PassRecoveryLocators.pass_recovery)
    assert authpage.get_element_text(PassRecoveryLocators.phone_tab) == "Номер"
    assert authpage.get_element_text(PassRecoveryLocators.mail_tab) == "Логин"
    assert authpage.get_element_text(PassRecoveryLocators.login_tab) == "Почта"
    assert authpage.get_element_text(PassRecoveryLocators.ls_tab) == "Лицевой счёт"
    assert authpage.element_are_present(PassRecoveryLocators.captcha)
    assert authpage.get_element_text(PassRecoveryLocators.btn_continue) == "Далее"
    assert authpage.element_are_present(PassRecoveryLocators.back)
    assert TestData.PASS_RECOVERY_URL in authpage.get_url()

# Тест №4
def test_change_tab_from_phone_to_email(init_driver):
    """Автоматическая смена таба аунтентификации с телефона на почту на странице формы авторизации"""
    authpage = AuthPage(init_driver)
    authpage.hover_cursor_click(AuthLocators.name_field)
    authpage.enter_word(AuthLocators.name_field, "qwe123@yandex.ru")
    authpage.click_element(AuthLocators.password_field)
    value = authpage.get_attribute_value(AuthLocators.tab_value, 'value')
    assert value == 'mail'

# Тест №5
def test_change_tab_from_phone_to_login(init_driver):
    """Автоматическая смена таба аунтентификации с телефона на логин на странице формы авторизации"""
    authpage = AuthPage(init_driver)
    authpage.hover_cursor_click(AuthLocators.name_field)
    authpage.enter_word(AuthLocators.name_field, "qwe123")
    authpage.click_element(AuthLocators.password_field)
    value = authpage.get_attribute_value(AuthLocators.tab_value, 'value')
    assert value == 'login'

# Тест №6
def test_change_tab_from_mail_to_phone(init_driver):
    """Автоматическая смена таба аунтентификации с почты на телефон на странице формы авторизации"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.mail_tab)
    authpage.hover_cursor_click(AuthLocators.name_field)
    authpage.enter_word(AuthLocators.name_field, "9876543210")
    authpage.click_element(AuthLocators.password_field)
    value = authpage.get_attribute_value(AuthLocators.tab_value, 'value')
    assert value == 'phone'

# Тест №7
def test_change_tab_from_mail_to_login(init_driver):
    """Автоматическая смена таба аунтентификации с почты на логин на странице формы авторизации"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.mail_tab)
    authpage.hover_cursor_click(AuthLocators.name_field)
    authpage.enter_word(AuthLocators.name_field, "qwe123")
    authpage.click_element(AuthLocators.password_field)
    value = authpage.get_attribute_value(AuthLocators.tab_value, 'value')
    assert value == 'login'

# Тест №8
def test_change_tab_from_ls_to_mail(init_driver):
    """Автоматическая смена таба аунтентификации с лицевого счета на почту на странице формы авторизации"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.ls_tab)
    authpage.hover_cursor_click(AuthLocators.name_field)
    authpage.enter_word(AuthLocators.name_field, "qwe123@yandex.ru")
    authpage.click_element(AuthLocators.password_field)
    value = authpage.get_attribute_value(AuthLocators.tab_value, 'value')
    assert value == 'mail'

# Тест №9
def test_change_tab_from_ls_to_login(init_driver):
    """Автоматическая смена таба аунтентификации с лицевого счета на логин на странице формы авторизации"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.ls_tab)
    authpage.hover_cursor_click(AuthLocators.name_field)
    authpage.enter_word(AuthLocators.name_field, "qwe123")
    authpage.click_element(AuthLocators.password_field)
    value = authpage.get_attribute_value(AuthLocators.tab_value, 'value')
    assert value == 'login'

# Тест №10
def test_error_message_with_empty_phone_field(init_driver):
    """Сообщение об ошибке при авторизации с пустым полем мобильный телефон"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.btn_login)
    assert authpage.element_are_present(AuthLocators.error_phone)

# Тест №11
def test_error_message_with_empty_email_field(init_driver):
    """Соощение об ошибке при авторизации с пустым полем электронная почта"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.mail_tab)
    authpage.click_element(AuthLocators.btn_login)
    assert authpage.element_are_present(AuthLocators.error_mail)

# Тест №12
def test_error_message_with_empty_login_field(init_driver):
    """Сообщение об ошибке при авторизации с пустым полем логин"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.login_tab)
    authpage.click_element(AuthLocators.btn_login)
    assert authpage.element_are_present(AuthLocators.login_tab)

# Тест №13
def test_error_message_with_empty_ls_field(init_driver):
    """Сообщение об ошибке при авторизации с пустым полем лицевой счет"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.ls_tab)
    authpage.click_element(AuthLocators.btn_login)
    assert authpage.element_are_present(AuthLocators.ls_tab)

# Тест №14
def test_link_to_the_password_recovery_page(init_driver):
    """Ссылка на кнопке Забыл пароль на странице Авторизации переводит на страницу с формой Восстановления пароля"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.forgot_password)
    assert authpage.element_are_present(PassRecoveryLocators.pass_recovery)

# Тест №15
def test_reset_back(init_driver):
    """Ссылка на кнопке "Вернуться назад" на странице с формой Восстановление пароля возвращает на страницу Авторизации"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.forgot_password)
    authpage.click_element(PassRecoveryLocators.back)
    assert authpage.element_are_present(AuthLocators.auth)

# Тест №16
def test_link_to_registration_page(init_driver):
    """Ссылка на кнопке "Зарегистрироваться" на странице с формой Авторизация переводит на страницу с формой Регистрации"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.registration)
    assert authpage.element_are_present(RegistrationLocators.reg)

# Тест №17
def test_link_to_user_agreement(init_driver):
    """Ссылка на кнопке Пользовательское соглашение в подвале ведет на страницу с пользовательским соглашением"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.terms_of_use)
    init_driver.switch_to.window(init_driver.window_handles[-1])
    url_user_agreement = init_driver.current_url
    assert url_user_agreement == TestData.USER_AGREEMENT_URL

# Тест №18
def test_invalid_login_password(init_driver):
    """Сообщение об ошибке при авторизация несуществующего пользователя с помощью логина и пароля"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.login_tab)
    authpage.hover_cursor_click(AuthLocators.name_field)
    authpage.enter_word(AuthLocators.name_field, "asdf1234")
    authpage.hover_cursor_click(AuthLocators.password_field)
    authpage.enter_word(AuthLocators.password_field, "Qwer1234")
    authpage.click_element(AuthLocators.btn_login)
    assert authpage.element_are_present(AuthLocators.error_message)

# Тест №19
def test_support_window(init_driver):    # на данный момент всплывающее окно поддержки убрано
    """Всплывающее окно поддержки на странице с формой авторизации"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.customer_support)
    assert authpage.element_are_present(AuthLocators.name_support)
    assert authpage.element_are_present(AuthLocators.phone_support)

# Тест №20
def test_close_support_window(init_driver):   # на данный момент всплывающее окно поддержки убрано
    """Закрытие всплывающего окна поддержки на странице с формой авторизации"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.customer_support)
    authpage.hover_cursor_click(AuthLocators.close_customer_support)
    assert authpage.element_invisibility(AuthLocators.name_support)

# Тест №21
def test_visible_password(init_driver):
    """Видимые символы пароля в поле для ввода 'Пароль' на странице с формой авторизации"""
    authpage = AuthPage(init_driver)
    authpage.hover_cursor_click(AuthLocators.password_field)
    authpage.enter_word(AuthLocators.password_field, "Qwer1234")
    authpage.hover_cursor_click(AuthLocators.eye_icon)
    pass_input = authpage.element_find(AuthLocators.password_field)
    assert pass_input.get_attribute("value") == "Qwer1234"

# Тест №22
def test_authorization_mail(init_driver):
    """Авторизация пользователя через электронную почту"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.mail_tab)
    authpage.enter_word(AuthLocators.name_field, "test1234@yandex.ru")
    authpage.enter_word(AuthLocators.password_field, "Tester1234")
    authpage.click_element(AuthLocators.btn_login)
    assert authpage.element_are_present(AuthLocators.lk)

# Тест №23
def test_error_enter_1_character_firstname_on_registration_page(init_driver):
    """Сообщение об ошибке на странице формы Регистрации при вводе 1 буквы на кириллице в поле Имя """
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.registration)
    authpage.enter_word(RegistrationLocators.first_name_field, "ф")
    authpage.click_element(RegistrationLocators.address_field)
    assert authpage.element_are_present(RegistrationLocators.error_firts_name)

# Тест №24
def test_error_enter_31_character_lasttname_on_registration_page(init_driver):
    """Сообщение об ошибке на странице формы Регистрации при вводе 31 буквы на кириллице в поле Фамилия"""
    authpage = AuthPage(init_driver)
    authpage.click_element(AuthLocators.registration)
    authpage.enter_word(RegistrationLocators.last_name_field, "йцукенгшшщзхфывапаортолдчсмимтн")
    authpage.click_element(RegistrationLocators.address_field)
    assert authpage.element_are_present(RegistrationLocators.error_last_name)