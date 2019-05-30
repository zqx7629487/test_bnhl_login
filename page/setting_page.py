from Base.base import Base
from page.page_element import Elements


class SettingPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def go_to_logout(self, tag=1):

        # 滑动
        self.slide_page()
        # 点退出登录按钮
        self.click_element(Elements.setting_logout_btn_id)
        if int(tag) == 1:
            # 点击确认退出
            self.click_element(Elements.setting_acc_quit_btn_id)
        else:
            # 点击取消退出
            self.click_element(Elements.setting_dis_quit_btn_id)
