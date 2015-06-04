# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.selector import Selector
from data.items import ListingItem
import re
import scrapy
import urllib2
import json



class EbaydataSpider(CrawlSpider):
    download_delay = 1
    name="listing"
    allowed_domains=['aliexpress.com']
    start_urls=['http://www.aliexpress.com/wholesale?\
                catId=0&initiative_id=SB_20150604014815\
                &SearchText=phone+6+case+'
                ]
    rules = [
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="history-item product "]')),'myparse'),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="page-next ui-pagination-next"]')))
            ]

    def myparse(self,response):
        orders=response.xpath('//span[@class="orders-count"]/b/text()').extract()
        if orders==[]:
            item=ListingItem()
            item['orders']=['0']
            item['quantity']=['0']
            item['date']=['None']
            temproductid=response.xpath('//div[@class="prod-id"]/span/text()').extract()
            productid=re.findall(re.compile('[0-9]+'),temproductid[0])[0]
            item['productid']=productid
            item['category']=response.xpath('//a[@rel="category tag"]/text()').extract()
            item['title']=response.xpath('//h1[@itemprop="name"]/text()').extract()
            item['seller']=response.xpath('//a[@class="store-lnk"]/text()').extract()
            item['price']=response.xpath('//span[@itemprop="price"]/text()').extract()
            item['address']=response.xpath('//address/text()').extract()[0][2:]
            item['url']=response.url
            yield item
        else:
            temproductid=response.xpath('//div[@class="prod-id"]/span/text()').extract()
            productid=re.findall(re.compile('[0-9]+'),temproductid[0])[0]
            starturl='http://www.aliexpress.com/cross-domain/'+\
                     'detailevaluationproduct/index.html?'+\
                     'productId='+productid+'&type=default&'+\
                     'page=1&_=1433225585325'
            myresponse=urllib2.urlopen(starturl)
            res=myresponse.read()
            whodict=json.loads(res)
            # recdict= whodict['records']
            pagdict=whodict['page']
            for i in  range(1,int(pagdict['total'])+1):
                url='http://www.aliexpress.com/cross-domain/'+\
                'detailevaluationproduct/index.html?'+\
                'productId='+productid+'&type=default&'+\
                'page='+str(i)+'&_=1433225585325'
                eve_response=urllib2.urlopen(url)
                eve_res=eve_response.read()

                eve_whodict=json.loads(eve_res)
                eve_recdict=eve_whodict['records']
                # print eve_recdict
                for rec in eve_recdict:
                    item=ListingItem()
                    item['price']=rec['price']
                    item['quantity']=rec['quantity']
                    temdate=rec['date'].split(' ')[:3]
                    datedict={'Jan':'01','Feb':'02',
                            'Mar':'03','Apr':'04',
                            'May':'05','Jun':'06',
                            'Jul':'07','Aug':'08',
                            'Sep':'09','Otc':'10',
                           'Nov':'11','Dec':'12'
                           }
                    temdate[1]=datedict[temdate[1]]
                    finalldate=[]
                    finalldate.append(temdate[2])
                    finalldate.append(temdate[1])
                    finalldate.append(temdate[0])
                    item['date']='-'.join(finalldate)
                    item['category']=response.xpath('//a[@rel="category tag"]/text()').extract()[-1:]
                    item['orders']=response.xpath('//span[@class="orders-count"]/b/text()').extract()
                    temproductid=response.xpath('//div[@class="prod-id"]/span/text()').extract()
                    productid=re.findall(re.compile('[0-9]+'),temproductid[0])[0]
                    item['productid']=productid
                    item['title']=response.xpath('//h1[@itemprop="name"]/text()').extract()
                    item['seller']=response.xpath('//a[@class="store-lnk"]/text()').extract()
                    item['address']=response.xpath('//address/text()').extract()[0][2:]
                    item['url']=response.url
                    yield item












