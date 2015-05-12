from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from ebay.items import EbayItem
class ebayspider(CrawlSpider):
    name="mysearch"
    allowed_domains=['ebay.com']
    start_urls=['http://www.ebay.com/sch/Clothing-Shoes-Accessories-/11450/i.html?_from=R40&_nkw=clothing&_sop=12']
    rules = [
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="gspr next"]'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="vip"]'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="si-ss-eu"]/a'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//td[@class="gspr nextBtn"]/a'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//td[@class="next"]/a'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="vi-url"]/a')),'myparse'),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="ttl"]/a')),'myparse'),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="ttl g-std"]/a')),'myparse'),
	    ]
             
  
    def myparse(self,response):
        item =EbayItem()
	tempsellerid=response.xpath('//*[@class="mbg-nw"]/text()').extract()
	if tempsellerid==[]:
            item['sellersid']=['no store']
        else:
            item['sellersid']=tempsellerid
	item["location"]=response.xpath('//div[@class="iti-eu-bld-gry "]/text()').extract()
        item["itemnumber"]= response.xpath('//*[@id="descItemNumber"]/text()').extract()
        item["title"]=response.xpath('//*[@id="itemTitle"]/text()').extract()
        
        x=response.xpath('//a[contains(text(),"sold")]/text()').extract()
        if x==[]:
           temp=['0 sold']
        else:
           temp=x
        item['sales']=temp[0].split()[0]
        tems=response.xpath('//span[@id="prcIsum"]/text()').extract()
   
	if tems==[]:
           tems=response.xpath('//span[@id="mm-saleDscPrc"]/text()').extract()
        temsp=tems[0]
	temsprice=temsp[4:]
        item['price']=temsprice	
	tempshipping=response.xpath('//span[@id="fshippingCost"]/span[1]/text()').extract()
	if tempshipping==[]:
           tempshipping=['free']
        item['shipping']=tempshipping
        item['url']=response.url
        return item

       
   
        

       


     
       #/html/body/div[3]/div[2]/div/div[2]/div[4]/div[3]/div/div/div/div[1]/div[1]/a/span
