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
    dataList1=jsonData.get('data1').get('y5')
    dataList2=jsonData.get('data1').get('y6')
    dataList3=jsonData.get('data1').get('y7')
    dataList4=jsonData.get('data1').get('y8')
    return dateList,dataList1,dataList2,dataList3,dataList4
def storeData(dateStr,dataStr1,dataStr2,dataStr3,dataStr4,conn,cur,wdzjPlatId):
    sql='insert into platBorrowerGrade (date,wanPerson,shiWanPerson,baiWanPerson,qianWanPerson,wdzjPlatId) values ("'+dateStr+'","'+dataStr1+'","'+dataStr2+'","'+dataStr3+'","'+dataStr4+'","'+wdzjPlatId+'")'
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
            'target1':'16',
            'target2':'2'}
        data=session.postReq(url, param)
        dateList,dataList1,dataList2,dataList3,dataList4=handleData(data)
        for j in range(len(dateList)):
            dateStr=str(dateList[j])
            dataStr1=str(dataList1[j])
            dataStr2=str(dataList1[j])
            dataStr3=str(dataList1[j])
            dataStr4=str(dataList1[j])
            storeData(dateStr,dataStr1,dataStr2,dataStr2,dataStr2,conn,cur,str(i))
    except Exception,e:
        traceback.print_exc()
cur.close()
conn.close