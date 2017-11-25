#coding=utf-8
'''
Created on 2017年6月26日
日志类  用户记录爬虫过程中的关键id  以及异常 信息
@author: sunyi
'''
import logging
class LogUtil():
    def __init__(self,filepath):
        logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=filepath,
                filemode='w')
        self.log=logging
    def info(self,logstr):
        self.log.info(logstr)
    def debug(self,logstr):
        self.log.debug(logstr)
    def warning(self,logstr):
        self.log.warning(logstr)
