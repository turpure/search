__author__ = 'james'
from ebaysdk.trading import Connection
from namedic import skuitem

from fields import Fields
import re
import ssl
import requests
import Queue
from ebaysdk.exception import ConnectionError
from concurrent import  futures
mydic=skuitem()
items=mydic.keys()
class GetFields(object):
    failedqueue=Queue.Queue()
    def __init__(self,
                 domain='api.ebay.com',
                 appid='ZhouPeng-3242-4cc7-88fd-310f513fcd71',
                 devid='df3f2898-65b1-4e15-afd5-172b989903aa',
                 certid='a0e19cf9-9b2b-457f-b6f1-87f3f600ca63',
                 token='AgAAAA**AQAAAA**aAAAAA**cJyLVQ**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wMkoqiC5mHoQmdj6x9nY+seQ**N+QCAA**AAMAAA**nLCwNt4AQt1TRtd2ydNIMuZ2JYnQZKVVYarn41QQfBSqccEDld22ltKr+C/HJTN8AKD4+jn/nIEqtjNMkmh9sxTIa6jVVLAH5sN/93X7gTCmTkOsE/Av612U90nRoyQJ5bX1+NO25tMDZs9U0aTJIwVVu1BAB8/nsjL0pTCWw7KZACJ+a/aQ6swXLvSvOCWIBjFyCaWibKZseT2LoJMvJQmC2QpIuDsQ8cTYozLUYZqC88uKAjo7DNWIvaPVCdwkp/Vux3arR1Asin4ewX1l+LWCamWsXeBiVyaYq/oEUXABgknieVAPEpaFAfSzlrcTNmTWLBDDRwRGI/8hJCwK6/eJWexGrLk7U7p0kRltktNseTckAKT7g1ED4C5gUeQ4/nTHsNQBejUPTzTlwBWTJpwRaBFD7dAlbagH+TKaEJK41Esf/ZpL2599LUMolsO8tBgo0BhtCF/bYtdUUfopksIKNUwPXikadUxx6TurknnTtR1WDD229uUJIIf9BCS68WB56OfDTdXcZ8rdPZ0zdHuw5+BRxrumpFUzTQb5fJeHRDLPtQbLdX5rFPrS+NPJl6Qzi7bWNxUCydNQcIzKv7xLquIPoPx8bD1PRCoQbzjTQsOqhe9PBvLtcJ0Ggve78YjQKb5nDt6YThZ6D+1EOKdcthU03VizDfBKBLJ/NPqktDTx74tsS3l4feAjblGDoQ2RZXefJ9Jk3t+Qc4khlvl4mKpjZ4sCakh4qPWr9H6t3CN80hz5MO1Y7uHPUY61'
                 ):
        self.idomain=domain
        self.iappid=appid
        self.idevid=devid
        self.icertid=certid
        self.itoken=token
        self.mycon=Connection(domain=self.idomain,
                            appid=self.iappid,
                            devid=self.idevid,
                            certid=self.icertid,
                            token=self.itoken)

    def get_xml(self,item):
        fails=0

        while True:
            if fails>=15:
                break
            try:
                myrequest={'ItemID':item,'IncludeWatchCount':True}
                myresponse=self.mycon.execute('GetItem',myrequest)
                return myresponse.text
            except ConnectionError as e:
                print(e)
                print 'the GetItem Call of %s is die' % item
                fails+=1
            except (ssl.SSLError,requests.RequestException):
                print 'the request of %s via GetItem failed' % item
                fails+=1
            else:
                break
    def parse(self,arry):
        patternCad=re.compile(r"<CategoryID>(.*?)</CategoryID>")
        # patternCae=re.compile(r"<CategoryName>(.*?)</CategoryName>")
        patternTie=re.compile(r'<Title>(.*?)</Title>')

        patternCuy=re.compile(r"<Currency>(.*?)</Currency>")
        patternCue=re.compile(r'>(\d+\.\d+)</CurrentPrice>')

        patternHit=re.compile(r"<HitCount>(.*?)</HitCount>")

        patternItd=re.compile(r"<ItemID>(.*?)</ItemID>")

        patternQud=re.compile(r"<QuantitySold>(.*?)</QuantitySold>")

        patternSht=re.compile(r'>(\d+\.\d+)</ShippingServiceCost>')


        patternSte=re.compile(r"<StartTime>(.*?)</StartTime>")

        patternVil=re.compile(r'<ViewItemURL>(.*?)</ViewItemURL>')
        xml=self.get_xml(arry)
        expfileds=Fields()
        expfileds.fielddic['categoryid']=re.findall(patternCad,xml)[0]

        # expfileds.fielddic['categoryname']=re.findall(patternCae,xml)[0]
        expfileds.fielddic['currency']=re.findall(patternCuy,xml)[0]
        try:
            expfileds.fielddic['currentprice']=re.findall(patternCue,xml)[0]
        except IndexError:
             print xml

        expfileds.fielddic['hitcount']=re.findall(patternHit,xml)[0]

        expfileds.fielddic['itemid']=re.findall(patternItd,xml)[0]

        expfileds.fielddic['quantitysold']=re.findall(patternQud,xml)[0]
        expfileds.fielddic['starttime']=re.findall(patternSte,xml)[0][:10]
        try:
            expfileds.fielddic['shippingcost']=re.findall(patternSht,xml)[0]
        except IndexError:
            print xml
        expfileds.fielddic['viewitemurl']=re.findall(patternVil,xml)[0]
        expfileds.fielddic['title']=re.findall(patternTie,xml)[0]
        expfileds.fielddic['mysku']=mydic[arry]
        return expfileds.fielddic


def  main():
    getdata=GetFields()



    with futures.ThreadPoolExecutor(max_workers=20) as executor:

        future_to_url=dict((executor.submit(getdata.parse,item),item)for item in items)
        for future in futures.as_completed(future_to_url):
            item=future_to_url[future]
            if future.exception() is not None:
                print "%s generated an exception:%s" % (item,future.exception)
            else:

                 yield future.result()
if __name__=='__main__':
    main()








