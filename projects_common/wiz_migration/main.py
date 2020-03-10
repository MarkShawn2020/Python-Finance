
from core.login import *
from core.parse import *


if __name__ == '__main__':
    driver = initialize_webdriver()
    driver_login(driver)
    for wiz_page_to_migrate in wiz_pages_to_migrate:
        driver_parse(driver, wiz_page_to_migrate)

