from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import PROFILE_BUTTON, EXIT_BUTTON

def test_click_exit_button_in_profile_passed(driver_chrome, log_in):
    driver_chrome = log_in
    driver_chrome.find_element(*PROFILE_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((EXIT_BUTTON)))
    driver_chrome.find_element(*EXIT_BUTTON).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text(),'Вход')]")))
    login_text = driver_chrome.find_element(By.XPATH, ".//h2[contains(text(),'Вход')]").text
    assert login_text == 'Вход'
    driver_chrome.quit()