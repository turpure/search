__author__ = 'james'
import re
'''fomart the data in this way {'SKU':'itemID'}'''
def skuitem():
    namearry={}
    try:
        f=open('/home/james/PycharmProjects/modifybyapi/mfields/rawdata','r')
    except IOError as e:
        print(e)
    pattern=re.compile(r'\d{12}')
    for eachline in f:
        sku=eachline[:5]
        itemid=re.findall(pattern,eachline)
        if not itemid==[]:
            namearry[itemid[0]]=sku
    f.close()
    return namearry
if __name__=='__main__':
    a=skuitem()
    for i in a.keys():
        print i
    print len(a.keys())