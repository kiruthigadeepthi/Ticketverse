from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.loginpage import LoginPage

class BusBooking:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://9659058568.pythonanywhere.com/buses/"
       
    def load(self):
        self.driver.get(self.url)

    def book_bus(self):
        booknow=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[2]/div/button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", booknow)
        time.sleep(1)
        booknow.click()
        time.sleep(1)
        login=LoginPage(self.driver)
        login.login("kiruthigasns16@gmail.com", "Kiruajith@1234")
        seat=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img")
        seat.click()
        add_passengers=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/form/button")
        add_passengers.click()
        first_name=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[3]/div[2]/input")
        first_name.send_keys("Kiruthiga")
        time.sleep(1)
        last_name=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[3]/div[3]/input")
        last_name.send_keys("Ajith")
        time.sleep(1)
        gender=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[4]/div[1]/div/div[2]/span")
        gender.click()
        time.sleep(1)
        dob=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[4]/div[2]/div/input[2]")
        dob.send_keys("16/11/2000")
        time.sleep(1)
        nationality=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[5]/div[1]/input")
        nationality.send_keys("INDIAN")
        time.sleep(1)
        phone=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[5]/div[2]/input")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", phone)
        phone.send_keys("9278300110")
        time.sleep(1)
        email=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[6]/div[1]/input")
        email.send_keys("kiruthigasns16@gmail.com")
        time.sleep(1)
        address=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[6]/div[2]/input")
        address.send_keys("abc")
        time.sleep(1)
        postcode=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div[1]/input")
        postcode.send_keys("562761")
        time.sleep(1)
        passport=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div[2]/input")
        passport.send_keys("12345")
        time.sleep(1)
        add_button=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/button")
        add_button.click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        print("Alert says:", alert.text)
        alert.accept()
        payment=self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/button")
        payment.click()
        time.sleep(2)