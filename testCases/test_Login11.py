from pageObjects.LoginPage1 import Login

class Test_Credkart_Login:
    def test_Credkart_Login_002(self,setup):
        self.driver=setup
        self.lp=Login(self.driver)
        self.lp.Login_Url()
        self.lp.Enter_Email("Credencetest@test.com")
        self.lp.Enter_Password("Credence@123")
        self.lp.Click_On_Login()
        print(self.lp.Log_in_Status())
        if self.lp.Log_in_Status()==True:
            self.driver.save_screenshot("C:\\Users\\dound\\PycharmProjects\\Pytest_PageObjectDemo\\Screenshots\\login.PNG")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\dound\\PycharmProjects\\Pytest_PageObjectDemo\\Screenshots\\login_Fail.PNG")
            assert False

