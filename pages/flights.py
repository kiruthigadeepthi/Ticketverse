from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Flights:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://9659058568.pythonanywhere.com/flights/"
       
    def load(self):
        self.driver.get(self.url)

    def book_flight(self,source,destination):
        self.driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/input[1]").send_keys(source)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/input[2]").send_keys(destination)
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)

        calendar_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div[3]/div/div/input")))
        calendar_icon.click()
        time.sleep(1)
        month_dropdown = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div/select")
        month_dropdown.send_keys("April")
        time.sleep(1)
        #year_dropdown = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div/div/input")
        #year_dropdown.send_keys("2026")
        
        self.driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/span[32]").click()
        time.sleep(1)
        
        
        slider = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/ul/li[1]/div[1]/span")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", slider)
        time.sleep(2)
        slider.click()
        #actions=ActionChains(self.driver)
        #actions.click_and_hold(slider).move_by_offset(100, 0).release().perform()
        time.sleep(1)
        departure=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/ul/li[2]/div[1]/span")
        departure.click()
        time.sleep(1)
        departure.click()
        time.sleep(1)
        arrival=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/ul/li[3]/div[1]/span")
        arrival.click()
        time.sleep(1)
        arrival.click()
        airline=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/ul/li[4]/div[1]/span")
        airline.click()
        time.sleep(1)

