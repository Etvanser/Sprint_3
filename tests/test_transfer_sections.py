from selenium.webdriver.common.by import By
from locators import SAUCER_LINK_BUTTON, FILLINGS_LINK_BUTTON, BREAD_LINK_BUTTON

def test_transter_sauce_section_passed(driver_chrome, log_in):
    driver_chrome = log_in
    class_sauce = driver_chrome.find_element(By.XPATH, ".//span[contains(text(),'Соусы')]/parent::div")
    before_click = class_sauce.get_attribute('class')
    driver_chrome.find_element(*SAUCER_LINK_BUTTON).click()
    after_click = class_sauce.get_attribute('class')
    assert before_click != after_click

def test_transter_fillings_section_passed(driver_chrome, log_in):
    driver_chrome = log_in
    class_fillings = driver_chrome.find_element(By.XPATH, ".//span[contains(text(),'Начинки')]/parent::div")
    before_click = class_fillings.get_attribute('class')
    driver_chrome.find_element(*FILLINGS_LINK_BUTTON).click()
    after_click = class_fillings.get_attribute('class')
    assert before_click != after_click

def test_transter_bread_section_passed(driver_chrome, log_in):
    driver_chrome = log_in
    driver_chrome.find_element(*SAUCER_LINK_BUTTON).click()
    class_bread= driver_chrome.find_element(By.XPATH, ".//span[contains(text(),'Булки')]/parent::div")
    before_click = class_bread.get_attribute('class')
    driver_chrome.find_element(*BREAD_LINK_BUTTON).click()
    after_click = class_bread.get_attribute('class')
    assert before_click != after_click


