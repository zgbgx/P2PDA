#coding=utf-8
'''
Created on 2017年6月24日
session 工具类
@author: sunyi
'''
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
    def getReq(self,url):
        return self.session.get(url,headers=self.headers).text
    def addCookie(self,cookie):
        self.headers['cookie']=cookie
    def postReq(self,url,param):
        return self.session.post(url, param).text
