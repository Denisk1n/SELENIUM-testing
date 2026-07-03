from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure

class MyInfoPage(BasePage):
   
   
   PAGE_URL = Links.MY_INFO_PAGE
   
   FIRST_NAME_FIELD = ("css selector", "input[name='firstName']")
   SAVE_CHANGES_BUTTON = ("css selector", ".orangehrm-horizontal-padding button[type='submit']")
   
   MALE_GENDER_INPUT = ("css selector", "input[value='1']")
   FEMALE_GENDER_INPUT = ("css selector", "input[value='2']")

   MALE_GENDER_LABEL = ("xpath", "//label[.//input[@value='1']]")
   FEMALE_GENDER_LABEL = ("xpath", "//label[.//input[@value='2']]")
   
   DOWNLOADSPINER = ("css selector", ".oxd-loading-spinner")

   def change_name(self, new_name):
      with allure.step(f"Меняем имя пользователя на {new_name}"):
         self.wait.until(EC.invisibility_of_element_located(self.DOWNLOADSPINER))
         
         field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
         
         field.click()
         field.send_keys(Keys.CONTROL + "a")
         field.send_keys(Keys.DELETE)
         
         assert field.get_attribute("value") == "", f"Поле не очистилось: {field.get_attribute('value')}"

         field.send_keys(new_name)
         self.name = new_name
      
   @allure.step("Сохраняем изменения")
   def save_changes(self):
      self.wait.until(EC.element_to_be_clickable(self.SAVE_CHANGES_BUTTON)).click()
      
      
   @allure.step("Выбираем мужской пол")
   def select_male_gender(self):
      self.wait.until(EC.element_to_be_clickable(self.MALE_GENDER_LABEL)).click()

   @allure.step("Выбираем женский пол")
   def select_female_gender(self):
      self.wait.until(EC.element_to_be_clickable(self.FEMALE_GENDER_LABEL)).click()


   
   @allure.step("Имя успешно сохранилось")
   def is_save_changes_name(self):
            
      self.wait.until(EC.invisibility_of_element_located(self.DOWNLOADSPINER))
      self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
      self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))
      
      
   @allure.step("Изменени на мужской пол успешно сохранено")
   def is_male_selected(self):
      self.wait.until(EC.element_located_to_be_selected(self.MALE_GENDER_INPUT))

   @allure.step("Изменени на женский пол успешно сохранено")
   def is_female_selected(self):
      self.wait.until(EC.element_located_to_be_selected(self.FEMALE_GENDER_INPUT))
   
   @allure.step("Ожидание закгрузки данных")
   def wait_download(self):
      self.wait.until(EC.invisibility_of_element_located(self.DOWNLOADSPINER))
