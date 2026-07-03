from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure

class LoginPage(BasePage):
   
   
   PAGE_URL = Links.LOGIN_PAGE
   
   USERNAME_FIELD = ("css selector", "input[name='username']")
   USERPASSWORD_FIELD = ("xpath", "//input[@name='password']")
   SUBMIT_BUTTON = ("css selector", "button[type='submit']")
   
   @allure.step("Вводим логин")
   def enter_login(self, login):
      self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)
      
   @allure.step("Вводим пароль")
   def enter_password(self, password):
      self.wait.until(EC.element_to_be_clickable(self.USERPASSWORD_FIELD)).send_keys(password)
      
   @allure.step("Нажимаем на кнопку 'Login' ")
   def click_submit_button(self):
      self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
      
      
      