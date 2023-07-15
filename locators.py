from selenium.webdriver.common.by import By

PROFILE_BUTTON = By.LINK_TEXT, 'Личный Кабинет' # Кнопка личного кабинета
REG_TEXT_BUTTON = By.LINK_TEXT, 'Зарегистрироваться' # Кнопка ссылка "Зарегистрироваться"
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
SAUCER_LINK_BUTTON = By.XPATH, ".//span[contains(text(),'Соусы')]" # Кнопка Соусы
FILLINGS_LINK_BUTTON = By.XPATH, ".//span[contains(text(),'Начинки')]" # Кнопка Начинки
BREAD_LINK_BUTTON = By.XPATH, ".//span[contains(text(),'Булки')]" # Кнопка Булки
