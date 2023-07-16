from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
from locators import Locators
from helpers import generic_password, generic_email


def test_registration_passed(driver_chrome):
    email = generic_email()
    password = generic_password()

    driver = driver_chrome
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*Locators.PROFILE_BUTTON).click()
    driver.find_element(*Locators.REG_TEXT_BUTTON).click()
    driver.find_element(*Locators.NAME_INPUT).send_keys("Александр")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.REG_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOG_IN_BUTTON))
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOG_IN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
    button_order = driver.find_element(*Locators.PLACE_ORDER_BUTTON).text
    assert button_order == 'Оформить заказ'


def test_registration_fail_password(driver_chrome):
    driver = driver_chrome
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*Locators.PROFILE_BUTTON).click()
    driver.find_element(*Locators.REG_TEXT_BUTTON).click()
    driver.find_element(*Locators.NAME_INPUT).send_keys("Александр")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(generic_email())
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(random.randint(10000, 99999))
    driver.find_element(*Locators.REG_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.REG_BUTTON))
    error = driver.find_element(By.CLASS_NAME, "input__error.text_type_main-default").text
    assert error == 'Некорректный пароль'
