from selenium import webdriver
from urls import URLS
from locators import MainPageLocators


class TestConstructorPage:

    def test_transition_to_bun_success(self, driver):
        """Проверка перехода к разделу 'Булки'"""
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        driver.find_element(*MainPageLocators.bun_btn).click()

        bun_text = driver.find_element(*MainPageLocators.bun).text
        bun_displayed = driver.find_element(*MainPageLocators.bun_ul).is_displayed()

        assert bun_text == 'Булки' and bun_displayed

    def test_transition_to_sauces_success(self, driver):
        """Проверка перехода к разделу 'Соусы'"""
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()

        sauces_text = driver.find_element(*MainPageLocators.sauces).text
        sauces_displayed = driver.find_element(*MainPageLocators.sauces_ul).is_displayed()

        assert sauces_text == 'Соусы' and sauces_displayed

    def test_transition_to_topping_success(self, driver):
        """Проверка перехода к разделу 'Начинки'"""
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.toppings_btn).click()

        topping_text = driver.find_element(*MainPageLocators.topping).text
        topping_displayed = driver.find_element(*MainPageLocators.topping_ul).is_displayed()

        assert topping_text == 'Начинки' and topping_displayed

