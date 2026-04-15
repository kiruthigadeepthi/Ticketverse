import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    #options.add_argument("--headless")
    #driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
