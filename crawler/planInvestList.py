#coding=utf-8
'''
Created on 2017年6月24日
人人贷债权列表爬虫  json格式返回
@author: sunyi
'''
import json
import time
from databaseUtil import DatabaseUtil
from sessionUtil import SessionUtil
from dictUtil import DictUtil
from logUtil import LogUtil
import traceback
def handleData(returnStr):
    jsonData=json.loads(returnStr)
    loanList=jsonData.get('data').get('jsonList')
    return loanList
def storeData(jsonOne,conn,cur,planId):
    amount=jsonOne.get('amount')
    createTime=jsonOne.get('createTime')
    finalAmout=jsonOne.get('finalAmout')
    nickName=jsonOne.get('nickName')
    tradeMethod=jsonOne.get('tradeMethod')
    ucodeId=jsonOne.get('ucodeId')
    userId=jsonOne.get('userId')
    sql='insert into RRDPlanInvest (amount,createTime,finalAmout,nickName,tradeMethod,ucodeId,userId,planId) values ("'+amount+'","'+createTime+'","'+finalAmout+'","'+nickName+'","'+tradeMethod+'","'+ucodeId+'","'+userId+'","'+planId+'")'
    cur.execute(sql)
    conn.commit()

conn,cur=DatabaseUtil().getConn()
session=SessionUtil()
logUtil=LogUtil("planInvest.log")
for i in range(1,13387):
    time.sleep(1)
    url='https://www.renrendai.com/financeplan/getFinancePlanLenders.action?financePlanStr='+str(i)+'&_='+str(int(time.time()))
    logUtil.warning(str(i))
    try:
        data=session.getReq(url)
        investList=handleData(data)
        if len(investList)>0:
            for j in range(len(investList)):
                dictObject=DictUtil(investList[j])
                storeData(dictObject,conn,cur,str(i))
    except Exception,e:
        logUtil.warning(traceback.print_exc())

cur.close()
conn.close