from random import randint

class Person:
    user_name = 'Андрей'
    email = 'Andrey_Zubkov_29_123@yandex.ru'
    password = 'ZAG123456'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Qwe'