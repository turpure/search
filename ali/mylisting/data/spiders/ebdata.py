# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.selector import Selector
from data.items import ListingItem
import re
import scrapy


class ebaydataSpider(CrawlSpider):
    download_delay = 1
    name="listing"
    allowed_domains=['aliexpress.com']
    start_urls=['http://www.aliexpress.com/wholesale? \
                catId=0&initiative_id=AS_20150523233307 \
                &SearchText=silicone+mould+',
                ]
    rules = [
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="history-item product "]')),'myparse'),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="page-next ui-pagination-next"]'))),
            #Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="ui-pagination-next"]')),'myparse')
            ]

    def myparse(self,response):
        item=ListingItem()

        listing4=response.xpath('//h1[@itemprop="name"]/text()').extract()
        item['title']=listing4
        listings=response.xpath('//span[@class="orders-count"]/b/text()').extract()   #div[1]/table/tbody/tr[1]

        item['orders']=listings
        listing1=response.xpath('//a[@class="store-lnk"]/text()').extract()
        item['seller']=listing1
        listing2=response.xpath('//address/text()').extract()
        item['address']=listing2[0][2:]
        listing3=response.xpath('//span[@itemprop="price"]/text()').extract()
        item['price']=listing3


        item['url']=response.url
        yield item
