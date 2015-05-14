from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from data.items import DataItem
import re
import scrapy

#import urllib2
class ebaydataSpider(CrawlSpider):
    download_delay = 1
    name="eb"
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
	       #print t0
               item["itemnumber"]=t0;
               itmes.append(item)
       return items
