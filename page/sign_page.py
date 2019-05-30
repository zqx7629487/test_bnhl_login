from Base.base import Base
from page.page_element import Elements


class SignPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_login_page(self):
        # 点击跳转登录
        self.click_element(Elements.go_to_login)
