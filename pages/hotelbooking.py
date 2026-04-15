from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.loginpage import LoginPage

class Hotelbooking:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://9659058568.pythonanywhere.com/"
       
    def load(self):
        self.driver.get(self.url)

    def bookhotel(self):
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/a").click()

        login=LoginPage(self.driver)
        login.login("kiruthigasns16@gmail.com", "Kiruajith@1234")
        hotels=self.driver.find_element(By.XPATH,"/html/body/div[1]/div/ul/a[8]/li")
        hotels.click()
        type=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/ul/li[2]/div[1]/span")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", type)
        time.sleep(2)
        type.click()
        self.driver.save_screenshot("screenshots/hoteltype.png")
        select_type=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/ul/li[2]/div[2]/label[1]/span")
        time.sleep(2)
        select_type.click()
        time.sleep(2)
        bookrooms=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/div[2]/button")
        bookrooms.click()
        time.sleep(2)
        checkin=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div[1]/div/input[2]")
        checkin.send_keys("20/04/2026")
        checkout=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div[2]/div/input[2]")
        checkout.send_keys("22/04/2026")
        time.sleep(2)
        payment=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[10]/button")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", payment)
        time.sleep(2)
        payment.click()
        time.sleep(2)
        #card=self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div/form/div[3]/div/label[2]/div/div/span")
        #card.click()


