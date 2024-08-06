import pytest
from selenium import webdriver
from pageObjects.LoginPage import login
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen

class Test_001_login:
    baseUrl= readConfig.getApplicationUrl()
    username=readConfig.getuseremail()
    password=readConfig.getuserpasswd()
    logger=LogGen.loggen()
    def test_homePageTitle(self,set):
        self.logger.info("************** Test_001_login **************")
        self.logger.info("********* Verify Home Page Title *************")
        self.driver= set
        self.driver.get(self.baseUrl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.logger.info("******** Test Case Passed *******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("******* Test case Failed ******")
            assert False

    def test_login(self,set):
        self.logger.info("******** Verifying Login Test ********")
        self.driver=set
        self.driver.get(self.baseUrl)
        self.login=login(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********** Login Test Passed *********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Login Test Failed *********")
            assert False
print(readConfig.getApplicationUrl())
