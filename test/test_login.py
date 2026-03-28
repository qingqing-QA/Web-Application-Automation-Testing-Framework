import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.lcell.bnu.edu/")
    yield driver
    driver.quit()

def test_valid_login(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
