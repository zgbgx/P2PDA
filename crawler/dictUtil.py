#coding=utf-8
'''
Created on 2017年6月24日
处理json对象工具类
@author: sunyi
'''
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class DictUtil():
    def __init__(self,dictObject):
        self.dictObject=dictObject
    def get(self,keyStr):
        getStr=self.dictObject.get(keyStr)
        if getStr is None:
            return ""
        if (type(getStr)==int or type(getStr)==float or type(getStr)==bool):
            return str(getStr)
        if type(getStr)==unicode:
            return getStr.encode('utf-8')
        return getStr
        