#coding=utf-8
'''
Created on 2017年6月24日
爬去债权详情
@author: sunyi
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
    planList=jsonData.get('data').get('plans')
    return planList
def storeData(jsonOne,conn,cur,logUtil,loanId):
    amount=jsonOne.get('amount')
    earnInterest=jsonOne.get('earnInterest')
    expectedYearRate=jsonOne.get('expectedYearRate')
    fundsuserRate=jsonOne.get('fundsUseRate')
    planId=jsonOne.get('id')
    name=jsonOne.get('name')
    status=jsonOne.get('status')
    subpointCountActual=jsonOne.get('subpointCountActual')
    sql='insert into RRDXinPlanList (amount,earnInterest,expectedYearRate,fundsUseRate,planId,name,status,subpointCountActual) values ("'+amount+'","'+earnInterest+'","'+expectedYearRate+'","'+fundsuserRate+'","'+planId+'","'+name+'","'+status+'","'+subpointCountActual+'")'
    print(sql)
    logUtil.warning(loanId)
    cur.execute(sql)
    conn.commit()
session=SessionUtil()
conn,cur=DatabaseUtil().getConn()
logUtil=LogUtil("uplanList.log")
for i in range(1,73):
    url='https://www.renrendai.com/autoinvestplan/listPlan!listPlanJson.action?pageIndex='+str(i)+'&_='+str(int(time.time()))
    try:
        planList=handleData(session.getReq(url))
        for j in range(len(planList)):
            dictObject=DictUtil(planList[j])
            storeData(dictObject,conn,cur,logUtil,str(i))
    except Exception,e:
        logUtil.warning(traceback.print_exc())
cur.close()
conn.close()
