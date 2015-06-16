# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.selector import Selector
from data.items import SalesItem
import re
import scrapy
import sellers




class ebaydataSpider(CrawlSpider):
    download_delay = 1
    name="yafei"
    allowed_domains=['ebay.com']
    start_urls=['http://www.ebay.com/usr/'+ i for i in sellers.yafei]
                 

               
    rules = [
            Rule(SgmlLinkExtractor(restrict_xpaths=('//span[@class="store_lk fl"]/a'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="gspr next"]'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="vip"]'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="u-flL si-ss-lbl "]/a'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="gspr nextBtn"]'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="gspr nextBtn"]'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="gspr nextBtn-d"]'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//td[@class="next"]/a'))),#vist the next page in the store
            Rule(SgmlLinkExtractor(restrict_xpaths=('//td[@class="gspr nextBtn"]/a'))),#vist the next page in the store
            Rule(SgmlLinkExtractor(restrict_xpaths=('//td[@class="next"]/a'))),  #vist the next page in the store
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="gspr nextBtn"]'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="vi-url"]')),'myparse'),
            #Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="vi-url"]')),'myparse'),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="vi-url"]/a')),'myparse'),#vist listings in the store
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="ttl"]/a')),'myparse'),#vist listings in the store
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="ttl g-std"]/a')),'myparse') #vist listings in the store
            ]  
              
     
    def myparse(self,response):
        for url in response.xpath('//a[contains(text(),"View all revisions")]/@href').extract():
            yield scrapy.Request(url,callback=self.mp)     
    def mp(self,res):
       item=SalesItem()
       mydate=res.xpath('//table[@bgcolor="#FFFFFF"]/tr[2]/td[1]/text()').extract()
       def func(s):
              di={'Jan':'01','Feb':'02',
                  'Mar':'03','Apr':'04',
                  'May':'05','Jun':'06',
                  'Jul':'07','Aug':'08',
                  'Sep':'09','Otc':'10',
                  'Nov':'11','Dec':'12'
                  }
           
              li=s.split('-')
              li[0]=di[li[0]]
              lidate=[]
              lidate.append(li[2])
              lidate.append(li[0])
              lidate.append(li[1])
              out=str('-'.join(lidate))
              return out 	
       date=func(mydate[0])
       item['pushdate']=date
       reg0='[0-9]{12}'
       pr0=re.compile(reg0)
       t0=re.findall(pr0,res.url)
       item["itemnumber"]=t0[0]
       
       yield item          
       
       
       
