# -*- coding: utf-8 -*-

# Scrapy settings for maoyanmovie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyanmovie'

SPIDER_MODULES = ['maoyanmovie.spiders']
NEWSPIDER_MODULE = 'maoyanmovie.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'maoyanmovie (+http://www.yourdomain.com)'
# USER_AGENT_LIST=[
# 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
# ]
# import random
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Pragma": "no-cache",
    "Host": "maoyan.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    'Cookie': '__mta=121074487.1593314012121.1593327622093.1593331768016.21; uuid_n_v=v1; uuid=58388340B8ED11EAB4E28FB161D5B82B53B517EE1BF14DA38E44381DC9DDCC66; _csrf=20c3b79955c0d420076677477ff00096ebae2c77a7f0f4353a31719c7a7dee50; _lxsdk_cuid=172f8ea6aa1c8-0d64eceef87b8d-f7d123e-e1000-172f8ea6aa1c8; _lxsdk=58388340B8ED11EAB4E28FB161D5B82B53B517EE1BF14DA38E44381DC9DDCC66; mojo-uuid=1179dfe44c63d65f6d826d03a3bca20d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593325783,1593327399,1593334552,1593346306; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593430641; __mta=121074487.1593314012121.1593331768016.1593430641372.22; _lxsdk_s=17309bbb625-ffc-19c-6c1%7C%7C1'
}
# DEFAULT_REQUEST_HEADERS = {
#   'Cookie': '__mta=121074487.1593314012121.1593327622093.1593331768016.21; uuid_n_v=v1; uuid=58388340B8ED11EAB4E28FB161D5B82B53B517EE1BF14DA38E44381DC9DDCC66; _csrf=20c3b79955c0d420076677477ff00096ebae2c77a7f0f4353a31719c7a7dee50; _lxsdk_cuid=172f8ea6aa1c8-0d64eceef87b8d-f7d123e-e1000-172f8ea6aa1c8; _lxsdk=58388340B8ED11EAB4E28FB161D5B82B53B517EE1BF14DA38E44381DC9DDCC66; mojo-uuid=1179dfe44c63d65f6d826d03a3bca20d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593325783,1593327399,1593334552,1593346306; mojo-session-id={"id":"cb5c7539a953ec846a8872ec79965aa2","time":1593354888119}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593354888; __mta=121074487.1593314012121.1593331768016.1593354888217.22; _lxsdk_s=172fb5a1067-2b8-fa2-10%7C%7C3',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyanmovie.middlewares.MaoyanmovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'maoyanmovie.middlewares.MaoyanmovieDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'maoyanmovie.pipelines.MaoyanmoviePipeline': 300,
#}
ITEM_PIPELINES = {
    'maoyanmovie.pipelines.MaoyanmoviePipeline': 300,
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
