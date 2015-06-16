# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.selector import Selector
from data.items import ListingItem
import re
import scrapy
import sellers

class EbaydataSpider(CrawlSpider):
    download_delay = 1
    name="chenwenping"
    allowed_domains=['ebay.com']
    
    start_urls=['http://www.ebay.com/usr/'+ i for i in sellers.chenwenping]
    rules = [
            Rule(SgmlLinkExtractor(restrict_xpaths=('//span[@class="store_lk fl"]/a'))),
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
        itemnumber1=['000000000000']
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
        strsales=re.findall(sfil,temsales[0])[0]
        strsales=strsales.replace(',','')
        item['sales']=int(strsales)


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
        strprice= re.findall(preg,temprice[0])[0]
        item['price']=float(strprice)
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
        strshipping=noempty(shippinglis)[0]
        item['shipping']=float(strshipping)

        item['listing_url']=response.url
        item['flag']=['1'] #count the times of crawling

        item['owner']=['chenweiping']
        return item

       
