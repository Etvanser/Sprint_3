import pytest
import random
from selenium import webdriver

@pytest.fixture
def generic_email():
    email = ("aleksandrkozlov11", str(random.randint(1000, 9999)), "@ya.ru")
    return email
@pytest.fixture
def generic_password():
    return random.randint(100000, 999999)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
