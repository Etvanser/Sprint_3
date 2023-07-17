from selenium.webdriver.common.by import By


class Locators:

    PROFILE_BUTTON = By.LINK_TEXT, 'Личный Кабинет' # Кнопка личного кабинета
    REG_TEXT_BUTTON = By.LINK_TEXT, 'Зарегистрироваться' # Кнопка ссылка "Зарегистрироваться"
    INVALID_PASSWORD_TEXT = By.CLASS_NAME, "input__error.text_type_main-default"
    NAME_INPUT = By.XPATH, ".//label[contains(text(),'Имя')]/parent::div/input" # Поле ввода Имени
    EMAIL_INPUT = By.XPATH, ".//label[contains(text(),'Email')]/parent::div/input" # Поле ввода email
    PASSWORD_INPUT = By.XPATH, ".//input[@name='Пароль']" # Поле ввода пароля
    REG_BUTTON = By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]" # Кнопка регистрации
    LOG_IN_BUTTON = By.XPATH, ".//button[contains(text(),'Войти') or contains(text(),'Войти в аккаунт')]" # Кнопка войти
    LOG_IN_LINK_BUTTON = By.XPATH, ".//a[contains(text(),'Войти')]" # Кнопка ссылка в форме регистрации
    RECOVER_PASSWORD_LINK_BUTTON = By.XPATH, ".//a[contains(text(),'Восстановить пароль')]" # Кнопка ссылка "Восстановить пароль"
    PLACE_ORDER_BUTTON = By.XPATH, ".//button[contains(text(),'Оформить заказ')]" # Кнопка оформить заказ
    EXIT_BUTTON = By.XPATH, ".//button[contains(text(),'Выход')]" # Кнопка выход в личном кабинете
    CONSTRUCTOR_BUTTON = By.CLASS_NAME, 'AppHeader_header__logo__2D0X2' # Кнопка конструктора
    PARENT_SAUCER_LINK_BUTTON = By.XPATH, ".//span[contains(text(),'Соусы')]/parent::div"
    PARENT_FILLINGS_LINK_BUTTON = By.XPATH, ".//span[contains(text(),'Начинки')]/parent::div"
    PARENT_BREAD_LINK_BUTTON = By.XPATH, ".//span[contains(text(),'Булки')]/parent::div"
    SAUCER_LINK_BUTTON = By.XPATH, ".//span[contains(text(),'Соусы')]" # Кнопка Соусы
    FILLINGS_LINK_BUTTON = By.XPATH, ".//span[contains(text(),'Начинки')]" # Кнопка Начинки
    BREAD_LINK_BUTTON = By.XPATH, ".//span[contains(text(),'Булки')]" # Кнопка Булки
    HEADING_TEXT_LOG_IN = By.XPATH, ".//h2[contains(text(),'Вход')]"
