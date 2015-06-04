# -*- coding: utf-8 -*-

# Scrapy settings for data project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'data'

SPIDER_MODULES = ['data.spiders']
NEWSPIDER_MODULE = 'data.spiders'
ITEM_PIPELINES = ['data.pipelines.MySQLStorePipeline']
COOKIES_ENABLES=False
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'data.spiders.rotate_useragent.RotateUserAgentMiddleware' :400
    }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'data (+http://www.yourdomain.com)'
