__author__ = 'james'
'''put the data into mysql'''

import MySQLdb
import getitemcall
def putin():
    conn=MySQLdb.connect(host='192.168.1.129',user='root',passwd='urnothing',db='ebaydata')
# connect the mysql in my sercer
    cur=conn.cursor()
    sqlexist='select itemid from modifyapi where itemid=%s;'
    priceupdate='select currentprice from modifyapi where itemid=%s'
    titleupdate='select title from modifyapi where itemid=%s'
    soldupdate='select sold from modifyapi where itemid=%s'
    hitupdate='select hitcount from modifyapi where itemid=%s'
    sqlinsert='insert into modifyapi values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    for i in getitemcall.main():
        if not cur.execute(sqlexist,i['itemid']):
            print '%s not existing and will be put into the database' % (i['itemid'])
            cur.execute(sqlinsert,(i['mysku'],i['itemid'],i['categoryid'],
                           i['title'],i['quantitysold'],i['shippingcost'],i['currency'],
                           i['currentprice'],i['hitcount'],i['starttime'],i['viewitemurl'],
                           i['deltaprice'],i['deltatitle'],i['deltacount'],
                           i['deltasold'],i['curdate']))
            conn.commit()
        else:
            cur.execute('update modifyapi set curdate=%s',i['curdate'])
            conn.commit()
            cur.execute(priceupdate,i['itemid'])
            priceraw=cur.fetchone()[0]
            if not priceraw==i['currentprice']:
                print '%s:the currentprice is updated' % i['itemid']
                deltap=str(float(i['currentprice'])-float(priceraw))
                cur.execute('update modifyapi set currentprice=%s,deltaprice=%s where itemid=%s',(i['currentprice'],deltap,i['itemid']))
                conn.commit()
            if priceraw==i['currentprice']:
                cur.execute('update modifyapi set deltaprice=%s where itemid=%s',('0',i['itemid']))
                conn.commit()
            cur.execute(soldupdate,i['itemid'])
            soldraw=cur.fetchone()[0]
            if not soldraw==i['quantitysold']:
                print '%s:the quantitysold is updated' % i['itemid']
                deltas=str(int(i['quantitysold'])-int(soldraw))
                cur.execute('update modifyapi set sold=%s,deltasold=%s where itemid=%s',(i['quantitysold'],deltas,i['itemid']))
                conn.commit()
            if soldraw==i['quantitysold']:
                cur.execute('update modifyapi set deltasold=%s where itemid=%s',('0',i['itemid']))
                conn.commit()
            cur.execute(hitupdate,i['itemid'])
            hitraw=cur.fetchone()[0]
            if not hitraw==i['hitcount']:
                print '%s:the hitcount is updated' % i['itemid']
                deltah=str(int(i['hitcount'])-int(hitraw))
                cur.execute('update modifyapi set hitcount=%s,deltacount=%s where itemid=%s',(i['hitcount'],deltah,i['itemid']))
                conn.commit()
            if hitraw==i['hitcount']:
                cur.execute('update modifyapi set deltacount=%s where itemid=%s',('0',i['itemid']))
                conn.commit()
            cur.execute(titleupdate,i['itemid'])
            titleraw=cur.fetchone()[0]
            if not titleraw==i['title']:
                print '%s:the title is updated' % i['itemid']
                cur.execute('update modifyapi set title=%s,deltatitle=%s where itemid=%s',(i['title'],'Yes',i['itemid']))
                conn.commit()
            if titleraw==i['title']:
                print '%s:the title is the same' % i['itemid']
                cur.execute('update modifyapi set deltatitle=%s where itemid=%s',('No',i['itemid']))
                conn.commit()
    cur.close()
    conn.close()

def test():
    conn=MySQLdb.connect(host='192.168.1.129',user='root',passwd='urnothing',db='ebaydata')
    cur=conn.cursor()
    sql="select price from modify where itemid=%s"
    cur.execute(sql,'301500133392')
    raw=cur.fetchone()
    print raw[0]
    conn.close()
if __name__=='__main__':
    # test()
    putin()