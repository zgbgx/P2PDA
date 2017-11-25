#coding=utf-8
'''
Created on 2017年7月3日
平台成交量指数
@author: 
'''
from databaseUtil import DatabaseUtil
from sessionUtil import SessionUtil
from logUtil import LogUtil
from dictUtil import DictUtil
import traceback
import json
def handleData(returnStr):
    jsonData=json.loads(returnStr)
    dateList=jsonData.get('data1').get('x')
    dataList1=jsonData.get('data1').get('y1')
    dataList2=jsonData.get('data1').get('y2')
    dataList3=jsonData.get('data1').get('y3')
    dataList4=jsonData.get('data1').get('y4')
    dataList5=jsonData.get('data1').get('y5')
    return dateList,dataList1,dataList2,dataList3,dataList4,dataList5
def storeData(dateStr,dataStr1,dataStr2,dataStr3,dataStr4,dataStr5,conn,cur,wdzjPlatId):
    sql='insert into platIncomeRateByPeriod (date,day,oneMonth,twoMonth,threeMonth,sixMonth,wdzjPlatId) values ("'+dateStr+'","'+dataStr1+'","'+dataStr2+'","'+dataStr3+'","'+dataStr4+'","'+dataStr5+'","'+wdzjPlatId+'")'
    cur.execute(sql)
    conn.commit()
conn,cur=DatabaseUtil().getConn()
session=SessionUtil()
logUtil=LogUtil("platIncomeRate.log")
cur.execute('select wdzjPlatId from platData where month="2017-06"')
data=cur.fetchall()
print(data)
mylist=list()
print(data)
for i in range(0,len(data)):
    platId=str(data[i].get('wdzjPlatId'))
    
    mylist.append(platId)

print mylist  
for i in mylist:
    url='http://shuju.wdzj.com/plat-info-target.html'
    try:
        param={
            'wdzjPlatId':i,
            'type':'3',
            'target1':'17',
            'target2':'1'}
        data=session.postReq(url, param)
        dateList,dataList1,dataList2,dataList3,dataList4,dataList5=handleData(data)
        for j in range(len(dateList)):
            dateStr=str(dateList[j])
            dataStr1=str(dataList1[j])
            dataStr2=str(dataList2[j])
            dataStr3=str(dataList3[j])
            dataStr4=str(dataList4[j])
            dataStr5=str(dataList5[j])
            storeData(dateStr,dataStr1,dataStr2,dataStr3,dataStr4,dataStr5,conn,cur,str(i))
    except Exception,e:
        traceback.print_exc()
cur.close()
conn.close