from selenium import webdriver
from datetime import datetime
from py._xmlgen import html
import pytest

_driver = None

def pytest_addoption(parser):
    """添加命令行参数--browser和--host,设置默认测试环境地址"""
    parser.addoption("--browser", action="store", default="firefox", help="browser option:firefox or chrome")
    parser.addoption("--host", action="store", default="https://publishdemo.mpen.com.cn/login", help="https://publishdemo.mpen.com.cn/login")

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """测试失败时自动截图，展示到html报告中"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """插入Description和Test_nodeid列，删除原来的Test列"""
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    """Description列添加详情和Test_nodeid添加详情，删除原有的Test列"""
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)

def _capture_screenshot():
    """截图保存为base64"""
    return _driver.get_screenshot_as_base64()


@pytest.fixture(scope='session')
def driver(request):
    """定义全局driver参数"""

    global _driver

    if _driver is None:
        name = request.config.getoption("--browser")   #获取浏览器名称
        if name == "firefox":
            _driver = webdriver.Firefox()
        elif name == "chrome":
            _driver = webdriver.Chrome()
        else:
            _driver = webdriver.Chrome()
        print("正在启动%s浏览器" % name)

    def fn():
        print("所有用例都执行完了^^")
        _driver.quit()
    request.addfinalizer(fn)
    return _driver

@pytest.fixture(scope='session')
def host(request):
    """全局host参数"""
    return request.config.getoption("--host")


