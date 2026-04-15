import pytest
from pages.homepage import HomePage

@pytest.mark.parametrize("tab,expected_url_part", [
    ("Flights", "flights"),
    ("Train", "trains"),
    ("Bus", "bus"),
    ("Movies", "movies"),
    ("Events","events"),
    ("Sports","sports"),
    ("Hotels","hotels")
])
def test_navigation_tabs(driver, tab, expected_url_part):
    homepage = HomePage(driver)
    homepage.load()
    current_url = homepage.select_tab(tab)
    assert expected_url_part in current_url.lower()