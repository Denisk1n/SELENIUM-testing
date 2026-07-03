import random
import pytest
import allure
from base.base_test import TestBase
from config.data import StaticData


@allure.feature("Функционал изменения и сохранения данных пользователя ")
class TestChangeMyInfo(TestBase):
   
   @allure.title("Изменения имени и пола")
   @allure.severity("Critical")
   @pytest.mark.smoke
   def test_change_profile_name(self):

      self.login_page.open()
      self.login_page.enter_login(self.data.LOGIN)
      self.login_page.enter_password(self.data.PASSWORD)
      self.login_page.click_submit_button()
      
      self.dashboard_page.is_opened()
      self.dashboard_page.click_my_info_link()
      
      self.my_info_page.is_opened()
      self.my_info_page.change_name(new_name=f"Test #{random.randint(1, 100)}")
      
      self.my_info_page.select_female_gender()
      self.my_info_page.save_changes()
      
      self.my_info_page.is_save_changes_name()
      self.my_info_page.is_female_selected()
      self.my_info_page.wait_download()
      self.my_info_page.make_screenshot("Страница после изменений")
      
      
      


