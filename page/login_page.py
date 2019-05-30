from Base.base import Base
from page.page_element import Elements


class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login_page(self, account, pwd):
        self.input_element(Elements.account_box, account)
        self.input_element(Elements.password_box, pwd)
        self.click_element(Elements.login_but)

    def login_close_page(self):
        """关闭登录页面"""
        # 点击关闭按钮
        self.click_element(Elements.login_close_page_btn_id)

    def if_login_but(self):
        self.find_element(Elements.login_but)