import pytest
from page.login_page import login_cbxt, get_result_success, get_result_fail
from time import sleep
from common.base import Base

class Test_Login():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver, host):
        """每个用例都执行的前置操作和后置操作"""
        print("----------用例开始,打开首页----------")
        pass

        yield
        print("----------用例结束清除cookie，刷新页面----------\n")
        driver.delete_all_cookies()
        sleep(3)

    def test_01(self, driver, host):
        """输入正确的账号和密码，登录成功"""
        login_cbxt(driver, host)
        result = get_result_success(driver)
        assert result == "MPen出版系统"

    def test_02(self, driver, host):
        """输入正确的用户名和错误的密码，登陆失败"""
        login_cbxt(driver, host, username="admin", password="admin")
        result = get_result_fail(driver)
        assert result == "账号或密码错误"
