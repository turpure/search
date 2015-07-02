__author__ = 'james'
import requests
import re
class ItemBySeller(object):

    def __init__(self, sellerid ,starttime,appid='ZhouPeng-3242-4cc7-88fd-310f513fcd71'):
        self.appid=appid
        self.sellerid=sellerid
        self.starttime=starttime
    def get_xml(self,url):
        response=requests.get(url)
        return response.text
    def get_item(self):
        pattern=re.compile(r"<itemId>([0-9]{12})")
        myset=set()
        for i in range(1,3):
            url='http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.12.0\
&SECURITY-APPNAME='\
+self.appid+\
'&RESPONSE-DATA-FORMAT=XML&REST-PAYLOAD\
&itemFilter(0).name=Seller&itemFilter(0).value='\
+self.sellerid+\
'&itemFilter(1).name=FeaturedOnly&itemFilter(1).value=False\
&itemFilter(2).name=StartTimeFrom&itemFilter(2).value='\
+self.starttime+\
'T04:26:57.000Z\
&paginationInput.entriesPerPage=100\
&paginationInput.pageNumber='\
+str(i)+\
'&outputSelector=SellerInfo'
            xml=self.get_xml(url)
            eleitem=re.findall(pattern,xml)
            myset=set(eleitem)|myset
        return myset




