class TestData:
    # АДРЕС ДРАЙВЕРА
    CHROME_DRIVER_PATH = 'chromedriver.exe'
    # URL авторизация "Ростелеком"
    START_URL = 'https://b2c.passport.rt.ru/'
    # URL страницы пользовательское соглашение
    USER_AGREEMENT_URL = START_URL + 'sso-static/agreement/agreement.html'
    # URL страницы восстановления пароля
    PASS_RECOVERY_URL = START_URL + 'auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id='
    # URL страницы регистрации нового пользователя
    REGISTER_URL = START_URL + 'auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id='

