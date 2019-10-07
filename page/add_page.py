import allure
from selenium.webdriver.common.by import By

from base.action import BaseAction



class AddPage(BaseAction):
    name=By.XPATH,"//*[@text='姓名']"
    phone=By.XPATH,"//*[@text='电话']"
    @allure.step(title="输入姓名")
    def send_name(self,n):
        allure.attach("姓名",n,allure.attach_type.TEXT)
        self.input(self.name,n)
        # allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    @allure.step(title="输入手机号")
    def send_phone(self,p):
        allure.attach("手机号", p, allure.attach_type.TEXT)
        self.input(self.phone,p)
        # allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)