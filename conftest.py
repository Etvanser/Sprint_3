import pytest
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LOG_IN_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, PLACE_ORDER_BUTTON
from data import valid_email, valid_password
@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
@pytest.fixture
def generic_email():
    email = ("aleksandrkozlov11", str(random.randint(1000, 9999)), "@ya.ru")
    return email
@pytest.fixture
def generic_password():
    return random.randint(100000, 999999)

@pytest.fixture
def log_in(driver_chrome):
    driver_chrome.get('https://stellarburgers.nomoreparties.site/')

    driver_chrome.find_element(*LOG_IN_BUTTON).click()
    driver_chrome.find_element(*EMAIL_INPUT).send_keys(valid_email)
    driver_chrome.find_element(*PASSWORD_INPUT).send_keys(valid_password)
    driver_chrome.find_element(*LOG_IN_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((PLACE_ORDER_BUTTON)))
    return driver_chrome