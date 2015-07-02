__author__ = 'james'
from getfields import GetFields
from itembyseller import ItemBySeller

hit=ItemBySeller('gemeba','2015-06-25')

items=hit.get_item()
print items
hit403=GetFields()
print hit403
print hit403.get_xml(items).next()
print hit403.parse('gemeba','2015-06-25').next() # return the fields we expect.