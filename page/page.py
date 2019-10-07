from page.add_page import AddPage
from page.connect_page import ConnectPage


class Page:
    def __init__(self,driver):
        self.driver=driver
    @property
    def addpage(self):
        return AddPage(self.driver)
    @property
    def sendpage(self):
        return ConnectPage(self.driver)
