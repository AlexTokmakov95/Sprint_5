from selenium import webdriver
from selenium.webdriver.common.by import By


class Locators:
    button_enter_account = (By.CLASS_NAME, "button_button__33qZ0") # кнопка "Войти в аккаунт" на главной странице
    link_registration = (By.CLASS_NAME, "Auth_link__1fOlj") # ссылка "Зарегистрироваться" на странице входа
    input_name_reg = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # поле ввода "Имя" на странице регистрации
    input_email_reg = (By.XPATH, "//label[text()='Email']/following-sibling::input") # поле ввода "Email" на странице регистрации
    input_password_reg = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # поле ввода "Пароль" на странице регистрации
    button_registration = (By.CSS_SELECTOR, ".button_button__33qZ0") # кнопка "Зарегистрироваться" на странице регистрации
    text_incorrect_password = (By.XPATH, ".//p[contains(@class, 'input__error')]") # текст 'Некорректный пароль' на странице регистрации
    input_email_enter = (By.CSS_SELECTOR, ".input__textfield[name='name']") # поле ввода "Email" на странице входа
    input_password_enter = (By.CSS_SELECTOR, ".input__textfield[name='Пароль']") # поле ввода "Пароль" на странице входа
    button_enter = (By.XPATH, ".//button[text()='Войти']") # кнопка "Войти" на странице входа
    button_order = (By.XPATH, ".//button[text()='Оформить заказ']") # кнопка "Оформить заказ" на главной странице при успешной авторизации
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]') # кнопка "Личный Кабинет" на главной странице при успешной авторизации
    button_exit = (By.XPATH, ".//button[text()='Выход']") # кнопка "Выход" на странице личного кабинета
    link_enter = (By.CLASS_NAME, "Auth_link__1fOlj") # ссылка "Войти" на странице регистрации и восстановления пароля
    button_profile = (By.CLASS_NAME, "Account_link_active__2opc9") # кнопка "Профиль" на странице личного кабинета
    link_constructor = (By.XPATH, ".//p[text()='Конструктор']") # ссылка "Конструктор" на главной странице
    link_recovery_password = (By.XPATH, '//a[text()="Восстановить пароль"]') # ссылка "Восстановить пароль" на странице входа
    text_enter = (By.XPATH, ".//*[text() = 'Вход']") # текст 'Вход' на странице входа
    link_logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") # ссылка логотипа сайта
    button_sauces = (By.XPATH, ".//span[text()='Соусы']/parent::*") # кнопка "Соусы" в форме "Конструктор"
    text_sauces = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']") # текст "Соусы" в форме "Конструктор"
    button_filling = (By.XPATH, ".//span[text()='Начинки']/parent::*") # кнопка "Начинки" в форме "Конструктор"
    text_filling = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']") # текст "Начинки" в форме "Конструктор"
    button_ban = (By.XPATH, ".//span[text()='Булки']/parent::*") # кнопка "Булки" в форме "Конструктор"
    text_ban = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']") # текст "Булки" в форме "Конструктор"