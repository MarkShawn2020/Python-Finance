from .settings import *
from core import webdriver, EC, By, Keys, WebDriverWait, os, re, requests, time

class NotConfigured(Exception):
    pass


def cookie_jar2str(cookie_dict: dict):
    kv_pair_str_list = list("%s=%s;" % (item["name"], item["value"]) for item in cookie_dict)
    return "".join(kv_pair_str_list)


def cookie_str2jar(cookie_str: str):
    import re
    cooie_jar = []
    for name, value in re.findall(r'(.*?)=(.*?);', cookie_str):
        cooie_jar.append({"name": name, "value": value})
    return cooie_jar




class ProgressBar(object):

    def __init__(self, title,
                 count=0.0,
                 run_status=None,
                 fin_status=None,
                 total=100.0,
                 unit='', sep='/',
                 chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "【%s】%s %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.status)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        # 【名称】状态 进度 单位 分割线 总数 单位
        _info = self.info % (self.title, self.status,
                             self.count / self.chunk_size, self.unit, self.seq, self.total / self.chunk_size, self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)


def wait_element(driver: webdriver.Firefox, func, wait_time=10):
    element = WebDriverWait(driver, wait_time).until(func)
    return element


def initialize_webdriver() -> webdriver.Firefox:
    try:
        driver = webdriver.Firefox(
            executable_path=GECKODRIVER_PATH,
            firefox_binary=FIREFOX_PATH,
            service_log_path=GECKODRIVER_LOG_PATH
        )
    except Exception as e:
        print(e)
        raise NotConfigured("请确认浏览器执行程序与驱动位置正确！")

    from win32api import GetSystemMetrics

    driver.set_window_position(GetSystemMetrics(0) / 2, 0)
    driver.set_window_size(GetSystemMetrics(0) / 2, GetSystemMetrics(1))

    driver.set_page_load_timeout(PAGE_LOAD_TIME)
    driver.set_script_timeout(SCRIPT_LOAD_TIME)
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)

    return driver