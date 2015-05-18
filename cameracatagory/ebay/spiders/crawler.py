from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from ebay.items import EbayItem
class ebayspider(CrawlSpider):
    name="camerasearch"
    allowed_domains=['ebay.com']
    start_urls=['http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=camera+case+bag&_sop=12']
    rules = [Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="gspr next"]'))),# xpath is right and vist the next page
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="vip"]'))), # xpath is OK. vist the page in given catagory
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="si-ss-eu"]/a'))),#xpath is right.vist the store from the listing.
            Rule(SgmlLinkExtractor(restrict_xpaths=('//td[@class="gspr nextBtn"]/a'))),#vist the next page in the store
            Rule(SgmlLinkExtractor(restrict_xpaths=('//td[@class="next"]/a'))),  #vist the next page in the store
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="gspr nextBtn"]'))),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="vi-url"]')),'myparse'),
            Rule(SgmlLinkExtractor(restrict_xpaths=('//td[@class="next"]/a'))),#vist the next page in the store
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="vi-url"]/a')),'myparse'),#vist listings in the store
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="ttl"]/a')),'myparse'),#vist listings in the store
            Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="ttl g-std"]/a')),'myparse') #vist listings in the store
            ]  
  
    def myparse(self,response):
        item =EbayItem()
	tempsellerid=response.xpath('//*[@class="mbg-nw"]/text()').extract()
	if tempsellerid==[]:
            item['sellerid']=['no store']
        else:
            item['sellerid']=tempsellerid
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
