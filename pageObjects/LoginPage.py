from selenium.webdriver.common.by import By


class login:
    text_username_id="Email"
    text_password_id="Password"
    login_button_xpath="//button[@type='submit']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID, self.text_username_id).clear()
        self.driver.find_element(By.ID,self.text_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID,self.text_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()

