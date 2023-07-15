from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LOG_IN_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, PLACE_ORDER_BUTTON, PROFILE_BUTTON, REG_TEXT_BUTTON,\
    LOG_IN_LINK_BUTTON, RECOVER_PASSWORD_LINK_BUTTON
from data import valid_email, valid_password
def test_log_in_main_page_passed(driver_chrome):
    driver_chrome.get('https://stellarburgers.nomoreparties.site/')

    driver_chrome.find_element(*LOG_IN_BUTTON).click()
    driver_chrome.find_element(*EMAIL_INPUT).send_keys(valid_email)
    driver_chrome.find_element(*PASSWORD_INPUT).send_keys(valid_password)
    driver_chrome.find_element(*LOG_IN_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((PLACE_ORDER_BUTTON)))
    button_order = driver_chrome.find_element(*PLACE_ORDER_BUTTON).text
    assert button_order == 'Оформить заказ'
    driver_chrome.quit()
def test_log_in_profile_page_passed(driver_chrome):
    driver_chrome.get('https://stellarburgers.nomoreparties.site/')

    driver_chrome.find_element(*PROFILE_BUTTON).click()
    driver_chrome.find_element(*EMAIL_INPUT).send_keys(valid_email)
    driver_chrome.find_element(*PASSWORD_INPUT).send_keys(valid_password)
    driver_chrome.find_element(*LOG_IN_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((PLACE_ORDER_BUTTON)))
    button_order = driver_chrome.find_element(*PLACE_ORDER_BUTTON).text
    assert button_order == 'Оформить заказ'
    driver_chrome.quit()

def test_log_in_form_registration_passed(driver_chrome):
    driver_chrome.get('https://stellarburgers.nomoreparties.site/')

    driver_chrome.find_element(*PROFILE_BUTTON).click()
    driver_chrome.find_element(*REG_TEXT_BUTTON).click()
    driver_chrome.find_element(*LOG_IN_LINK_BUTTON).click()
    driver_chrome.find_element(*EMAIL_INPUT).send_keys(valid_email)
    driver_chrome.find_element(*PASSWORD_INPUT).send_keys(valid_password)
    driver_chrome.find_element(*LOG_IN_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((PLACE_ORDER_BUTTON)))
    button_order = driver_chrome.find_element(*PLACE_ORDER_BUTTON).text
    assert button_order == 'Оформить заказ'
    driver_chrome.quit()

def test_log_in_form_reсover_password_passed(driver_chrome):
    driver_chrome.get('https://stellarburgers.nomoreparties.site/')

    driver_chrome.find_element(*PROFILE_BUTTON).click()
    driver_chrome.find_element(*RECOVER_PASSWORD_LINK_BUTTON).click()
    driver_chrome.find_element(*LOG_IN_LINK_BUTTON).click()
    driver_chrome.find_element(*EMAIL_INPUT).send_keys(valid_email)
    driver_chrome.find_element(*PASSWORD_INPUT).send_keys(valid_password)
    driver_chrome.find_element(*LOG_IN_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((PLACE_ORDER_BUTTON)))
    button_order = driver_chrome.find_element(*PLACE_ORDER_BUTTON).text
    assert button_order == 'Оформить заказ'
    driver_chrome.quit()