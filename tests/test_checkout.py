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

def test_checkout(driver):
    # Step 1: Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Step 2: Wait for inventory page
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Step 3: Add item to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Step 4: Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Step 5: Wait for cart page
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
    )

    # Step 6: Click checkout
    driver.find_element(By.ID, "checkout").click()

    # Step 7: Fill in checkout form
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Priyanka")
    driver.find_element(By.ID, "last-name").send_keys("Jain")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # Step 8: Continue to overview page
    driver.find_element(By.ID, "continue").click()

    # Step 9: Click Finish
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    ).click()

    # Step 10: Verify success message
    confirmation = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text

    assert confirmation == "Thank you for your order!"
    print("Checkout completed successfully.")
