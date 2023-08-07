import time
from selenium.webdriver.common.by import By

class Login:
    Text_Email_XPATH=(By.XPATH,"//input[@name='email']")
    Text_password_XPATH=(By.XPATH,"//input[@id='password']")
    Click_Login_button_XPATH=(By.XPATH,"//button[@type='submit']")
    login_status = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self,driver):
        self.driver=driver

    def Login_Url(self):
        self.driver.get("https://automation.credence.in/login")

    def Enter_Email(self,email):
        self.driver.find_element(*Login.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self,password):
        self.driver.find_element(*Login.Text_password_XPATH).send_keys(password)

    def Click_On_Login(self):
        self.driver.find_element(*Login.Click_Login_button_XPATH).click()

    def Log_in_Status(self):
        try:
          self.driver.find_element(*Login.login_status)
          return True
        except:
            return False

