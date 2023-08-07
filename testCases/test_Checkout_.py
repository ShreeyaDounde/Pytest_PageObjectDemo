import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.LoginPage1 import Login
from pageObjects.CheckOutPage1 import Credkart_checkout

class Test_CredKart_Checkout:

    def test_checkout(self,setup):
        self.driver=setup
        self.lp=Login(self.driver)
        self.lp.Login_Url()
        self.lp.Enter_Email("Credencetest@test.com")
        self.lp.Enter_Password("Credence@123")
        self.lp.Click_On_Login()
        self.cop=Credkart_checkout(self.driver)
        #click on macbook
        self.cop.Click_MacBook()
        #click on add to cart
        self.driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # Proceed to Checkout
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
        time.sleep(3)
        # Enter First_Name
        self.driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Credence")
        # Enter Last_Name
        self.driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Pune")
        # Enter Phone
        self.driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9091929355")
        # Enter Address
        self.driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Dhankawdi, Pune")
        # Enter Zip
        self.driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("411013")
        # Select state
        state = Select(self.driver.find_element(By.XPATH, "//select[@id='state']"))
        state.select_by_visible_text("Pune")
        # Enter  Owner name
        self.driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Tushar")
        # Enter CVV
        self.driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("043")
        # Select Year
        year = Select(self.driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        year.select_by_index(2)

        # Select Month
        month = Select(self.driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        month.select_by_index(2)

        # Enter card number\
        # 5281 0370 4891 6168
        self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
        self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
        self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
        self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")
        # Click on Checkout button
        self.driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()

        print(self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]").text)


