from .general import *


# 这是一个较为稳健可复用的表单登陆算法，可结合Scrapy的response_fron函数一起研究
def _key_in(form_ele, key_set):
    for name_ele in form_ele.find_elements_by_xpath(".//input[@name]"):
        for name_key in key_set:
             if name_key in name_ele.get_attribute("name"):
                return name_ele


def login_form(driver):
    if not WIZ_USERNAME or not WIZ_PASSWORD:
        raise NotConfigured("请确认您为知笔记的用户名与密码配置正确！")
    for form_ele in driver.find_elements_by_class_name("form"):
        input_name_ele = _key_in(form_ele, NAME_SET)
        input_pswd_ele = _key_in(form_ele, PSWD_SET)
        if input_name_ele and input_pswd_ele:
            input_name_ele.clear()
            input_name_ele.send_keys(WIZ_USERNAME)
            input_pswd_ele.clear()
            input_pswd_ele.send_keys(WIZ_PASSWORD)
            form_ele.find_element_by_class_name("btn").click()
            return True
    raise Exception("ERROR to login!")


def save_cookie_file(driver):
    with open(COOKIE_FILE_PATH, "w", encoding="utf-8") as f:
        f.write(cookie_jar2str(driver.get_cookies()))


def driver_login(driver: webdriver.Firefox):

    any_wiz_href = wiz_pages_to_migrate[0]

    if not os.path.exists(COOKIE_FILE_PATH):
        driver.get(any_wiz_href)
        login_form(driver)
        save_cookie_file(driver)
    else:
        with open(COOKIE_FILE_PATH, "r") as f:
            s = f.read()
        # selenium启动后需要先访问一个网址，以生成domain数据，不然无法直接添加cookie
        driver.get("https://note.wiz.cn/")
        for cookie_item in cookie_str2jar(s):
            driver.add_cookie(cookie_item)

    print("Successfully logged in.")
    driver.get(any_wiz_href)
