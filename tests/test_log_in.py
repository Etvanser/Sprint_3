from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import valid_email, valid_password


class TestLogIn:
    def test_log_in_main_page_passed(self, driver_chrome):
        driver = driver_chrome
        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(valid_password)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        button_order = driver.find_element(*Locators.PLACE_ORDER_BUTTON).text
        assert button_order == 'Оформить заказ'

    def test_log_in_profile_page_passed(self, driver_chrome):
        driver = driver_chrome
        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(valid_password)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        button_order = driver.find_element(*Locators.PLACE_ORDER_BUTTON).text
        assert button_order == 'Оформить заказ'

    def test_log_in_form_registration_passed(self, driver_chrome):
        driver = driver_chrome
        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.REG_TEXT_BUTTON).click()
        driver.find_element(*Locators.LOG_IN_LINK_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(valid_password)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        button_order = driver.find_element(*Locators.PLACE_ORDER_BUTTON).text
        assert button_order == 'Оформить заказ'

    def test_log_in_form_recover_password_passed(self, driver_chrome):
        driver = driver_chrome
        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.RECOVER_PASSWORD_LINK_BUTTON).click()
        driver.find_element(*Locators.LOG_IN_LINK_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(valid_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(valid_password)
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        button_order = driver.find_element(*Locators.PLACE_ORDER_BUTTON).text
        assert button_order == 'Оформить заказ'
