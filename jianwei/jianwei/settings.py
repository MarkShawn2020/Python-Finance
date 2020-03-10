# -*- coding: utf-8 -*-

# Scrapy settings for jianwei project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html


"""
-------------------------------------------------------
以下是见微数据的个人登陆信息，请确保填写正确，必填
-------------------------------------------------------
"""

LOGIN_UID = 'your username'  # 账户名、手机号或者邮箱

LOGIN_PWD = 'your password'  # 密码


"""
--------------------------------------------------------
以下是将搜集的数据导出到CSV（可以用Excel打开）的设置
注意：程序导出的CSV如出现中文乱码现象，应使用NotePad或者Sublime
等软件，打开将其转为UTF-8 BOM格式编码，再用Excel打开。
默认目录为该工程项目地址 jianwei 文件夹，可修改
--------------------------------------------------------
"""

FEED_FORMAT = 'csv'
FEED_URI = './files/data.csv'
FEED_EXPORT_ENCODING = 'utf-8'

'''
--------------------------------------------------------
以下是将搜集的数据导出到MongoDB的设置，无需修改
--------------------------------------------------------
'''

ITEM_PIPELINES = {
    'jianwei.pipelines.MongoPipeline': 30,
}

MONGO_CLIENT = 'localhost'

MONGO_URI = 27017

MONGO_DB = 'jianwei'

DOWNLOAD_DELAY = 5  # 防止被封上限


'''
--------------------------------------------------------------
'''


BOT_NAME = 'jianwei'

SPIDER_MODULES = ['jianwei.spiders']

NEWSPIDER_MODULE = 'jianwei.spiders'

ROBOTSTXT_OBEY = False

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'

LOG_LEVEL = 'INFO'




# LOG_FORMAT = '%(levelname)s: %(message)s'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'jianwei (+http://www.yourdomain.com)'





# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jianwei.middlewares.JianweiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jianwei.middlewares.JianweiDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jianwei.pipelines.JianweiPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
