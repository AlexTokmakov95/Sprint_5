import pytest
import random
from locators import Locators
from data import ValidData, Urls, PersonData

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestTransitions:

    def test_click_profile_button_open_profile_form(self, login_password_enter): # переход по клику на «Личный кабинет»

        driver = login_password_enter

        driver.find_element(*Locators.button_personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.button_profile))
        element = driver.find_element(*Locators.button_profile)
        assert Urls.url_profile == driver.current_url and element.text == 'Профиль'

        driver.quit()

    def test_click_constructor_button_show_constructor_form(self, login_password_enter): # Переход из личного кабинета в конструктор

        driver = login_password_enter

        driver.find_element(*Locators.button_personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.button_profile))
        driver.find_element(*Locators.link_constructor).click()

        element = driver.find_element(*Locators.button_order)
        assert Urls.url_main_paige == driver.current_url and element.text == 'Оформить заказ'

        driver.quit()

    def test_click_logo_button_show_constructor_form(self, login_password_enter): # Переход из личного кабинета в конструктор при нажатии на лого

        driver = login_password_enter

        driver.find_element(*Locators.button_personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.button_profile))
        driver.find_element(*Locators.link_logo).click()

        element = driver.find_element(*Locators.button_order)
        assert Urls.url_main_paige == driver.current_url and element.text == 'Оформить заказ'

        driver.quit()

    def test_click_logout_button_in_personal_account_open_login_form(self, login_password_enter): # выход по кнопке «Выйти» в личном кабинете

        driver = login_password_enter

        driver.find_element(*Locators.button_personal_account).click()
        
        WebDriverWait(driver, 8).until(expected_conditions.presence_of_element_located(Locators.button_profile))

        driver.find_element(*Locators.button_exit).click()
        WebDriverWait(driver, 8).until(expected_conditions.presence_of_element_located(Locators.button_enter))

        element = driver.find_element(*Locators.text_enter)
        assert driver.current_url == Urls.url_login and element.text == 'Вход'

        driver.quit()         
