#coding=utf-8
'''
Created on 2017年6月24日
mysql 链接工具类
@author: 
'''
import pymysql
class DatabaseUtil():
    def getConn(self):
        conn=pymysql.connect(host='yourhost',user='youname',passwd='yourpassword',db='p2p',charset='utf8', cursorclass = pymysql.cursors.DictCursor)
        cur=conn.cursor()
        cur.execute('USE p2p')
        return conn,cur