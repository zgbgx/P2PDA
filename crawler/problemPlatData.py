#coding=utf-8
'''
Created on 2017年6月24日
人人贷债权列表爬虫  json格式返回
@author: 
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
    platData=jsonData.get('data').get('platOuterVo')
    return platData
def storeData(jsonOne,conn,cur,platId):
    actualCapital=jsonOne.get('actualCapital')
    aliasName=jsonOne.get('aliasName')
    association=jsonOne.get('association')
    associationDetail=jsonOne.get('associationDetail')
    autoBid=jsonOne.get('autoBid')
    autoBidCode=jsonOne.get('autoBidCode')
    bankCapital=jsonOne.get('bankCapital')
    bankFunds=jsonOne.get('bankFunds')
    bidSecurity=jsonOne.get('bidSecurity')
    bindingFlag=jsonOne.get('bindingFlag')
    businessType=jsonOne.get('businessType')
    companyName=jsonOne.get('companyName')
    credit=jsonOne.get('credit')
    creditLevel=jsonOne.get('creditLevel')
    delayScore=jsonOne.get('delayScore')
    delayScoreDetail=jsonOne.get('delayScoreDetail')
    displayFlg=jsonOne.get('displayFlg')
    drawScore=jsonOne.get('drawScore')
    drawScoreDetail=jsonOne.get('drawScoreDetail')
    equityVoList=jsonOne.get('equityVoList')
    experienceScore=jsonOne.get('experienceScore')
    experienceScoreDetail=jsonOne.get('experienceScoreDetail')
    fundCapital=jsonOne.get('fundCapital')
    gjlhhFlag=jsonOne.get('gjlhhFlag')
    gjlhhTime=jsonOne.get('gjlhhTime')
    gruarantee=jsonOne.get('gruarantee')
    inspection=jsonOne.get('inspection')
    juridicalPerson=jsonOne.get('juridicalPerson')
    locationArea=jsonOne.get('locationArea')
    locationAreaName=jsonOne.get('locationAreaName')
    locationCity=jsonOne.get('locationCity')
    locationCityName=jsonOne.get('locationCityName')
    manageExpense=jsonOne.get('manageExpense')
    manageExpenseDetail=jsonOne.get('manageExpenseDetail')
    newTrustCreditor=jsonOne.get('newTrustCreditor')
    newTrustCreditorCode=jsonOne.get('newTrustCreditorCode')
    officeAddress=jsonOne.get('officeAddress')
    onlineDate=jsonOne.get('onlineDate')
    payment=jsonOne.get('payment')
    paymode=jsonOne.get('paymode')
    platBackground=jsonOne.get('platBackground')
    platBackgroundDetail=jsonOne.get('platBackgroundDetail')
    platBackgroundDetailExpand=jsonOne.get('platBackgroundDetailExpand')
    platBackgroundExpand=jsonOne.get('platBackgroundExpand')
    platEarnings=jsonOne.get('platEarnings')
    platEarningsCode=jsonOne.get('platEarningsCode')
    platName=jsonOne.get('platName')
    platStatus=jsonOne.get('platStatus')
    platUrl=jsonOne.get('platUrl')
    problem=jsonOne.get('problem')
    problemTime=jsonOne.get('problemTime')
    recordId=jsonOne.get('recordId')
    recordLicId=jsonOne.get('recordLicId')
    registeredCapital=jsonOne.get('registeredCapital')
    riskCapital=jsonOne.get('riskCapital')
    riskFunds=jsonOne.get('riskFunds')
    riskReserve=jsonOne.get('riskReserve')
    riskcontrol=jsonOne.get('riskcontrol')
    securityModel=jsonOne.get('securityModel')
    securityModelCode=jsonOne.get('securityModelCode')
    securityModelOther=jsonOne.get('securityModelOther')
    serviceScore=jsonOne.get('serviceScore')
    serviceScoreDetail=jsonOne.get('serviceScoreDetail')
    startInvestmentAmout=jsonOne.get('startInvestmentAmout')
    term=jsonOne.get('term')
    termCodes=jsonOne.get('termCodes')
    termWeight=jsonOne.get('termWeight')
    transferExpense=jsonOne.get('transferExpense')
    transferExpenseDetail=jsonOne.get('transferExpenseDetail')
    trustCapital=jsonOne.get('trustCapital')
    trustCreditor=jsonOne.get('trustCreditor')
    trustCreditorMonth=jsonOne.get('trustCreditorMonth')
    trustFunds=jsonOne.get('trustFunds')
    tzjPj=jsonOne.get('tzjPj')
    vipExpense=jsonOne.get('vipExpense')
    withTzj=jsonOne.get('withTzj')
    withdrawExpense=jsonOne.get('withdrawExpense')
    sql='insert into problemPlatDetail (actualCapital,aliasName,association,associationDetail,autoBid,autoBidCode,bankCapital,bankFunds,bidSecurity,bindingFlag,businessType,companyName,credit,creditLevel,delayScore,delayScoreDetail,displayFlg,drawScore,drawScoreDetail,equityVoList,experienceScore,experienceScoreDetail,fundCapital,gjlhhFlag,gjlhhTime,gruarantee,inspection,juridicalPerson,locationArea,locationAreaName,locationCity,locationCityName,manageExpense,manageExpenseDetail,newTrustCreditor,newTrustCreditorCode,officeAddress,onlineDate,payment,paymode,platBackground,platBackgroundDetail,platBackgroundDetailExpand,platBackgroundExpand,platEarnings,platEarningsCode,platName,platStatus,platUrl,problem,problemTime,recordId,recordLicId,registeredCapital,riskCapital,riskFunds,riskReserve,riskcontrol,securityModel,securityModelCode,securityModelOther,serviceScore,serviceScoreDetail,startInvestmentAmout,term,termCodes,termWeight,transferExpense,transferExpenseDetail,trustCapital,trustCreditor,trustCreditorMonth,trustFunds,tzjPj,vipExpense,withTzj,withdrawExpense,platId) values ("'+actualCapital+'","'+aliasName+'","'+association+'","'+associationDetail+'","'+autoBid+'","'+autoBidCode+'","'+bankCapital+'","'+bankFunds+'","'+bidSecurity+'","'+bindingFlag+'","'+businessType+'","'+companyName+'","'+credit+'","'+creditLevel+'","'+delayScore+'","'+delayScoreDetail+'","'+displayFlg+'","'+drawScore+'","'+drawScoreDetail+'","'+equityVoList+'","'+experienceScore+'","'+experienceScoreDetail+'","'+fundCapital+'","'+gjlhhFlag+'","'+gjlhhTime+'","'+gruarantee+'","'+inspection+'","'+juridicalPerson+'","'+locationArea+'","'+locationAreaName+'","'+locationCity+'","'+locationCityName+'","'+manageExpense+'","'+manageExpenseDetail+'","'+newTrustCreditor+'","'+newTrustCreditorCode+'","'+officeAddress+'","'+onlineDate+'","'+payment+'","'+paymode+'","'+platBackground+'","'+platBackgroundDetail+'","'+platBackgroundDetailExpand+'","'+platBackgroundExpand+'","'+platEarnings+'","'+platEarningsCode+'","'+platName+'","'+platStatus+'","'+platUrl+'","'+problem+'","'+problemTime+'","'+recordId+'","'+recordLicId+'","'+registeredCapital+'","'+riskCapital+'","'+riskFunds+'","'+riskReserve+'","'+riskcontrol+'","'+securityModel+'","'+securityModelCode+'","'+securityModelOther+'","'+serviceScore+'","'+serviceScoreDetail+'","'+startInvestmentAmout+'","'+term+'","'+termCodes+'","'+termWeight+'","'+transferExpense+'","'+transferExpenseDetail+'","'+trustCapital+'","'+trustCreditor+'","'+trustCreditorMonth+'","'+trustFunds+'","'+tzjPj+'","'+vipExpense+'","'+withTzj+'","'+withdrawExpense+'","'+platId+'")'
    cur.execute(sql)
    conn.commit()

conn,cur=DatabaseUtil().getConn()
session=SessionUtil()
logUtil=LogUtil("problemPlatDetail.log")
cur.execute('select platId from problemPlat')
data=cur.fetchall()
print(data)
mylist=list()
print(data)
for i in range(0,len(data)):
    platId=str(data[i].get('platId'))
    
    mylist.append(platId)

print mylist  
for i in mylist:
    url='http://wwwservice.wdzj.com/api/plat/platData30Days?platId='+i
    try:
        data=session.getReq(url)
        platData=handleData(data)
        dictObject=DictUtil(platData)
        storeData(dictObject,conn,cur,i)
    except Exception,e:
        traceback.print_exc()
cur.close()
conn.close