from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


def test_click_exit_button_in_profile_passed(log_in):
    log_on = log_in
    log_on.find_element(*Locators.PROFILE_BUTTON).click()
    WebDriverWait(log_on, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
    log_on.find_element(*Locators.EXIT_BUTTON).click()
    WebDriverWait(log_on, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADING_TEXT_LOG_IN))
    login_text = log_on.find_element(*Locators.HEADING_TEXT_LOG_IN).text
    assert login_text == 'Вход'
