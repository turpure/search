__author__ = 'james'
import datetime
'''define the fieds that we want to get'''
class Fields(object):
    fielddic={}
    fielddic['currency']=''
    fielddic['itemid']=''
    fielddic['starttime']=''
    fielddic['viewitemurl']=''
    fielddic['categoryid']=''
    fielddic['currentprice']=''
    fielddic['quantitysold']=''
    fielddic['shippingcost']='' #first priority
    fielddic['title']=''
    fielddic['hitcount']=''
    fielddic['curdate']=str(datetime.datetime.now())[:10]
    fielddic['mysku']=''
    fielddic['deltacount']='0'
    fielddic['deltaprice']='0'
    fielddic['deltasold']='0'
    fielddic['deltatitle']='0'


