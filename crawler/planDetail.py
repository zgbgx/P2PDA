#coding=utf-8
'''
Created on 2017年6月24日
爬去债权详情
@author: sunyi
'''
from sessionUtil import SessionUtil
from htmlUtil import HtmlUtil
import sys
from databaseUtil import DatabaseUtil
from logUtil import LogUtil
import time
import traceback
reload(sys)
sys.setdefaultencoding('utf8')
def storeData(htmlObject,conn,cur,planId,logUtil):
    logUtil.warning(planId)
    mytype=str(htmlObject.find('h1',{'class':'fn-left fn-text-overflow text-big'}).text).split('（')[0]
    periods=str(htmlObject.find('h1',{'class':'fn-left fn-text-overflow text-big'}).find('span',{'class':'text-big'}).text)[3:-3]
    if htmlObject.find('em',{'class':'font-24px'}) is None:
        interest=str(htmlObject.find('span',{'class':'font-40px num-family'}).text)
    else:
        interest=str(htmlObject.find('em',{'class':'font-24px'}).text)
    months=str(htmlObject.find('span',{'class':'font-40px color-dark-text num-family'}).text)
    amount=str(htmlObject.find('span',{'class':'font-40px color-dark-text num-family  '}).text).strip()
    mylimit=str(htmlObject.find('span',{'class':'fn-left basic-value basic-value-new'}).find('em').text).strip()
    totalEarnings=htmlObject.find('i',{'class':'font-36px num-family'}).text 
    lockEndTime=htmlObject.findAll('td')[5].text
    beginJoinTime=htmlObject.findAll('td')[8].text
    sql='insert into RRDPlanDetail (type,periods,interest,months,amount,mylimit,totalEarnings,lockEndTime,beginJoinTime,planId) values ("'+mytype+'","'+periods+'","'+interest+'","'+months+'","'+amount+'","'+mylimit+'","'+totalEarnings+'","'+lockEndTime+'","'+beginJoinTime+'","'+planId+'")'
    cur.execute(sql)
    conn.commit()
session=SessionUtil()
conn,cur=DatabaseUtil().getConn()
logUtil=LogUtil("planDetail.log")
for i in range(77,13387):
    url="https://www.renrendai.com/financeplan/"+str(i)
    try:
        htmlObject=HtmlUtil(session.getReq(url))
        storeData(htmlObject,conn,cur,str(i),logUtil)
    except Exception,e:
        logUtil.warning(traceback.print_exc())
        
