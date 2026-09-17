import pytest
from data import PersonData, Urls
from selenium import webdriver
from locators import Locators

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture 
def connect_driver():
    driver = webdriver.Chrome()
    driver.get(Urls.url_main_paige)
    return driver

@pytest.fixture
def login_password_enter(connect_driver):
    connect_driver.get(Urls.url_login)

    connect_driver.find_element(*Locators.input_email_enter).send_keys(PersonData.login)
    connect_driver.find_element(*Locators.input_password_enter).send_keys(PersonData.password)
    connect_driver.find_element(*Locators.button_enter).click()

    WebDriverWait(connect_driver, 5).until(expected_conditions.presence_of_element_located(Locators.button_order))
    return connect_driver