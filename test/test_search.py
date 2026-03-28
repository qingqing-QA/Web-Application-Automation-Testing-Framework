import pytest
from selenium import webdriver
from pages.login_page import LoginPage



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lcell.bnu.edu.cn/")
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    return driver


# ✅ Test 1: Search (Filter) a specific class
def test_search_specific_class(logged_in_driver):
    classlist = classPage(logged_in_driver)

    classlist.search_class("English")

    results = classlist.get_class_names()

    assert any("English" in item for item in results)


# ✅ Test 2: Search with no matching result
def test_search_no_result(logged_in_driver):
    classlist = classPage(logged_in_driver)

    classlist.search_class("No Results")

    results = classlist.get_class_names()

    assert len(results) == 0


# ✅ Test 3: Empty search (should show all class)
def test_search_empty(logged_in_driver):
    classlist = classPage(logged_in_driver)

    classlist.search_class("")

    results = classlist.get_class_names()

    assert len(results) > 0
