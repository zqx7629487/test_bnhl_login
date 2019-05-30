from page.home_page import HomePage
from page.login_page import LoginPage
from page.person_page import PersonPage
from page.setting_page import SettingPage
from page.sign_page import SignPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    def home_page(self):
        # 主页
        return HomePage(self.driver)

    def login_page(self):
        # 选择登录
        return LoginPage(self.driver)

    def sign_page(self):
        # 输入账号
        return SignPage(self.driver)

    def person_page(self):
        # 个人页面
        return PersonPage(self.driver)

    def setting_page(self):
        # 设置页面
        return SettingPage(self.driver)
