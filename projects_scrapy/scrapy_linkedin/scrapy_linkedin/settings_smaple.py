# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_linkedin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_linkedin'

SPIDER_MODULES = ['scrapy_linkedin.spiders']
NEWSPIDER_MODULE = 'scrapy_linkedin.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent

YOUR_COOKIE = 'xxxxxxxxxxxxxxxxxxx'
YOUR_CSRF = 'XXXXXXXXXXXX'
YOUR_USER_AGENT = 'XXXXXXXXXXXX'
DEFAULT_REQUEST_HEADERS = {
    'accept': 'application/vnd.linkedin.normalized+json+2.1',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh,en-GB;q=0.9,en;q=0.8,en-US;q=0.7,zh-CN;q=0.6',
    'cookie': YOUR_COOKIE,
    'csrf-token': YOUR_CSRF,
    'user-agent': YOUR_USER_AGENT,
    'referer': 'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22cn%3A0%22%5D&origin=FACETED_SEARCH',
    'x-li-lang': 'en_US',
    'x-li-page-instance': 'urn:li:page:d_flagship3_search_srp_people;qp0ocIAZSR+pyeEZChsMZg==',
    'x-li-track': '{"clientVersion":"1.3.3190","osName":"web","timezoneOffset":8,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
    'x-restli-protocol-version': '2.0.0'
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
DOWNLOAD_DELAY = 0.2

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)


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
#    'scrapy_linkedin.middlewares.ScrapyLinkedinSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_linkedin.middlewares.ScrapyLinkedinDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scrapy_linkedin.pipelines.ScrapyLinkedinPipeline': 300,
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
