#coding=utf-8
'''
Created on 2017年6月24日
爬去债权详情
@author: 
'''

import sys
import traceback
from databaseUtil import DatabaseUtil
from sessionUtil import SessionUtil
from htmlUtil import HtmlUtil
from logUtil import LogUtil
from dictUtil import DictUtil
import time
import json
reload(sys)
sys.setdefaultencoding('utf8')
def handleData(returnStr):
    jsonData=json.loads(returnStr)
    planList=jsonData.get('data').get('list')
    return planList
def storeData(jsonOne,conn,cur,logUtil,loanId):
    amount=jsonOne.get('amount')
    appendMultipleAmount=jsonOne.get('appendMultipleAmount')
    if len(appendMultipleAmount)==0:
        appendMultipleAmount='0'
    applyQuitDays=jsonOne.get('applyQuitDays')
    baseInterestRate=jsonOne.get('baseInterestRate')
    beginSellingTime=jsonOne.get('beginSellingTime')
    category=jsonOne.get('category')
    earnInterest=jsonOne.get('earnInterest')
    expectedYearRate=jsonOne.get('expectedYearRate')
    extraInterestRate=jsonOne.get('extraInterestRate')
    inalPeriod=jsonOne.get('inalPeriod')
    if len(inalPeriod)==0:
        inalPeriod='0'
    uPlanId=jsonOne.get('id')
    lockPeriod=jsonOne.get('lockPeriod')
    minRegisterAmount=jsonOne.get('minRegisterAmount')
    name=jsonOne.get('name')
    oldExpectedRate=jsonOne.get('oldExpectedRate')
    processRatio=jsonOne.get('processRatio')
    simpleInterest=jsonOne.get('simpleInterest')
    status=jsonOne.get('oldExpectedRate')
    subPointCount=jsonOne.get('subPointCount')
    tag=jsonOne.get('tag')
    sql='insert into RRDUplanList (amount,appendMultipleAmount,applyQuitDays,baseInterestRate,beginSellingTime,category,earnInterest,expectedYearRate,extraInterestRate,inalPeriod,uPlanId,lockPeriod,minRegisterAmount,name,oldExpectedRate,processRatio,simpleInterest,status,subPointCount,tag) values ("'+amount+'","'+appendMultipleAmount+'","'+applyQuitDays+'","'+baseInterestRate+'","'+beginSellingTime+'","'+category+'","'+earnInterest+'","'+expectedYearRate+'","'+extraInterestRate+'","'+inalPeriod+'","'+uPlanId+'","'+lockPeriod+'","'+minRegisterAmount+'","'+name+'","'+oldExpectedRate+'","'+processRatio+'","'+simpleInterest+'","'+status+'","'+subPointCount+'","'+tag+'")'
    print(sql)
    logUtil.warning(loanId)
    cur.execute(sql)
    conn.commit()
session=SessionUtil()
conn,cur=DatabaseUtil().getConn()
logUtil=LogUtil("uplanList.log")
for i in range(366):
    url='https://www.renrendai.com/pc/p2p/uPlan/getFinancePlanList?startNum='+str(i)+'&limit=10&_='+str(int(time.time()))
    try:
        planList=handleData(session.getReq(url))
        for j in range(len(planList)):
            dictObject=DictUtil(planList[j])
            storeData(dictObject,conn,cur,logUtil,str(i))
    except Exception,e:
        logUtil.warning(traceback.print_exc())
cur.close()
conn.close()
