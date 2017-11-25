#coding=utf-8
'''
Created on 2017年7月3日
平台成交量指数
@author: sunyi
'''
from databaseUtil import DatabaseUtil
from sessionUtil import SessionUtil
from logUtil import LogUtil
from dictUtil import DictUtil
import traceback
import json
def handleData(returnStr):
    jsonData=json.loads(returnStr)
    dateList=jsonData.get('date')
    dataList1=jsonData.get('data1')
    dataList2=jsonData.get('data2')
    return dateList,dataList1,dataList2
def storeData(dateStr,dataStr1,dataStr2,conn,cur,wdzjPlatId):
    sql='insert into platNewNumVSOldNum (date,newNum,oldNum,wdzjPlatId) values ("'+dateStr+'","'+dataStr1+'","'+dataStr2+'","'+wdzjPlatId+'")'
    cur.execute(sql)
    conn.commit()
conn,cur=DatabaseUtil().getConn()
session=SessionUtil()
logUtil=LogUtil("xinPlanInvest.log")
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
            'type':'1',
            'target1':'19',
            'target2':'20'}
        data=session.postReq(url, param)
        dateList,dataList1,dataList2=handleData(data)
        for j in range(len(dateList)):
            dateStr=str(dateList[j])
            dataStr1=str(dataList1[j])
            dataStr2=str(dataList2[j])
            storeData(dateStr,dataStr1,dataStr2,conn,cur,str(i))
    except Exception,e:
        traceback.print_exc()
cur.close()
conn.close