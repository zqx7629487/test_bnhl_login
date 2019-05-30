
import pytest
from selenium.common.exceptions import TimeoutException

from Base.get_file_data import data
from Base.utils import get_phone_driver
from page.page import Page


def get_login_data():
    # 预期成功列表
    suc_list = []
    # 预期失败列表
    fail_list = []

    data_list = data("login.yaml")
    for i in data_list.values():
        if i.get("toast"):
            fail_list.append((i.get("account"), i.get("passwd"),
                              i.get("toast"), i.get("expect_data")))
        else:
            suc_list.append((i.get("account"), i.get("passwd"),
                             i.get("expect_data")))
    data_dict = {"suc": suc_list, "fail": fail_list}
    print(data_dict)
    return data_dict


class TestLogin(object):

    def setup_class(self):
        self.driver = get_phone_driver("com.yunmall.lc",
                                       "com.yunmall.ymctoc.ui.activity.MainActivity")
        self.page = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def auto_in_login(self):
        # 主页点击我
        self.page.home_page().click_my()
        # 点击已注册账户登录
        self.page.sign_page().click_login_page()

    @pytest.mark.parametrize("account,pwd,expect_data", get_login_data().get("suc"))
    def test_login(self, account, pwd, expect_data):
        # # 主页点击我
        # self.page.home_page().click_my()
        # # 点击已注册账户登录
        # self.page.sign_page().click_login_page()

        # 输入登录信息
        self.page.login_page().login_page(account, pwd)
        # 判断登录与否
        try:
            # 获取我的优惠
            shop_cart = self.page.person_page().get_shop_cart()
            try:
                assert shop_cart == expect_data
            except AssertionError:
                # 截图并创建allure
                self.page.person_page().screen_page()
                assert False
            finally:
                # 点击设置按钮
                self.page.person_page().click_setting()
                # 退出账号
                self.page.setting_page().go_to_logout()
        except TimeoutException:
            # 截图并创建allure
            self.page.person_page().screen_page()
            # 返回首页
            self.page.login_page().login_close_page()
            assert False

    @pytest.mark.parametrize("account,pwd,expect_data,toast", get_login_data().get("fail"))
    def test_login_is_no(self, account, pwd, expect_data, toast):
        # # 主页点击我
        # self.page.home_page().click_my()
        # # 点击已注册账户登录
        # self.page.sign_page().click_login_page()

        # 输入登录信息
        self.page.login_page().login_page(account, pwd)
        # 判断登录与否
        try:
            # 判断toast消息
            # 截图 查看toast消息
            self.page.person_page().screen_page()
            toast_test = self.page.person_page().get_toast(toast)
            # print("toast:{},expect_toast{}".format(toast, toast_test))
            try:
                # 判断登录按钮
                self.page.login_page().if_login_but()

                assert toast_test == toast
                # 放回首页
                self.page.setting_page().go_to_logout()

            except TimeoutException:
                # 截图并创建allure
                self.page.person_page().screen_page()
                # # 点击设置按钮
                self.page.person_page().click_setting()
                # 退出账号
                self.page.setting_page().go_to_logout()
                assert False

            except AssertionError:
                # 截图并创建allure
                self.page.person_page().screen_page()
                # 返回首页
                self.page.login_page().login_close_page()
                assert False

        except TimeoutException:
            # 截图并创建allure
            self.page.person_page().screen_page()
            try:
                # 判断登录按钮
                self.page.login_page().if_login_but()
                # 返回首页
                self.page.login_page().login_close_page()

            except TimeoutException:
                # # 点击设置按钮
                self.page.person_page().click_setting()
                # 退出账号
                self.page.setting_page().go_to_logout()
            assert False
        # # 点击设置按钮
        # self.page.person_page().click_setting()
        # # 退出账号
        # self.page.setting_page().go_to_logout()
