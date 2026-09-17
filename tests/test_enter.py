import pytest
import random
from locators import Locators
from data import ValidData, Urls, PersonData

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestEnter:

    def test_login_sign_in_button_show_login_page(self, connect_driver): # вход через кноку 'Войти в аккаунт' на главной
        
        connect_driver.find_element(*Locators.button_enter_account).click()

        connect_driver.find_element(*Locators.input_email_enter).send_keys(PersonData.login)
        connect_driver.find_element(*Locators.input_password_enter).send_keys(PersonData.password)

        connect_driver.find_element(*Locators.button_enter).click()
        WebDriverWait(connect_driver, 5).until(expected_conditions.presence_of_element_located(Locators.button_order))

        order_button = connect_driver.find_element(*Locators.button_order)
        assert connect_driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'
        
        connect_driver.quit()

    def test_login_personal_account_button_show_login_page(self, connect_driver): # вход через кнопку «Личный кабинет»

        connect_driver.find_element(*Locators.button_personal_account).click()

        connect_driver.find_element(*Locators.input_email_enter).send_keys(PersonData.login)
        connect_driver.find_element(*Locators.input_password_enter).send_keys(PersonData.password)

        connect_driver.find_element(*Locators.button_enter).click()
        WebDriverWait(connect_driver, 5).until(expected_conditions.presence_of_element_located(Locators.button_order))

        order_button = connect_driver.find_element(*Locators.button_order)
        assert connect_driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'
        
        connect_driver.quit()

    def test_login_registration_form_sign_in_button(self, connect_driver): # вход через кнопку в форме регистрации

        connect_driver.get(Urls.url_register)

        connect_driver.find_element(*Locators.link_enter).click()

        connect_driver.find_element(*Locators.input_email_enter).send_keys(PersonData.login)
        connect_driver.find_element(*Locators.input_password_enter).send_keys(PersonData.password)

        connect_driver.find_element(*Locators.button_enter).click()
        WebDriverWait(connect_driver, 5).until(expected_conditions.presence_of_element_located(Locators.button_order))

        order_button = connect_driver.find_element(*Locators.button_order)
        assert connect_driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'

        connect_driver.quit()

    def test_login_recovery_password_form_sign_in_button(self, connect_driver): # вход через кнопку в форме восстановления пароля
        
        connect_driver.get(Urls.url_recovery_password)

        connect_driver.find_element(*Locators.link_enter).click()

        connect_driver.find_element(*Locators.input_email_enter).send_keys(PersonData.login)
        connect_driver.find_element(*Locators.input_password_enter).send_keys(PersonData.password)

        connect_driver.find_element(*Locators.button_enter).click()
        WebDriverWait(connect_driver, 5).until(expected_conditions.presence_of_element_located(Locators.button_order))

        order_button = connect_driver.find_element(*Locators.button_order)
        assert connect_driver.current_url == Urls.url_main_paige and order_button.text == 'Оформить заказ'

        connect_driver.quit()