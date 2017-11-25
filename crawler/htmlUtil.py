#coding=utf-8
'''
Created on 2017年6月25日
处理html格式返回
@author: sunyi
'''
from bs4 import BeautifulSoup
class HtmlUtil():
    def __init__(self,text):
        self.text=text
        self.soup=BeautifulSoup(text,'lxml')
    def find(self,tag=None,attributes=None):
        return self.soup.find(tag,attributes)
    def findAll(self,tag=None,attributes=None):
        return self.soup.findAll(tag,attributes)