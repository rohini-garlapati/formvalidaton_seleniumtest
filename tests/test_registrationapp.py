import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

# Test 1: Empty name
def test_empty_name(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "email").send_keys("user@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("abcdef")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    time.sleep(1)
    alert = Alert(driver)
    alert_text = alert.text
    assert "Name cannot be empty" in alert_text
    alert.accept()

# Test 2: Empty email
def test_empty_email(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "name").send_keys("Rohini")
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "password").send_keys("abcdef")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    time.sleep(1)
    alert = Alert(driver)
    alert_text = alert.text
    assert "Email cannot be empty" in alert_text
    alert.accept()

# Test 3: Name too short (<3 chars)
def test_short_name(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "name").send_keys("Ro")
    driver.find_element(By.NAME, "email").send_keys("user@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("abcdef")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    time.sleep(1)
    alert = Alert(driver)
    alert_text = alert.text
    assert "Name must be at least 3 characters long" in alert_text
    alert.accept()

# Test 4: Empty password
def test_empty_password(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "name").send_keys("Rohini")
    driver.find_element(By.NAME, "email").send_keys("user@gmail.com")
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    time.sleep(1)
    alert = Alert(driver)
    alert_text = alert.text
    assert "Password cannot be empty" in alert_text
    alert.accept()

# Test 5: Valid input — should redirect and show greeting
def test_valid_input(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "name").send_keys("Rohini")
    driver.find_element(By.NAME, "email").send_keys("rohinisai1410@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("abcdef")
    driver.find_element(By.NAME, "year").send_keys("4")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Wait for redirect
    time.sleep(2)

    # Verify URL and message
    current_url = driver.current_url
    assert "/submit" in current_url, f"Expected redirect to result page, but got: {current_url}"

    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Welcome Rohini" in body_text, f"Greeting not found or incorrect: {body_text}"
