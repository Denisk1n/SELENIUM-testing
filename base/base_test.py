import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.myinfo_page import MyInfoPage
from config.data import StaticData


class TestBase:
   
   data: StaticData
   
   login_page: LoginPage
   dashboard_page: DashboardPage
   my_info_page: MyInfoPage
   
   @pytest.fixture(autouse=True)
   def setup(self, request, driver):
      request.cls.driver = driver
      request.cls.data = StaticData()
      
      request.cls.login_page = LoginPage(driver)
      request.cls.dashboard_page = DashboardPage(driver)
      request.cls.my_info_page = MyInfoPage(driver)
      