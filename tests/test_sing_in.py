from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
from locators import LOG_IN_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, PLACE_ORDER_BUTTON
from data import valid_email, valid_password
def test_log_in(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*LOG_IN_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys(valid_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(valid_password)
    driver.find_element(*LOG_IN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((PLACE_ORDER_BUTTON)))
    button_order = driver.find_element(*PLACE_ORDER_BUTTON).text
    assert button_order == 'Оформить заказ'
