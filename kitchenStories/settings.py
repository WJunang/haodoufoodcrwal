# Scrapy settings for kitchenStories project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'kitchenStories'
SPIDER_MODULES = ['kitchenStories.spiders']
NEWSPIDER_MODULE = 'kitchenStories.spiders'
ITEM_PIPELINES = ['kitchenStories.pipelines.KitchenstoriesPipeline']
# DEFAULT_REQUEST_HEADERS = {
#     # 'accept': 'image/webp,*/*;q=0.8',
#     # 'accept-language': 'zh-CN,zh;q=0.8',
#     # 'referer': 'https://www.taobao.com/',
#     # 'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
#     #'Charset': 'UTF-8'
#     'Charset': 'UTF-8',
#     'Accept-Encoding': 'gzip, deflate',
#     'User-Agent': 'HAODOU_RECIPE_CLIENT;(FRD-AL10;huawei_v6123;Android-6.0-23;1794x1080;113;4c97b7dc74870a0ed417d13052e87753;WIFI-)',
#     'Host':'api.haodou.com',
#     'Connection': 'close',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
#     'Content-Length': '44'
# }
#ROBOTSTXT_OBEY = True
#COOKIES_ENABLED=True
#USER_AGENT={'FRD-AL10;huawei_v6123;Android-6.0-23;1794x1080;113;4c97b7dc74870a0ed417d13052e87753;WIFI-'}
#USER_AGENT = {'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2 ',
#'Android(2.3)Browser -- Nexus S','Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
#'Mozilla/5.0 (Linux; U; Android 2.3.5; ja-jp; F-05D Build/F0001) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
#'Mozilla/5.0 (Linux; U; Android 2.3.5; ja-jp; F-05D Build/F0001) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
#'Opera/9.80 (Android 2.2;;; Linux; Opera Mobi/ADR-1012291359; U; en) Presto/2.7.60 Version/10.5',
#'Mozilla/5.0 (Linux; U; Android 4.0.1; ja-jp; Galaxy Nexus Build/ITL41D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 '
              #}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kitchenStories (+http://www.yourdomain.com)'
