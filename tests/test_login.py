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

def test_login_success(driver):
    # Enter correct username and password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for products page
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        assert "inventory" in driver.current_url
        print("Login successful.")
    except TimeoutException:
        driver.save_screenshot("login_failed.png")
        pytest.fail("Login failed or inventory page did not load.")

def test_login_invalid_credentials(driver):
    # Enter invalid username and password
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()

    # Wait for and verify error message
    try:
        error_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        error_text = error_element.text
        assert "Epic sadface" in error_text
        print("Invalid login test passed.")
    except TimeoutException:
        driver.save_screenshot("invalid_login_failed.png")
        pytest.fail("Expected error message did not appear.")
