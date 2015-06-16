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
import datetime
class MySQLStorePipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            db = 'ebay_monitor',
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
        if not tx.execute('select itemnumber from listing where itemnumber=%s',item['itemnumber']):
            tx.execute(
              'insert into listing (itemnumber,sellerid,location,category,title,price,shipping,sales,listing_url,cretime,chatime,flag,owner) \
                      values \
                      (%s,%s,%s,%s,%s,%s,%s,%s,%s,curdate(),curdate(),%s,%s)', \
                      (item['itemnumber'][0],item['sellerid'][0],item['location'][0],item['category'][0], \
                      item['title'][0],item['price'],item['shipping'],item['sales'],item['listing_url'],\
                      item['flag'][0],item['owner'][0]) 
                      )
        else:

            tx.execute('select sales,price,cretime,chatime from listing where itemnumber=%s',item['itemnumber'][0])
            myitem=tx.fetchall()
            print "*" \
                  ""*50
            print myitem
            subitem=myitem[0]

            ds=item['sales']-subitem['sales']
            dp=item['price']-subitem['price']
            print "#"*20
            print 'ds=%s,dp=%s' % (ds,dp)


            def datesplit(date):
                out=date.split('-')
                outlist=[int(out[0]),int(out[1]),int(out[2])]
                return outlist
            mydate=time.strftime('%Y-%m-%d',time.localtime(time.time()))
            myd=datesplit(mydate)
            mydatetime=datetime.date(myd[0],myd[1],myd[2])
            dtday=mydatetime-subitem['cretime']
            dt=dtday.days
            ddday=mydatetime-subitem['chatime']
            dd=ddday.days
            print 'dt=%s,dd=%s' % (dt,dd)

            volume=ds*item['price']
            tx.execute('update listing set \
                      price=%s,sales=%s,chatime=curdate(),deltas=%s,deltap=%s,deltat=%s,deltad=%s,volume=%s \
                       where listing.itemnumber=%s',\
                       (item['price'],item['sales'],ds,dp,dt,dd,volume,item['itemnumber'][0])
                       )

