from selenium.webdriver.common.by import By
import allure
from base.action import BaseAction


class ConnectPage(BaseAction):
    add_button=By.ID,"com.android.contacts:id/floating_action_button"
    @allure.step(title="点击添加按钮")
    def click_add_button(self):
        self.click(self.add_button)
