from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_saucedemo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    # Добавление товара
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)
    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
    # Проверка, что товар в корзине
    item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert "Sauce Labs Backpack" in item_name, "Товар не найден в корзине"
    # Оформление заказа
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)
    # Завершение покупки
    driver.find_element(By.ID, "finish").click()
    time.sleep(1)
    # Проверка успешного завершения
    complete_text = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "THANK YOU FOR YOUR ORDER" in complete_text.upper(), "Покупка не завершена"
    time.sleep(2)
    driver.quit()
