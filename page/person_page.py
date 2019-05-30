from Base.base import Base
from page.page_element import Elements


class PersonPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_shop_cart(self):
        """获取优惠券文本内容"""
        return self.find_element(Elements.person_shop_cart_id).text

    def click_setting(self):
        self.click_element(Elements.person_setting_btn_id)
