# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from data.items import DataItem
import re
import scrapy

#import urllib2
class ebaydataSpider(CrawlSpider):
    download_delay = 1
    name="ebdata"
    allowed_domains=['ebay.com']
    start_urls=['http://stores.ebay.com/wanlanlan3599?_trksid=p2047675.l2563']
    rules = [Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="gspr nextBtn"]'))),Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="vi-url"]')),'myparse')] #parse the listing containing sales history
     
    def myparse(self,response):
        for url in response.xpath('//a[contains(text(),"sold")]/@href').extract():
            yield scrapy.Request(url,callback=self.mp)     
    def mp(self,res):
       lis=res.xpath('//tr[contains(@bgcolor,"#f")]')
       items=[]
       for l in lis:                       
               item=DataItem()                               
               reg0='[0-9]{12}'
               pr0=re.compile(reg0)
               t0=re.findall(pr0,res.url)
               item["itemnumber"]=t0;
               td=l.xpath('//td[@class="contentValueFont"]/text()').extract()                      
               reg='[0-9]*\.[0-9]*'
               pr=re.compile(reg)
               t= re.findall(pr,td[0])
               item['price']=t[0]
               item['quantity']=td[1]
               
               print t0;
               def func(s):
                di={'Jan':'01','Feb':'02',
                   'Mar':'03','Apr':'04',
                   'May':'05','Jun':'06',
		    'Jul':'07','Aug':'08',
                    'Sep':'09','Otc':'10',
                    'Nov':'11','Dec':'12'
                    }
                date_str=s.split(' ')[0]
                li=date_str.split('-')
                li[0]=di[li[0]]
                lidate=[]
                lidate.append(li[2])
                lidate.append(li[0])
                lidate.append(li[1])
                out=str('-'.join(lidate))
                return out                                         
               tm=func(td[2])
               item['tim']=tm
               items.append(item)
       return items
         
             
       
       
