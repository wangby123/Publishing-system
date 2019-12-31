from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

"""
    locator中的定位方法
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
"""

class Base():
    """selenium的二次封装"""

    def __init__(self,driver):
        self.driver = driver
        self.timeout = 20
        self.t = 0.5

    def find_Element(self, locator):
        """定位元素(单数方法)"""
        if not isinstance(locator, tuple):     #isinstance函数判断locator对象是否是元祖类型
            print("locator参数类型错误，请传入元祖类型")
        else:
            print("正在定位元素：定位方式->%s, 值->%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))    #*locator将两个参数依次传入
            return ele

    def find_Elements(self, locator):
        """定位元素（复数方法）,返回一个list对象，如果没有定位到返回空列表[]"""
        if not isinstance(locator, tuple):     #isinstance函数判断locator对象是否是元祖类型
            print("locator必须传元祖类型")
        else:
            print("正在定位元素：定位方式：%s, 值：%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))    #*locator将两个参数依次传入
            return ele
            
    def click_(self, locator):
        """单击操作"""
        ele = self.find_Element(locator)
        ele.click()

    def send_Keys(self, locator, text):
        """send_keys输入操作"""
        ele = self.find_Element(locator)
        ele.send_keys(text)

    def clear_(self, locator):
        """文本框清除操作"""
        ele = self.find_Element(locator)
        ele.clear()

    def move_to_Element(self, locator):
        """鼠标悬停"""
        ele = self.find_Element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def select_by_Index(self, locator, index):
        """通过索引选择下拉框选项，从0开始，索引不用加"",选项是option的下拉框才能用"""
        ele = self.find_Element(locator)
        Select(ele).select_by_index(index)
        ele.click()

    def select_by_Value(self, locator, value):
        """通过value值选择下拉框选项，从0开始，value要加"",选项是option的下拉框才能用"""
        ele = self.find_Element(locator)
        Select(ele).select_by_value(value)
        ele.click()

    def select_by_visible_Text(self, locator, text):
        """通过text选择下拉框选项，从0开始，选项是option的下拉框才能用"""
        ele = self.find_Element(locator)
        Select(ele).select_by_visible_text(text)
        ele.click()

    def switch_to_Frame(self, id_index_locator):
        """切换frame"""
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.find_Element(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
             print("iframe切换异常")

    def switch_to_default_content(self):
        """从iframe回到主页面"""
        self.driver.switch_to.default_content()

    def switch_to_parent_frame(self):
        """从iframe返回上一级"""
        self.driver.switch_to.parent_frame()

    def switch_to_Window(self, handle_name):
        """切换窗口"""
        self.driver.switch_to.window(handle_name)

    def switch_to_Alert(self):
        """切换到alert弹窗"""
        r = self.alert_is_Present()
        if not r:
            print("没有alert弹窗")
        else:
            print("切换到alert弹窗成功")
            r.accept()
            
    def js_focus_element(self, locator):
        """聚焦元素"""
        ele = self.find_Element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        """滚动到底补"""
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        
    def js_click_id(self, id):
        """js解决click失效问题,根据id定位"""
        js = "document.getElementById(%s).click" % (id)
        self.driver.execute_script(js)
        
    def js_click_name(self, name, value):
        """js解决click失效问题,根据name定位"""
        js = "document.getElementsByName(%s)[%d].click" % (name, value)
        self.driver.execute_script(js)
        
    def js_click_classname(self, classname, value):
        """js解决click失效问题,根据classname定位"""
        js = "document.getElementsByClassName(%s)[%d].click" % (classname, value)
        self.driver.execute_script(js)
        
    def js_click_tagname(self, tagname, value):
        """js解决click失效问题,根据tagname定位"""
        js = "document.getElementsByTagName(%s)[%d].click" % (tagname, value)
        self.driver.execute_script(js)




    #----------------------------------------EC模块常用判断方法开始----------------------------------------
    #EC模块判断在page里面封装实际结果是直接返回bool，用例里面判断判断世界结果=True或=False即可
    def title_Is(self, title):
        """判断title完全相同,返回bool"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    def title_Contains(self, title):
        """判断实际title包含预期title,返回bool"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False


    def text_to_be_present_in_Element(self, locator, text):
        """判断元素的text与预期结果是否一致,返回bool值，元素定位出错了不会报错，只会返回False"""
        if  not isinstance(locator, tuple):     #isinstance函数判断locator对象是否是元祖类型
            print("locator必须传元祖类型")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def text_to_be_present_in_element_Value(self, locator, value):
        """判断元素的value与预期结果是否一致,返回bool值，元素定位出错了不会报错，只会返回False"""
        if not isinstance(locator, tuple):
            print("locator必须传元祖类型")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def alert_is_Present(self):
        """判断是否有弹窗，存在返回alert实例，不存在，返回false"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False
    #----------------------------------------EC模块常用判断方法结束----------------------------------------
    
    
    
    
    #----------------------------------------获取断言信息开始----------------------------------------
    def get_Title(self):
        """获取title(网页最上面的标题)"""
        return self.driver.title

    def get_Text(self, locator):
        """获取text,获取到返回text，没有获取到返回空值"""
        try:
            ele = self.find_Element(locator)
            print("获取到了元素的text，返回元素的text")
            return ele.text
        except:
            print("没有获取到text，返回空值")
            return ""

    def get_Attribute(self, locator, name):
        """获取元素的属性值,获取到返回属性值，没有获取到返回空值，属性名name需要加''"""
        try:
            ele = self.find_Element(locator)
            return ele.get_attribute(name)
        except:
            print("没有获取到元素的属性值，返回空值")
            return ""
    #----------------------------------------获取断言信息结束----------------------------------------
    
    
    
    
    #----------------------------------------判断元素开始----------------------------------------
    def is_Display(self, locator):
        """判断元素是可见还是隐藏,返回bool值
        注意：隐藏的元素可以定位到，但是在页面上不能操作
        """
        try:
            ele = self.find_Element(locator)
        except:
            print("定位的元素不存在,请输入存在的元素")
        else:
            result = ele.is_displayed()
            return result
            
    def is_Selected(self, locator):
        """判断下拉框、单选框、复选框等是否被选中,返回bool值"""
        ele = self.find_Element(locator)
        result = ele.is_selected()
        return result
            
    def is_element_Exist(self, locator):
        """判断元素是否存在,返回bool值"""
        try:
            self.find_Element(locator)
            return True
        except:
            print("元素不存在，返回False")
            return False

    def is_elements_Exist(self, locator):
        """复数定位判断元素是否存在,存在返回True，不存在就是一个空列表，返回False"""
        ele = self.find_Elements(locator)
        numbers = len(ele)
        if numbers == 0:
            print("元素不存在，返回False")
            return False
        else:
            print("定位到了%s个元素对象" % numbers)
            return True
    #----------------------------------------判断元素结束----------------------------------------
    



    
        


if __name__ == '__main__':
    driver = webdriver.Firefox()
    url = r"https://www.qq.com"
    driver.get(url)

    sleep(5)
    a = Base(driver)
    a.js_scroll_end()
    sleep(3)
    a.js_scroll_top()
    sleep(3)

    loc_nba = ("xpath", "html/body/div[1]/div[8]/div[1]/div[3]/div[1]/a")
    a.js_focus_element(loc_nba)
    sleep(3)

    # baidu = Base(driver)
    # loc1 = ("xpath", "//*[@id='u1']/a[8]")
    # loc2 = ("xpath", "//*[@id='wrapper']/div[6]/a[1]")
    # loc3 = ("xpath", "//*[@id='nr']")
    #
    # baidu.move_to_Element(loc1)
    # sleep(1)
    # baidu.click_(loc2)
    # sleep(2)
    # baidu.select_by_Value(loc3, "50")
    # sleep(4)




    driver.quit()






