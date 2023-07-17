import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import valid_email, valid_password


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def log_in(driver_chrome):
    driver = driver_chrome
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*Locators.LOG_IN_BUTTON).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(valid_email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(valid_password)
    driver.find_element(*Locators.LOG_IN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
    return driver
