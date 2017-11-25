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
import json
reload(sys)
sys.setdefaultencoding('utf8')
def storeData(htmlObject,conn,cur,logUtil,loanId):
    creditinfo=htmlObject.find('script',{'id':'credit-info-data'}).text
    jsonData=json.loads(creditinfo)
    jsonOne=jsonData.get('data')
    loanInfo=jsonOne.get('loan')
    beginBidTime=loanInfo.get('beginBidTime')
    sql='update RRDZhaiquanDetail set beginBidTime="'+beginBidTime+'" where loanId="'+loanId+'"'
    cur.execute(sql)
    conn.commit()
    logUtil.warning(loanId)
session=SessionUtil()
conn,cur=DatabaseUtil().getConn()
logUtil=LogUtil("zhaiquanUpdate.log")
for i in range(2029567,2209630):
    url="https://www.renrendai.com/loan/"+str(i)
    try:
        htmlObject=HtmlUtil(session.getReq(url))
        storeData(htmlObject,conn,cur,logUtil,str(i))
    except Exception,e:
        logUtil.warning(traceback.print_exc())
