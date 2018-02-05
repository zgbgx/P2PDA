# P2PDA
use the data scrapied from a third-party website to analyse chinese P2P industry(使用从第三方数据网站爬取的数据分析中国P2P行业现状)<br>
# 关于数据来源
本项目写于2017年七月初，主要使用Python爬取网贷之家以及人人贷的数据进行分析。
网贷之家是国内最大的P2P数据平台，人人贷国内排名前二十的P2P平台。
[源码地址](https://github.com/zgbgx/P2PDA)
# 数据爬取
## 抓包分析
抓包工具主要使用chrome的开发者工具 网络一栏，网贷之家的数据全部是ajax返回json数据，而人人贷既有ajax返回数据也有html页面直接生成数据。
### 请求实例
![QQ截图20180123205633.png](https://user-gold-cdn.xitu.io/2018/1/23/1612355fc7647661?w=861&h=588&f=png&s=30761)
从数据中可以看到请求数据的方式（GET或者POST），请求头以及请求参数。
![QQ截图20180123205843.png](https://user-gold-cdn.xitu.io/2018/1/23/1612355fc7734ef3?w=854&h=576&f=png&s=117389)
从请求数据中可以看到返回数据的格式（此例中为json）、数据结构以及具体数据。
注：这是现在网贷之家的API请求后台的接口，爬虫编写的时候与数据接口与如今的请求接口不一样，所以网贷之家的数据爬虫部分已无效。
## 构造请求
根据抓包分析得到的结果，构造请求。在本项目中，使用Python的 requests库模拟http请求
具体代码：
```
import requests
class SessionUtil():
    def __init__(self,headers=None,cookie=None):
        self.session=requests.Session()
        if headers is None:
            headersStr={"Accept":"application/json, text/javascript, */*; q=0.01",
                "X-Requested-With":"XMLHttpRequest",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
                "Accept-Encoding":"gzip, deflate, sdch, br",
                "Accept-Language":"zh-CN,zh;q=0.8"
                }
            self.headers=headersStr
        else:
            self.headers=headers
        self.cookie=cookie
    //发送get请求
    def getReq(self,url):
        return self.session.get(url,headers=self.headers).text
    def addCookie(self,cookie):
        self.headers['cookie']=cookie
    //发送post请求
    def postReq(self,url,param):
        return self.session.post(url, param).text
```
在设置请求头的时候，关键字段只设置了"User-Agent"，网贷之家和人人贷的没有反爬措施，甚至不用设置"Referer"字段来防止跨域错误。
##  爬虫实例
以下是一个爬虫实例
```
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
```
整个过程中 我们 构造请求，然后把解析每个请求的响应，其中json返回值使用json库进行解析，html页面使用BeautifulSoup库进行解析（结构复杂的html的页面推荐使用lxml库进行解析），解析到的结果存储到mysql数据库中。
## 爬虫代码
[爬虫代码地址](https://github.com/zgbgx/P2PDA/tree/master/crawler)(注：爬虫使用代码Python2与python3都可运行，本人把爬虫代码部署在阿里云服务器上，使用Python2 运行）
# 数据分析
数据分析主要使用Python的numpy、pandas、matplotlib进行数据分析，同时辅以海致BDP。
## 时间序列分析
### 数据读取
一般采取把数据读取pandas的DataFrame中进行分析。
以下就是读取问题平台的数据的例子
```
problemPlat=pd.read_csv('problemPlat.csv',parse_dates=True)#问题平台 
```
数据结构
![QQ截图20180123212641.png](https://user-gold-cdn.xitu.io/2018/1/23/1612355fc7838542?w=989&h=799&f=png&s=33695)
### 时间序列分析
eg 问题平台数量随时间变化
```
problemPlat['id']['2012':'2017'].resample('M',how='count').plot(title='P2P发生问题')#发生问题P2P平台数量 随时间变化趋势
```
图形化展示
![QQ截图20180123212803.png](https://user-gold-cdn.xitu.io/2018/1/23/1612355fc79a6ee9?w=589&h=372&f=png&s=22610)

## 地域分析
使用海致BDP完成（Python绘制地图分布轮子比较复杂，当时还未学习）
### 各省问题平台数量
![下载.png](https://user-gold-cdn.xitu.io/2018/1/23/1612355fc9c8440f?w=1240&h=1114&f=png&s=216741)
### 各省平台成交额
![全年成交额全国各省对比.png](https://user-gold-cdn.xitu.io/2018/1/23/1612355ff69ed6d3?w=1240&h=738&f=png&s=186534)

### 规模分布分析
eg 全国六月平台成交额分布
代码
```
juneData['amount'].hist(normed=True)
juneData['amount'].plot(kind='kde',style='k--')#六月份交易量概率分布
```
核密度图形展示
![QQ截图20180123213700.png](https://user-gold-cdn.xitu.io/2018/1/23/1612355fc9df8101?w=764&h=361&f=png&s=17567)
成交额取对数核密度分布
```
np.log10(juneData['amount']).hist(normed=True)
np.log10(juneData['amount']).plot(kind='kde',style='k--')#取 10 对数的 概率分布
```
图形化展示
![QQ截图20180123213901.png](https://user-gold-cdn.xitu.io/2018/1/23/1612355ff88aad1b?w=699&h=362&f=png&s=16146)
可看出取10的对数后分布更符合正常的金字塔形。
## 相关性分析
### eg.陆金所交易额与所有平台交易额的相关系数变化趋势
```
lujinData=platVolume[platVolume['wdzjPlatId']==59]
corr=pd.rolling_corr(lujinData['amount'],allPlatDayData['amount'],50,min_periods=50).plot(title='陆金所交易额与所有平台交易额的相关系数变化趋势')
```
图形化展示
![QQ截图20180123214114.png](https://user-gold-cdn.xitu.io/2018/1/23/1612355ff8ab63f9?w=634&h=411&f=png&s=41650)

## 分类比较
车贷平台与全平台成交额数据对比
```
carFinanceDayData=carFinanceData.resample('D').sum()['amount']
fig,axes=plt.subplots(nrows=1,ncols=2,sharey=True,figsize=(14,7))
carFinanceDayData.plot(ax=axes[0],title='车贷平台交易额')
allPlatDayData['amount'].plot(ax=axes[1],title='所有p2p平台交易额')
```
![QQ截图20180123214359.png](https://user-gold-cdn.xitu.io/2018/1/23/1612355ffa856e4f?w=1034&h=555&f=png&s=126890)

## 趋势预测
### eg预测陆金所成交量趋势（使用Facebook Prophet库完成）
```
lujinAmount=platVolume[platVolume['wdzjPlatId']==59]
lujinAmount['y']=lujinAmount['amount']
lujinAmount['ds']=lujinAmount['date']
m=Prophet(yearly_seasonality=True)
m.fit(lujinAmount)
future=m.make_future_dataframe(periods=365)
forecast=m.predict(future)
m.plot(forecast)
```
趋势预测图形化展示
![QQ截图20180123214653.png](https://user-gold-cdn.xitu.io/2018/1/23/1612355ffc6d2029?w=956&h=566&f=png&s=178403)
## 数据分析代码
[数据分析代码地址](https://github.com/zgbgx/P2PDA/blob/master/P2P.ipynb)(注：数据分析代码智能运行在Python3 环境下）
[代码运行后样例](https://raw.githubusercontent.com/zgbgx/P2PDA/master/P2P.html)(无需安装Python环境 也可查看具体代码解图形化展示)








