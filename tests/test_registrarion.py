from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
from locators import NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REG_BUTTON, LOG_IN_BUTTON
def test_registration_passed(generic_email, generic_password, driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()

    driver.find_element(*NAME_INPUT).send_keys("Александр")
    driver.find_element(*EMAIL_INPUT).send_keys(generic_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(generic_password)
    driver.find_element(*REG_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((LOG_IN_BUTTON)))
    assert "/login" in driver.current_url
    driver.quit()

def test_registration_fail_password(generic_email, driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()

    driver.find_element(*NAME_INPUT).send_keys("Александр")
    driver.find_element(*EMAIL_INPUT).send_keys(generic_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(random.randint(10000, 99999))
    driver.find_element(*REG_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((REG_BUTTON)))
    error = driver.find_element(By.CLASS_NAME, "input__error.text_type_main-default").text
    assert error == 'Некорректный пароль'
