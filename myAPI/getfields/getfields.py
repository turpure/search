__author__ = 'james'
from ebaysdk.trading import Connection
from itembyseller import ItemBySeller
from fields import Fields
import re
class GetFields(object):
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

    def get_xml(self,set):

        for ele in set:
            myrequest={'ItemID':ele,'IncludeWatchCount':True}
            myresponse=self.mycon.execute('GetItem',myrequest)
            yield myresponse.text
    def parse(self,sellerid,starttime):
        myset=ItemBySeller(sellerid,starttime).get_item()
        patternCad=re.compile(r"<CategoryID>(.*?)</CategoryID>")
        patternCae=re.compile(r"<CategoryName>(.*?)</CategoryName>")
        patternCoy=re.compile(r'<Country>(.*?)</Country>')
        patternCuy=re.compile(r"<Currency>(.*?)</Currency>")
        patternCue=re.compile(r'<CurrentPrice currencyID="USD">(.*?)</CurrentPrice>')
        patternFee=re.compile(r'<FeedbackScore>(.*?)</FeedbackScore>')
        patternFer=re.compile(r"<FeedbackRatingStar>(.*?)</FeedbackRatingStar>")
        patternGal=re.compile(r"<GalleryURL>(.*?)</GalleryURL>")
        patternHit=re.compile(r"<HitCount>(.*?)</HitCount>")
        patternHir=re.compile(r'<HitCounter>(.*?)</HitCounter>')
        patternItd=re.compile(r"<ItemID>(.*?)</ItemID>")
        patternLon=re.compile(r"<Location>(.*?)</Location>")
        patternQud=re.compile(r"<QuantitySold>(.*?)</QuantitySold>")
        patternQue=re.compile(r"<QuantitySoldByPickupInStore>(.*?)</QuantitySoldByPickupInStore>")
        patternSht=re.compile(r'<ShippingServiceCost currencyID="USD">(.*?)</ShippingServiceCost>')
        patternShe=re.compile(r"<ShippingService>(.*?)</ShippingService>")
        patternSku=re.compile(r"<SKU>(.*?)</SKU>")
        patternSte=re.compile(r"<StartTime>(.*?)</StartTime>")
        patternStr=re.compile(r"<StoreOwner>(.*?)</StoreOwner>")
        patternStl=re.compile(r"<StoreURL>(.*?)</StoreURL>")
        patternTie=re.compile(r'<Title>(.*?)</Title>')
        patternUsd=re.compile(r'<UserID>(.*?)</UserID>')
        patternUse=re.compile(r'<Site>(.*?)</Site>')
        patternVil=re.compile(r'<ViewItemURL>(.*?)</ViewItemURL>')
        patternLin=re.compile(r'<ListingDuration>(.*)</ListingDuration>')


        for xml in self.get_xml(myset):
            expfileds=Fields()
            expfileds.fielddic['categoryid']=re.findall(patternCad,xml)[0]
            expfileds.fielddic['categoryname']=re.findall(patternCae,xml)[0]
            expfileds.fielddic['country']=re.findall(patternCoy,xml)[0]
            expfileds.fielddic['currency']=re.findall(patternCuy,xml)[0]
            expfileds.fielddic['currentprice']=re.findall(patternCue,xml)[0]
            expfileds.fielddic['feedbackscore']=re.findall(patternFee,xml)[0]
            expfileds.fielddic['feedbackstar']=re.findall(patternFer,xml)[0]
            expfileds.fielddic['galleryurl']=re.findall(patternGal,xml)[0]
            expfileds.fielddic['hitcount']=re.findall(patternHit,xml)[0]
            expfileds.fielddic['hitcounter']=re.findall(patternHir,xml)[0]
            expfileds.fielddic['itemid']=re.findall(patternItd,xml)[0]
            expfileds.fielddic['location']=re.findall(patternLon,xml)[0]
            expfileds.fielddic['quantitysold']=re.findall(patternQud,xml)[0]
            expfileds.fielddic['quantitysoldinstore']=re.findall(patternQue,xml)[0]
            expfileds.fielddic['shippingcost']=re.findall(patternSht,xml)[0]
            expfileds.fielddic['shippingservice']=re.findall(patternShe,xml)[0]
            expfileds.fielddic['sku']=re.findall(patternSku,xml)
            expfileds.fielddic['starttime']=re.findall(patternSte,xml)[0]
            expfileds.fielddic['storeowner']=re.findall(patternStr,xml)[0]
            expfileds.fielddic['storeurl']=re.findall(patternStl,xml)[0]
            expfileds.fielddic['title']=re.findall(patternTie,xml)[0]
            expfileds.fielddic['userid']=re.findall(patternUsd,xml)[0]
            expfileds.fielddic['usersite']=re.findall(patternUse,xml)[0]
            expfileds.fielddic['viewitemurl']=re.findall(patternVil,xml)[0]
            expfileds.fielddic['listduration']=re.findall(patternLin,xml)
            yield expfileds.fielddic






