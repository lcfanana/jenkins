import time
import pytest
import yaml

from base.base_analyze import analyze_file
from base.driver import init_rivder
from page.page import Page





class TestConnect:
    def setup(self):
        self.driver=init_rivder()
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("args",analyze_file("contact_data.yaml","test_add_connect"))
    def test_add_connect(self,args):
        name = args["name"]
        phone=args["phone"]
        self.page.sendpage.click_add_button()
        self.page.addpage.send_name(name)
        self.page.addpage.send_phone(phone)


