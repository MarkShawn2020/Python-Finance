NAME_SET = {"name", "mail"}
PSWD_SET = {"password", "pswd"}

PAGE_LOAD_TIME = 10
SCRIPT_LOAD_TIME = 15
IMPLICIT_WAIT_TIME = 20

import os
DATA_DIR = os.path.abspath("data")
LOG_DIR = os.path.abspath("log")

GECKODRIVER_LOG_PATH = os.path.join(LOG_DIR, 'geckodriver.log')
COOKIE_FILE_PATH = os.path.join(LOG_DIR, "cookie.txt")

EDIT_MODE = "edit"
BACKTOREAD_MODE = "backtoread"


#################################################################
# 以下均是要自己修改的
#################################################################

QINIU_ACCESSS_KEY = "xxx"
QINIU_SECRET_KEY = "xxx"
QINUI_BUCKET_NAME = "xxx"

WIZ_USERNAME = "xxx@qq.com"
WIZ_PASSWORD = "Mark@xxx"

# 这是火狐驱动路径
GECKODRIVER_PATH = r'[火狐驱动]\geckodriver.exe'

# 这是火狐执行文件路径
FIREFOX_PATH= r'[火狐程序]\firefox.exe'

# 在文档内图片很多的情况下，这个对图床的开销是比较大的，慎重点
MD_IMGS_TO_UPLOAD = False
ATTACHED_FILES_TO_DOWNLOAD = False

# 先在网页端正常登陆为知笔记，然后定位到想迁移的一系列笔记那一页，输入该网址即可
# 主要是dc参数，这是每篇文档的标识，kb是每组的标识，程序的每个入口会遍历一个组的文章
# 并以此建立本地的映射路径，下载其原文件，并可根据自己情况配置图床，与文件下载
# 由于文件一般较多较大，本程序目前是单线程，后续可能会改成Scrpay版本
wiz_pages_to_migrate = [
    "https://note.wiz.cn/web/web?dc=xxx&cmd=kw%2C&kb=xxx",
]

