# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ListingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     
      
      sellerid= scrapy.Field()
      location= scrapy.Field()
      itemnumber= scrapy.Field()
      category = scrapy.Field()
      title= scrapy.Field()
      price = scrapy.Field()
      shipping= scrapy.Field()
      sales = scrapy.Field()
      listing_url= scrapy.Field()
      flag=scrapy.Field()
      pushdate=scrapy.Field()
      owner=scrapy.Field()
