from selenium.webdriver.common.by import By
from selenium import webdriver

NAME_INPUT = By.XPATH, ".//label[contains(text(),'Имя')]/parent::div/input" # Поле ввода Имени
EMAIL_INPUT = By.XPATH, ".//label[contains(text(),'Email')]/parent::div/input" # Поле ввода email
PASSWORD_INPUT = By.XPATH, ".//input[@name='Пароль']" # Поле ввода пароля
REG_BUTTON = By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]" # Кнопка регистрации
LOG_IN_BUTTON = By.XPATH, ".//button[contains(text(),'Войти') or contains(text(),'Войти в аккаунт')]" # Кнопка войти
PLACE_ORDER_BUTTON = By.XPATH, ".//button[contains(text(),'Оформить заказ')]"