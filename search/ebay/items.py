# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EbayItem(scrapy.Item):
    # define the fields for your item here like:
    sellersid=scrapy.Field()
    location=scrapy.Field()
    itemnumber=scrapy.Field()
    title = scrapy.Field()
    sales=scrapy.Field()
    price=scrapy.Field()
    shipping=scrapy.Field()
    url=scrapy.Field()
     
    
   
