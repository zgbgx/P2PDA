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
    loanList=jsonData.get('data').get('lenderRecords')
    return loanList
def storeData(jsonOne,conn,cur):
    amount=jsonOne.get('amount')
    autoCheckout=jsonOne.get('autoCheckout')
    bussNo=jsonOne.get('bussNo')
    financeCategory=jsonOne.get('financeCategory')
    financePlanId=jsonOne.get('financePlanId')
    financePlanSubPointId=jsonOne.get('financePlanSubPointId')
    investId=jsonOne.get('id')
    lendTime=jsonOne.get('lendTime')
    lenderType=jsonOne.get('lenderType')
    loanId=jsonOne.get('loanId')
    orderNo=jsonOne.get('orderNo')
    traderMethod=jsonOne.get('tradeMethod')
    user=jsonOne.get('user')
    investorId=jsonOne.get('userId')
    userNickName=jsonOne.get('userNickName')
    sql='insert into RRDZhaiquanInvest (amount,autoCheckout,bussNo,financeCategory,financePlanId,financePlanSubPointId,investId,lendTime,lenderType,loanId,orderNo,tradeMethod,user,investorId,userNickName) values ("'+amount+'","'+autoCheckout+'","'+bussNo+'","'+financeCategory+'","'+financePlanId+'","'+financePlanSubPointId+'","'+investId+'","'+lendTime+'","'+lenderType+'","'+loanId+'","'+orderNo+'","'+traderMethod+'","'+user+'","'+investorId+'","'+userNickName+'")'
    cur.execute(sql)
    conn.commit()

conn,cur=DatabaseUtil().getConn()
session=SessionUtil()
logUtil=LogUtil("zhaiquanInvest.log")
for i in range(2208789,2209630):
    url='https://www.renrendai.com/lend/getborrowerandlenderinfo.action?id=lenderRecords&loanId='+str(i)+'&_='+str(int(time.time()))
    logUtil.warning(str(i))
    try:
        data=session.getReq(url)
        investList=handleData(data)
        if len(investList)>0:
            for j in range(len(investList)):
                dictObject=DictUtil(investList[j])
                storeData(dictObject,conn,cur)
    except Exception,e:
        logUtil.warning(traceback.print_exc())

cur.close()
conn.close