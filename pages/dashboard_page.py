from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure


class DashboardPage(BasePage):
   
   PAGE_URL = Links.DASHBORD_PAGE
   
   @allure.step("Click on 'My Info' link")
   def click_my_info_link(self):
      self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON_LINK)).click()