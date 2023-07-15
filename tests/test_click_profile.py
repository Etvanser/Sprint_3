from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import PLACE_ORDER_BUTTON, PROFILE_BUTTON, EXIT_BUTTON, CONSTRUCTOR_BUTTON

def test_click_profile_button_passed(driver_chrome, log_in):
    driver_chrome = log_in
    driver_chrome.find_element(*PROFILE_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((EXIT_BUTTON)))
    exit_button = driver_chrome.find_element(*EXIT_BUTTON).text
    assert exit_button == 'Выход'
    driver_chrome.quit()

def test_click_constructor_in_profile_passed(driver_chrome, log_in):
    driver_chrome = log_in
    driver_chrome.find_element(*PROFILE_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((EXIT_BUTTON)))
    driver_chrome.find_element(*CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((PLACE_ORDER_BUTTON)))
    button_order = driver_chrome.find_element(*PLACE_ORDER_BUTTON).text
    assert button_order == 'Оформить заказ'
    driver_chrome.quit()

def test_click_logo_in_profile_passed(driver_chrome, log_in):
    driver_chrome = log_in
    driver_chrome.find_element(*PROFILE_BUTTON).click()
    driver_chrome.find_element(*CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((PLACE_ORDER_BUTTON)))
    button_order = driver_chrome.find_element(*PLACE_ORDER_BUTTON).text
    assert button_order == 'Оформить заказ'
    driver_chrome.quit()