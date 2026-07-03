from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType


# общие методы для работы со страницами, в нем инициализируем драйвер для доступа ко всем страницам 
class BasePage:
   
   def __init__(self, driver):
      self.driver = driver
      # ожидаем доступа к эллементу
      self.wait = WebDriverWait(driver, 10, poll_frequency=1)
     
   MY_INFO_BUTTON_LINK = ("xpath", "//span[text()='My Info']")
   
   
   #открываем страницу  
   def open(self):
      with allure.step(f"Open {self.PAGE_URL} page"):
         self.driver.get(self.PAGE_URL)
      
   # проверяем открыта ли эта страница 
   def is_opened(self):
      with allure.step(f"Page {self.PAGE_URL} is opened"):
         self.wait.until(EC.url_to_be(self.PAGE_URL))
      
   def make_screenshot(self, screenshot_name):
      allure.attach(
         body=self.driver.get_screenshot_as_png(),
         name=screenshot_name,
         attachment_type=AttachmentType.PNG
      )