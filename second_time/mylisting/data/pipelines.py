# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import MySQLdb
import MySQLdb.cursors
import socket
import select
import sys
import os
import errno
class MySQLStorePipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            db = 'ebay_com2',
            user = 'root',
            passwd = 'urnothing',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = False
        )
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item
        
    def _conditional_insert(self,tx,item):
       
        if item.get('itemnumber'):
           #for i in items:
           tx.execute(
                    'insert into listing (sellerid,location,itemnumber,category,title,price,shipping,sales,listing_url) \
                      values \
                      (%s,%s,%s,%s,%s,%s,%s,%s,%s)', \
                      (item['sellerid'][0],item['location'][0],item['itemnumber'][0],item['category'][0], \
                      item['title'][0],item['price'][0],item['shipping'][0],item['sales'][0],item['listing_url']) \
                      )
               
