from core.login import *
from core.parse import *


if __name__ == '__main__':
    driver = initialize_webdriver()
    driver_login(driver)
    parse_doc(driver, "https://note.wiz.cn/web/web?dc=70c19bdc-1ed0-4784-b360-8bd493daf3f3&cmd=kw%2C&kb=9c55032e-123a-4dc4-afb4-38e654f72e0b")


