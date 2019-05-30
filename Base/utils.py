from appium import webdriver


def get_phone_driver(package, activity):
    # server 启动参数
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'HUAWEI'
    desired_caps['automationName'] = 'Uiautomator2'
    # app的信息
    desired_caps['appPackage'] = package
    desired_caps['appActivity'] = activity
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
