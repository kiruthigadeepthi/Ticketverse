from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://9659058568.pythonanywhere.com/users/login/"
        # Locators
    def load(self):
        self.driver.get(self.url)

    def login(self, email, password):
        self.driver.find_element(By.NAME, "email").send_keys(email)
        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        time.sleep(2)
        
        element=self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div[4]/button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        element.click()
