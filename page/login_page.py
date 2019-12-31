import time
from common.base import Base
from selenium import webdriver
from time import sleep

# -------------定位元素信息------------ #
loc_user = ("id", "j_username")
loc_psw = ("id", "j_password")
loc_denglu = ("xpath", "//*[text()='登录']")

loc_chubanxitong = ("xpath", "//*[text()='MPen出版系统']")
loc_zhanghaohemimacuowu = ("xpath", "//*[text()='账号或密码错误']")

def login_cbxt(driver, host, username="admin", password="admin123"):
    """登录操作"""
    cbxt = Base(driver)
    driver.get(host)
    #火狐浏览器有个alert弹窗:“为了保证您的使用，请使用最新谷歌浏览器”，判断是否有弹窗，如果有点击确定
    cbxt.switch_to_Alert()

    cbxt.send_Keys(loc_user, username)
    cbxt.send_Keys(loc_psw, password)
    cbxt.click_(loc_denglu)
    time.sleep(3)

def get_result_success(driver):
    """获取登录成功后的“MPen出版系统”字样"""
    dry = Base(driver)
    result = dry.get_Text(loc_chubanxitong)
    return result

def get_result_fail(driver):
    """获取登录失败后“账号或密码错误”字样"""
    dry = Base(driver)
    result = dry.get_Text(loc_zhanghaohemimacuowu)
    return result


if __name__ == '__main__':
    driver = webdriver.Firefox()
    login_dry(driver, "https://publishdemo.mpen.com.cn/login")





