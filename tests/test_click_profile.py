from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestClickProfile:

    def test_click_profile_button_passed(self, log_in):
        log_on = log_in
        log_on.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(log_on, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        exit_button = log_on.find_element(*Locators.EXIT_BUTTON).text
        assert exit_button == 'Выход'

    def test_click_constructor_in_profile_passed(self, log_in):
        log_on = log_in
        log_on.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(log_on, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        log_on.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(log_on, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        button_order = log_on.find_element(*Locators.PLACE_ORDER_BUTTON).text
        assert button_order == 'Оформить заказ'

    def test_click_logo_in_profile_passed(self, log_in):
        log_on = log_in
        log_on.find_element(*Locators.PROFILE_BUTTON).click()
        log_on.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(log_on, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        button_order = log_on.find_element(*Locators.PLACE_ORDER_BUTTON).text
        assert button_order == 'Оформить заказ'
