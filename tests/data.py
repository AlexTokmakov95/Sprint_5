import random

class ValidData:
    user_name = 'Test'
    login = f"{random.randint(100, 999)}@ya.ru"
    password = f"{random.randint(100000, 999999)}"

class PersonData:
    user_name = 'Александр'
    login = "Alex_Tokmakov_43_357@yandex.ru"
    password = "426761"

class Urls:
    url_main_paige = "https://stellarburgers.education-services.ru/" # Основная страница

    url_login = "https://stellarburgers.education-services.ru/login" # Ссылка на страницу входа

    url_profile = "https://stellarburgers.education-services.ru/account/profile" # Ссылка формы Личный кабинет -> Профиль

    url_register = "https://stellarburgers.education-services.ru/register" # Ссылка на страницу регистрации

    url_recovery_password = "https://stellarburgers.education-services.ru/forgot-password" # Ссылка на страницу забыл пароль 