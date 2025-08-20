import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # Поднимаемся на уровень выше
from locators import MainPageLocators
from urls import URLS


class TestConstructorPage:

    def test_transition_to_bun_success(self, driver):
        # Проверка перехода к разделу "Булки"
        driver.get(URLS.MAIN_PAGE_URL)  # Открываем главную страницу
        driver.find_element(*MainPageLocators.sauces_btn).click()  # Переходим в раздел "Соусы"
        driver.find_element(*MainPageLocators.bun_btn).click()  # Переходим в раздел "Булки"
        bun_text = driver.find_element(*MainPageLocators.bun).text  # Получаем текст заголовка раздела
        bun_displayed = driver.find_element(
            *MainPageLocators.bun_ul
        ).is_displayed()  # Проверяем, что список булок видим
        assert bun_text == 'Булки' and bun_displayed  # Проверяем текст и видимость раздела
    def test_transition_to_sauces_success(self, driver):
        # Проверка перехода к разделу "Соусы"
        driver.get(URLS.MAIN_PAGE_URL)  # Открываем главную страницу
        driver.find_element(*MainPageLocators.sauces_btn).click()  # Кликаем по кнопке "Соусы"
        sauces = driver.find_element(*MainPageLocators.sauces).text  # Получаем текст заголовка раздела
        sauces_displayed = driver.find_element(
            *MainPageLocators.sauces_ul
        ).is_displayed()  # Проверяем, что список соусов видим
        assert sauces == 'Соусы' and sauces_displayed  # Проверяем текст и видимость раздела

    def test_transition_to_topping_success(self, driver):
        # Проверка перехода к разделу "Начинки"
        driver.get(URLS.MAIN_PAGE_URL)  # Открываем главную страницу
        driver.find_element(*MainPageLocators.toppings_btn).click()  # Кликаем по кнопке "Начинки"
        topping = driver.find_element(*MainPageLocators.topping).text  # Получаем текст заголовка раздела
        topping_displayed = driver.find_element(
            *MainPageLocators.topping_ul
        ).is_displayed()  # Проверяем, что список начинок видим
        assert topping == 'Начинки' and topping_displayed  # Проверяем текст и видимость раздела