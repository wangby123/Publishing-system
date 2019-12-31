import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from common.base import Base

class yonghuguanli_page(Base):
    """添加用户、"""

    loc_yonghuguanli = ("xpath", "//*[text()='用户管理']")
    loc_chubanshezhanghao = ("xpath", "//a[text()='出版社账号']")
    loc_iframe = ("xpath", "//*[@id='layui-layer1']")
    loc_tianjia = ("xpath", "//*[@onclick='PublishUser.openAddMgr()']")
    loc_chubanshemingcheng = ("xpath", "//*[@id='trueName']")
    loc_zhanghao = ("xpath", "//*[@id='loginId']")
    loc_youxiang = ("xpath", "//*[@id='email']")
    loc_mima = ("xpath", "//*[@id='password']")
    loc_lianxiren = ("xpath", "//*[@id='linkman']")
    loc_shoujihao = ("xpath", "//*[@id='mobile']")
    loc_baocun = ("xpath", "//*[@id='ensure']")

    loc_tianjiachenggong = ("xpath", "//*[text()='添加成功!']")

    def tianjia(self):
        """添加用户"""
        # self.click_(self.loc_yonghuguanli)                      #点击用户管理
        # self.click_(self.loc_chubanshezhanghao)                 #点击出版社账号
        # self.click_(self.loc_chubanshezhanghao)                 #点击出版社账号
        time.sleep(3)

        self.driver.get(r'http://drc.mpen.com.cn/mgr/publish_user')         #打开出版社账号小窗口
        time.sleep(3)

        self.click_(self.loc_tianjia)                           #点击“添加”

        time.sleep(5)
        # iframe = self.find_Element(self.loc_iframe)            #切换iframe
        self.driver.switch_to.frame(0)

        self.send_Keys(self.loc_chubanshemingcheng, "麦片科技2")  #出版社名称输入“麦片科技”
        self.send_Keys(self.loc_zhanghao, "maipiankeji")         #账号输入“maipiankeji”
        self.send_Keys(self.loc_youxiang, "123@qq.com")          #邮箱输入“123@qq.com”
        self.send_Keys(self.loc_mima, "123456")                  #密码输入“123456”
        self.send_Keys(self.loc_lianxiren, '麦片')               #联系人输入“麦片”
        self.send_Keys(self.loc_shoujihao, "13812345678")        #手机号输入“13812345678”
        self.click_(self.loc_baocun)                             #点击保存

    def get_result(self):
        result = self.get_Text(self.loc_tianjiachenggong)
        assert result == "添加成功!"




