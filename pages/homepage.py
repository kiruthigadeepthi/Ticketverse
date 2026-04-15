from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        #self.actions=ActionChains(driver)
        self.url = "https://9659058568.pythonanywhere.com/"
       
    def load(self):
        self.driver.get(self.url)

    def select_tab(self, option_text):
        self.driver.find_element(By.LINK_TEXT,option_text).click()
        return self.driver.current_url
 