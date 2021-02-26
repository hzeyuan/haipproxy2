from scrapy.utils.project import get_project_settings


settings = get_project_settings()

"""
Settings for global.
"""
#####################################################################
# Scrapy settings of this project
#####################################################################
# scrapy basic info
BOT_NAME = 'haiproxy'
SPIDER_MODULES = ['haipproxy2.crawler.spiders', 'haipproxy2.crawler.validators']
NEWSPIDER_MODULE = 'haipproxy2.crawler'

# downloader settings
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
DOWNLOAD_TIMEOUT = 30

# to aviod infinite recursion
DEPTH_LIMIT = 100
CONCURRENT_REQUESTS = 50

# don't filter anything, also can set dont_filter=True in Request objects
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'
HTTPCACHE_ENABLED = False
GFW_PROXY = settings.get('GFW_PROXY','http://127.0.0.1:8123')

# splash settings.If you use docker-compose,SPLASH_URL = 'http://splash:8050'
SPLASH_URL = 'http://127.0.0.1:8050'

# extension settings
RETRY_ENABLED = False
TELNETCONSOLE_ENABLED = False


UserAgentMiddleware = 'haipproxy2.crawler.middlewares.UserAgentMiddleware'
ProxyMiddleware = 'haipproxy2.crawler.middlewares.ProxyMiddleware'
DOWNLOADER_MIDDLEWARES = {
    UserAgentMiddleware: 543,
    ProxyMiddleware: 543,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    # it should be prior to HttpProxyMiddleware
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# scrapy log settings
LOG_LEVEL = 'DEBUG'
# LOG_FILE = 'logs/haipproxy2.log'


#####################################################################
# Custom settings of this project
#####################################################################

# redis settings.If you use docker-compose, REDIS_HOST = 'redis'
# if some value is empty, set like this: key = ''
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = '123456'
REDIS_DB = 3

# scheduler settings
TIMER_RECORDER = 'haipproxy2:scheduler:task'
LOCKER_PREFIX = 'haipproxy2:lock:'

# proxies crawler's settings
SPIDER_FEED_SIZE = 10
SPIDER_COMMON_TASK = 'haipproxy2:spider:common'
SPIDER_AJAX_TASK = 'haipproxy2:spider:ajax'
SPIDER_GFW_TASK = 'haipproxy2:spider:gfw'
SPIDER_AJAX_GFW_TASK = 'haipproxy2:spider:ajax_gfw'

# data_all is a set , it's a dupefilter
DATA_ALL = 'haipproxy2:all'

# the data flow is init queue->validated_queue->validator_queue(temp)->validated_queue(score queue)->
# ttl_queue, speed_qeuue -> clients
# http_queue is a list, it's used to store initially http/https proxy resourecs
INIT_HTTP_QUEUE = 'haipproxy2:init:http'

# socks proxy resources container
INIT_SOCKS4_QUEUE = 'haipproxy2:init:socks4'
INIT_SOCKS5_QUEUE = 'haipproxy2:init:socks5'

# custom validator settings
VALIDATOR_FEED_SIZE = 50

# they are temp sets, come from init queue, in order to filter transparnt ip
TEMP_HTTP_QUEUE = 'haipproxy2:http:temp'
TEMP_HTTPS_QUEUE = 'haipproxy2:https:temp'
TEMP_WEIBO_QUEUE = 'haipproxy2:weibo:temp'
TEMP_ZHIHU_QUEUE = 'haipproxy2:zhihu:temp'

# valited queues are zsets.squid and other clients fetch ip resources from them.
VALIDATED_HTTP_QUEUE = 'haipproxy2:validated:http'
VALIDATED_HTTPS_QUEUE = 'haipproxy2:validated:https'
VALIDATED_WEIBO_QUEUE = 'haipproxy2:validated:weibo'
VALIDATED_ZHIHU_QUEUE = 'haipproxy2:validated:zhihu'

# time to live of proxy ip resources
TTL_VALIDATED_RESOURCE = 2  # minutes
TTL_HTTP_QUEUE = 'haipproxy2:ttl:http'
TTL_HTTPS_QUEUE = 'haipproxy2:ttl:https'
TTL_WEIBO_QUEUE = 'haipproxy2:ttl:weibo'
TTL_ZHIHU_QUEUE = 'haipproxy2:ttl:zhihu'

# queue for proxy speed
SPEED_HTTP_QUEUE = 'haipproxy2:speed:http'
SPEED_HTTPS_QUEUE = 'haipproxy2:speed:https'
SPEED_WEIBO_QUEUE = 'haipproxy2:speed:weibo'
SPEED_ZHIHU_QUEUE = 'haipproxy2:speed:zhihu'

# squid settings on linux os
# execute sudo chown -R $USER /etc/squid/ and
# sudo chown -R $USER /var/log/squid/cache.log at first
SQUID_BIN_PATH = '/usr/sbin/squid'  # mac os '/usr/local/sbin/squid'
SQUID_CONF_PATH = '/etc/squid/squid.conf'  # mac os '/usr/local/etc/squid.conf'
SQUID_TEMPLATE_PATH = '/etc/squid/squid.conf.backup'  # mac os /usr/local/etc/squid.conf.backup

# client settings

# client picks proxies which's response time is between 0 and LONGEST_RESPONSE_TIME seconds
LONGEST_RESPONSE_TIME = 10

# client picks proxies which's score is not less than LOWEST_SCORE
LOWEST_SCORE = settings.get('LOWEST_SCORE',6)

# if the total num of proxies fetched is less than LOWES_TOTAL_PROXIES, haipproxy2 will fetch more
# more proxies with lower quality
LOWEST_TOTAL_PROXIES = 5
# if config
ORIGIN_IP = settings.get('ORIGIN_IP','')

#####################################################################
# monitor and bug trace
#####################################################################

# sentry for error tracking, for more information see
# https://github.com/getsentry/sentry
# disable it by setting USE_SENTRY = False
USE_SENTRY = True
SENTRY_DSN = 'http://009f7f5f50794deeb24791a39b86f254:56a9a5f5d3fc42a18bf87aa4341f8f3f@127.0.0.1:9000/2'

# prometheus for monitoring, for more information see
# https://github.com/prometheus/prometheus
# disable it by setting use_prom = False
USE_PROM = False
EXPORTER_LISTEN_HOST = '0.0.0.0'
EXPORTER_LISTEN_PORT = 8000