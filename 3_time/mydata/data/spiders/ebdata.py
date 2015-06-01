# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.selector import Selector
from data.items import SalesItem
import re
import scrapy




class ebaydataSpider(CrawlSpider):
    download_delay = 1
    name="salesdetails"
    allowed_domains=['ebay.com']
    start_urls=[
                 'http://stores.ebay.com/Strings77-Store?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/winning-sell?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/pickustyle/',
                 'http://stores.ebay.com/sexyshop09',
                 'http://stores.ebay.com/nice-craft88',
                 'http://stores.ebay.com/11331122?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/sockstore-ol?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/xrhuy12313?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/luodejun-2011?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/ASMALLCOLDLIPS?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/wholesale-etech?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/huangkanming2008?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/hotmall88?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/2012carmm?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/cheapfine2012?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/worldtop1?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/tinaforyou?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/amyebstore?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/eShow-store?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/fashionland2015?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/hkc-15?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/gagagastore',
                 'http://stores.ebay.com/wowcool2009?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/fashionable-168?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/hotting88?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/vivot?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/Everything-Out-There-Store?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/Hkesupplier?_trksid=p2047675.l2563',
                 'http://stores.ebay.com/Home-Clever?_trksid=p2047675.l2563'
               ]
    rules = [
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
        for url in response.xpath('//a[contains(text(),"sold")]/@href').extract():
            yield scrapy.Request(url,callback=self.mp)     
    def mp(self,res):
       lis=res.xpath('//tr[contains(@bgcolor,"#f")]')       
       i=0
       for l in lis:                       
          item=SalesItem()
          reg0='[0-9]{12}'
          pr0=re.compile(reg0)
          t0=re.findall(pr0,res.url)
          item["itemnumber"]=t0
          td=l.xpath('td[@class="contentValueFont"]/text()').extract()
          #reg='[0-9]*\.[0-9]*'
          #pr=re.compile(reg)
          #t= re.findall(pr,td[0])
          #item['price']=t[0]
          #for s in td:
          tempprice=td[0]
          item['price']=tempprice[4:]
          item['quantity']=td[1]
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
          item['shoptime']=tm
          yield item     
       
