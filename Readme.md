
# 🧪 SauceDemo UI Automation Framework

This is the UI automation framework for testing the **SauceDemo** e-commerce web application.

---

## ✅ Features

- Login, Add to Cart, and Checkout flow automation
- Selenium WebDriver for browser automation
- PyTest for test structure and execution
- Headless and incognito mode support

---

## 🖥️ Prerequisites

- Python 3.12 or higher installed
- Google Chrome browser installed
- ChromeDriver managed via `webdriver-manager`
- pip packages listed in `requirements.txt`

---

## ▶️ How to Run Tests Locally

1. Clone the repository:
```bash
git clone https://github.com/your-username/Saucedemo_Automation.git
cd Saucedemo_Automation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run all tests
```bash
pytest
```

4. Run a specific test file:
```bash
pytest tests/test_login.py
```

---

## 🧪 Test Strategy

- Covers end-to-end scenarios:
    - Valid and invalid login
    - Product selection and cart validation
    - Successful checkout process
- Verifies URL transitions, page contents, and expected UI elements

---
