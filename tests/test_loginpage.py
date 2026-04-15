from pages.loginpage import LoginPage


def test_valid_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login("kiruthigasns16@gmail.com", "Kiruajith@1234")
    
    driver.save_screenshot("screenshots/valid_login.png")
    assert driver.current_url=="https://9659058568.pythonanywhere.com/"
    
def test_invalid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("kiruthigasns16@gmail.com", "12345678")
    driver.save_screenshot("screenshots/invalid_login.png")
    assert "login" in driver.current_url