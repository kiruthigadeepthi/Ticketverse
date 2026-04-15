from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.loginpage import LoginPage
from selenium.webdriver.support.ui import Select

class MovieBooking:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://9659058568.pythonanywhere.com/movies/"
       
    def load(self):
        self.driver.get(self.url)

    def book_movie(self):
        filter=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/ul/li[1]/div[1]/span")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", filter)
        time.sleep(2)
        filter.click()
        time.sleep(1)
        self.driver.save_screenshot("screenshots/moviefilter.png")
        language=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/ul/li[1]/div[2]/label[1]/span")
        language.click()
        time.sleep(2)
        booknow=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[1]/div/button")
        booknow.click()
        time.sleep(1)
        dropdown = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/select")

        select = Select(dropdown)
        select.select_by_visible_text("Madurai")
        cont=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/button")
        cont.click()
        timeslot=self.driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/span")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", timeslot)
        time.sleep(2)
        timeslot.click()
        login=LoginPage(self.driver)
        login.login("kiruthigasns16@gmail.com", "Kiruajith@1234")
        seat=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[1]/div[4]/img")
        seat.click()
        time.sleep(2)
        bookticket=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/form/button")
        bookticket.click()


        
