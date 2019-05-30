import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure
import time


class Base:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10, poll_frequency=1.0):
        # 定位元素方法
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=10, poll_frequency=1.0):
        # 定位一组元素方法
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=10, poll_frequency=1.0):
        # 点击元素方法
        self.find_element(loc, timeout, poll_frequency).click()

    def input_element(self, loc, value, timeout=10, poll_frequency=1.0):
        # 输入元素
        input_box = self.find_element(loc, timeout, poll_frequency)
        input_box.clear()
        input_box.send_keys(value)

    def slide_page(self, sc=1):

        """

        :param sc: sc=1 向上滑动 sc=2向下滑动 sc=3向左  sc=4 向右
        :return:
        """
        time.sleep(3)
        page = self.driver.get_window_size()
        width = page["width"]
        height = page["height"]
        # isinstance()
        if sc == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, duration=2000)
        elif sc == 2:
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, duration=2000)
        elif sc == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, duration=2000)
        elif sc == 4:
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, duration=2000)

    def screen_page(self):
        # 截图
        pag_name = "../image" + os.sep + "{}.png".format(time.time())
        self.driver.get_screenshot_as_file(pag_name)
        with open("pag_name", "rb") as f:
            allure.attach("截图", f.read(), allure.attach.PNG)

    def get_toast(self, toast):
        error = (By.XPATH, "//*[contains(@text, '{}')]".format(toast))
        # 获取toast
        return self.find_element(error).text
