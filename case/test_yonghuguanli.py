from page.yonghuguanli_page import yonghuguanli_page
import pytest

class Test_yonghuguanli():

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver, host):
        """每个用例都执行的前置操作和后置操作"""
        print("----------用例开始,打开首页----------")
        self.dry = yonghuguanli_page(driver)

        yield
        print("----------用例结束清除cookie，刷新页面----------\n")
        driver.refresh()

    @pytest.mark.usefixtures("login")
    def test_01(self):
        """添加用户成功"""
        self.dry.tianjia()
        result = self.dry.get_result()
        assert result == "添加成功!"
