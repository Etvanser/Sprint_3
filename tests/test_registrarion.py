from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
from locators import NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REG_BUTTON, LOG_IN_BUTTON, PROFILE_BUTTON, REG_TEXT_BUTTON
def test_registration_passed(generic_email, generic_password, driver_chrome):
    driver_chrome.get('https://stellarburgers.nomoreparties.site/')

    driver_chrome.find_element(*PROFILE_BUTTON).click()
    driver_chrome.find_element(*REG_TEXT_BUTTON).click()
    driver_chrome.find_element(*NAME_INPUT).send_keys("Александр")
    driver_chrome.find_element(*EMAIL_INPUT).send_keys(generic_email)
    driver_chrome.find_element(*PASSWORD_INPUT).send_keys(generic_password)
    driver_chrome.find_element(*REG_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((LOG_IN_BUTTON)))
    assert "/login" in driver_chrome.current_url
    driver_chrome.quit()

def test_registration_fail_password(generic_email, driver_chrome):
    driver_chrome.get('https://stellarburgers.nomoreparties.site/')

    driver_chrome.find_element(*PROFILE_BUTTON).click()
    driver_chrome.find_element(*REG_TEXT_BUTTON).click()
    driver_chrome.find_element(*NAME_INPUT).send_keys("Александр")
    driver_chrome.find_element(*EMAIL_INPUT).send_keys(generic_email)
    driver_chrome.find_element(*PASSWORD_INPUT).send_keys(random.randint(10000, 99999))
    driver_chrome.find_element(*REG_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(
        expected_conditions.visibility_of_element_located((REG_BUTTON)))
    error = driver_chrome.find_element(By.CLASS_NAME, "input__error.text_type_main-default").text
    assert error == 'Некорректный пароль'
    driver_chrome.quit()