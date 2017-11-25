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
    dateList=jsonData.get('date')
    dataList=jsonData.get('data1')
    return dateList,dataList
def storeData(dateStr,dataStr,conn,cur,wdzjPlatId):
    sql='insert into platVolume (date,amount,wdzjPlatId) values ("'+dateStr+'","'+dataStr+'","'+wdzjPlatId+'")'
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
            'target1':'1',
            'target2':'0'}
        data=session.postReq(url, param)
        dateList,dataList=handleData(data)
        for j in range(len(dateList)):
            dateStr=str(dateList[j])
            dataStr=str(dataList[j])
            storeData(dateStr,dataStr,conn,cur,str(i))
    except Exception,e:
        traceback.print_exc()
cur.close()
conn.close