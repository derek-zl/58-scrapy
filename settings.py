# -*- coding: utf-8 -*-

# Scrapy settings for get_all project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'get_all'

SPIDER_MODULES = ['get_all.spiders']
NEWSPIDER_MODULE = 'get_all.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = '	Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
COOKIES={'c_citydomain': 'xa', 'cookieuid': '634eaf04-cedb-4960-8292-ebd13c22ac1a', '__utmz': '253535702.1491394232.1.1.utmcsr', 'nearCity': '%5B%7B%22cityName%22%3A%22%E8%A5%BF%E5%AE%89%22%2C%22city%22%3A%22xa%22%7D%2C%7B%22cityName%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22city%22%3A%22bj%22%7D%5D', 'gr_session_id_b4113ecf7096b7d6': '70c495e9-0b95-46d3-a9e5-1d09ccbb5c5a', 'spm': '', 'als': '0', 'Hm_lvt_5a7a7bfd6e7dfd9438b9023d5a6a4a96': '1491456899,1491556820,1491793117,1491959523', 'mcityName': '%E5%8C%97%E4%BA%AC', 'city': 'gz', 'dm_uuid': '8311f3d2-1d99-11e7-8584-1418774d6214', 'bj58_id58s': '"ZFpGdkwxZkp3MnlKOTk1OA', 'time_create': '1494638517232', 'Hm_lpvt_5bcc464efd3454091cf2095d3515ea05': '1492046710', '58home': 'bj', 'JSESSIONID': 'E97A6CD6FFE65FC4AB9FD19CF61BB94E', 'new_session': '0', 'gr_user_id': '643c4ecc-ee6f-4efe-9d29-ac00a753ac65', 'dm_fm': '58_58m_lbpost', 'new_uv': '46', 'job_detail_show_time': '2', 'id58': 'c5/njVjQx4uIk5ByA3ppAg', '58app_hide': '1', 'Hm_lvt_3bb04d7a4ca3846dcc66a99c3e861511': '1490077586', 'Hm_lvt_5bcc464efd3454091cf2095d3515ea05': '1491959514,1492046516,1492046537', 'Hm_lvt_e15962162366a86a6229038443847be7': '1490077586', '_ga': 'GA1.2.889643149.1490077588', 'mcity': 'bj', 'utm_source': '', 'commonTopbar_myfeet_tooltip': 'end', 'ipcity': 'xa%7C%u897F%u5B89%7C0', 'sessionid': 'd1fa33f3-1cc0-48c7-90a3-cff48bc68372', '58tj_uuid': '422ba9d3-2d84-49ce-9f47-45e95210c0b3', 'bangbigtip2': '1', '__utma': '253535702.889643149.1490077588.1491394232.1491394232.1', 'commontopbar_city': '3%7C%u5E7F%u5DDE%7Cgz', 'UM_distinctid': '15b45f123be30a-020ed4ea5600d58-4c332c7e-100200-15b45f123bf3f9', 'bj58_new_uv': '31', 'f': 'n', 'userid360_xml': '41A241D27F21FB155E9F660E00AEE766', 'abtest': '"zp_zhuzhan_pc_detail_template', 'myfeet_tooltip': 'end', 'scancat': '13907%2C23196%2C13909%2C38676%2C13918', 'ganji_jz_ca_source': 'eyJpdiI6IkxiWHdqalJXS0RmNzdQSXhDNCtIZXc9PSIsInZhbHVlIjoienhnVWtYUkFYRTEyK2pLMHZVeStnSEJ2XC94bGZ1MHlkTU10d05BbXhOaWs9IiwibWFjIjoiNWJmYjQ0ZWFhMjdmYmE0NTVkNjdjNDM4MjI4ZTVjOWRiZmYxNWI0OTM4MWVkOWJhZDE4MDc1OGY1MjZlMjQzZSJ9', 'm58comvp': 't12v115.159.229.17', 'final_history': '29028971144391%2C23918741932860%2C29019004344769%2C27548943485750%2C23910038825529', 'doumi_melon': 'eyJpdiI6IkhQdjd2V0FKT2IxUmptT2kxME5Fb1E9PSIsInZhbHVlIjoiZFwvNjVBczAxSTUzVGJUT0Vwa3JoWlZUZFBYZDZXM2ZjY1hTWFNqSzkwa2lLNW83bExLazVMcVV4UTZZeFN5XC9tVklKY3gyWWRNTlgzRmlMSCtzN2lwZz09IiwibWFjIjoiY2RkODUxYzFjMGM0MjU5OTVmNDYyY2E2ZGIxMjEyMDZhNDcxMjE1MmI0NjYxMmY4ZWEwOGQ4NmZmZDEwZTg2NiJ9', 'init_refer': 'http%253A%252F%252Fcallback.58.com%252Ffirewall%252Fvalid%252F22057284.do%253Fnamespace%253Dm.58.com%2526url%253Dhttp%25253A%25252F%25252Fm.58.com%25252Fgz%25252Ftongjiyuan%25252Fpn1%25252F%25253Freform%25253Dpcfront%252526PGTID%25253D0d202408-0000-3f66-998c-8a672d927892%252526ClickID%25253D1%252526segment%25253Dtrue'}
RANDOMIZE_DOWNLOAD_DELAY = True
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
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'get_all.middlewares.GetAllSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html


# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'get_all.pipelines.GetAllPipeline': 300,
    'get_all.pipelines.MySQLStorePipeline':300,
}



# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MYSQL_HOST='localhost'
MYSQL_DBNAME='58data'
MYSQL_USER='root'
MYSQL_PASSWD='12341234'


