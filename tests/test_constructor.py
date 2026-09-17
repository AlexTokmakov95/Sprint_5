import pytest
import random
from locators import Locators
from data import ValidData, Urls, PersonData

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login_password_enter): # Переход к разделу "Соусы"

        driver = login_password_enter

        driver.find_element(*Locators.link_constructor).click()
        driver.find_element(*Locators.button_sauces).click()

        element = driver.find_element(*Locators.text_sauces)

        assert element.text == 'Соусы'

        driver.quit()

    def test_constructor_go_to_filling_scroll_to_filling(self, login_password_enter): # Переход к разделу "Начинки"

        driver = login_password_enter

        driver.find_element(*Locators.link_constructor).click()
        driver.find_element(*Locators.button_filling).click()

        element = driver.find_element(*Locators.text_filling)

        assert element.text == 'Начинки'

        driver.quit()

    def test_constructor_go_to_bun_scroll_to_bun(self, login_password_enter): # Переход к разделу "Булки"

        driver = login_password_enter

        driver.find_element(*Locators.link_constructor).click()
        driver.find_element(*Locators.button_filling).click()
        driver.find_element(*Locators.button_ban).click()

        element = driver.find_element(*Locators.text_ban)

        assert element.text == 'Булки' 

        driver.quit()   





