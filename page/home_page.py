from Base.base import Base
from page.page_element import Elements


class HomePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_my(self):
        # 点击我
        self.click_element(Elements.home_go_me)


