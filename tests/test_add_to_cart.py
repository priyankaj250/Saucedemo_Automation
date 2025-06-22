import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.driver_setup import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def test_add_single_item_to_cart(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    try:
        cart_badge = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        ).text
        assert cart_badge == "1"
        print("Single item added to cart successfully.")
    except TimeoutException:
        driver.save_screenshot("single_cart_badge_missing.png")
        pytest.fail("Cart badge did not appear or item was not added.")

def test_add_multiple_items_to_cart(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    try:
        cart_badge = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        ).text
        assert cart_badge == "2"
        print("Multiple items added to cart successfully.")
    except TimeoutException:
        driver.save_screenshot("multiple_cart_badge_missing.png")
        pytest.fail("Cart badge did not appear or items were not added.")
