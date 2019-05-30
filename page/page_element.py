from selenium.webdriver.common.by import By


class Elements:
    """管理所有页面元素"""

    """首页"""
    # 我的按钮
    home_go_me = (By.ID, "com.yunmall.lc:id/tab_me")

    """注册页面"""
    # 登录按钮
    go_to_login = (By.ID, "com.yunmall.lc:id/gotologon")

    """登录页面"""
    # 账号输入框
    account_box = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    # 密码输入框
    password_box = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    # 登录按钮
    login_but = (By.ID, "com.yunmall.lc:id/logon_button")
    # 关闭登录页面按钮
    login_close_page_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """个人中心页面"""
    # 我的优惠券
    person_shop_cart_id = (By.ID, "com.yunmall.lc:id/txt_my_coupons")
    # 设置按钮
    person_setting_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
    """设置页面"""

    # 退出按钮
    setting_logout_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
    # 弹窗 确认退出按钮
    setting_acc_quit_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
    # 弹窗 取消退出按钮
    setting_dis_quit_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")
