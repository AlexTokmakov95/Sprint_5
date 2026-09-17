import pytest
import random
from locators import Locators
from data import ValidData, Urls

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    def test_correct_login_password_successful_registration(self, connect_driver):
        connect_driver.get(Urls.url_register)

        connect_driver.find_element(*Locators.input_name_reg).send_keys(ValidData.user_name)
        connect_driver.find_element(*Locators.input_email_reg).send_keys(ValidData.login)
        connect_driver.find_element(*Locators.input_password_reg).send_keys(ValidData.password)

        connect_driver.find_element(*Locators.button_registration).click()
        WebDriverWait(connect_driver, 5).until(expected_conditions.presence_of_element_located(Locators.text_enter))
        element = connect_driver.find_element(*Locators.text_enter)
        
        assert connect_driver.current_url == Urls.url_login and element.text == 'Вход'

        connect_driver.quit()

    def test_error_for_incorrect_password_nothing_happens(self, connect_driver):
        connect_driver.get(Urls.url_register)

        connect_driver.find_element(*Locators.input_name_reg).send_keys(ValidData.user_name)
        connect_driver.find_element(*Locators.input_email_reg).send_keys(ValidData.login)
        connect_driver.find_element(*Locators.input_password_reg).send_keys("fgg")

        connect_driver.find_element(*Locators.button_registration).click()
        WebDriverWait(connect_driver, 5).until(expected_conditions.presence_of_element_located(Locators.text_incorrect_password))
        error_message = connect_driver.find_element(*Locators.text_incorrect_password)

        assert error_message.text == 'Некорректный пароль'

        connect_driver.quit()
