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
            db = 'ali1',
            user = 'root',
            passwd = 'urnothing',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
        )
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item
        
    def _conditional_insert(self,tx,item):
       
        if item.get('productid'):
           #for i in items:
           tx.execute(
                      'insert into alilisting (productid,category,seller,address,price,orders,quantity,shoptime,title,url) \
                      values \
                      (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', \
                      (item['productid'],item['category'][0],item['seller'][0],item['address'],item['price'],
                       item['orders'][0],item['quantity'],item['date'],item['title'][0],item['url'])
                      )
               
