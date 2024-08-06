import pytest
from selenium import webdriver

@pytest.fixture()
def set(browser):
    if browser == "ie":
        driver = webdriver.Ie()
    elif browser =="firefox":
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")