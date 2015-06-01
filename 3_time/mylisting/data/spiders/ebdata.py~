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
        item =ListingItem()
        def noempty(lis):
            for i in lis:
                if i!=[]:
                   return i
        selleridlis=[]
        sellerid0=response.xpath('//*[@class="mbg-nw"]/text()').extract()
        selleridlis.append(sellerid0)
        sellerid1=['No ID']
        selleridlis.append(sellerid1)
        item['sellerid']=noempty(selleridlis)
        
        locationlis=[]
	location0=response.xpath('//div[@class="iti-eu-bld-gry "]/text()').extract()
        locationlis.append(location0)
        location1=['No Location']
        locationlis.append(location1)
        item["location"]=noempty(locationlis)
        
        itemnumberlis=[]
        itemnumber0= response.xpath('//*[@id="descItemNumber"]/text()').extract()
        itemnumberlis.append(itemnumber0)
        itemnumber1=['No Itemnumber']
        itemnumberlis.append(itemnumber1)
        item["itemnumber"]=noempty(itemnumberlis)
        
        categorylis=[]
        category0=response.xpath('//a[@class="scnd"]/text()').extract()
        categorylis.append(category0)
        category1=['No Category']
        categorylis.append(category1)
        item['category']=noempty(categorylis)
        
        titlelis=[]
        title0=response.xpath('//*[@id="itemTitle"]/text()').extract()
        titlelis.append(title0)
        title1=['No title']
        titlelis.append(title1)
        item["title"]=noempty(titlelis)


        saleslis=[]
        sales0=response.xpath('//a[contains(text(),"sold")]/text()').extract()
        saleslis.append(sales0)
        sales1=['0 sold']
        saleslis.append(sales1)
        fil='[0-9]*\,?[0-9]+'
        sfil=re.compile(fil)
        temsales=noempty(saleslis)
        item['sales']=re.findall(sfil,temsales[0])
         
       
         #item['sales']=temp[0].split()[0]
        pricelis=[]
        price0=response.xpath('//span[@id="prcIsum"]/text()').extract()
        pricelis.append(price0)
        price1=response.xpath('//span[@id="mm-saleDscPrc"]/text()').extract()
        pricelis.append(price1)
        price2=['US $0.00']
        pricelis.append(price2)
        temprice=noempty(pricelis)
        reg='[0-9]*\.[0-9]*'
        preg=re.compile(reg)
        item['price']= re.findall(preg,temprice[0])
      
        shippinglis=[]
	temshipping0=response.xpath('//span[@id="fshippingCost"]/span[1]/text()').extract()
        if temshipping0==[]:
           temshipping0=['0.00']
        #fil='[0-9]*\.[0-9]*'
        #sfil=re.compile(fil)
        shipping0=re.findall(preg,temshipping0[0])
	shippinglis.append(shipping0)
        shipping1=['0.00']
        shippinglis.append(shipping1)
        item['shipping']=noempty(shippinglis)
        
    
        item['listing_url']=response.url
        return item

       
