'''
Created on 2019年2月22日

@author: Administrator
'''
import logging
from datetime import datetime
import threading
import readConfig
import os
from logging import handlers

class Log:
    def __init__(self):
        global logPath,resultPath,proDir        
        proDir=readConfig.proDir
        resultPath =os.path.join(proDir,'result')
        #创建结果文件
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
            #调用时间创建日志文件
        logPath=os.path.join(resultPath,str(datetime.now().strftime('%y%m%d')))
        if not os.path.exists(logPath):
            os.mkdir(logPath)
            #defined logger
        self.logger = logging.getLogger(os.path.join(logPath,"output.log"))
        #defined log level
        self.logger.setLevel(logging.DEBUG)
        #日志格式
        formatter = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        #defined handler
        sh =logging.StreamHandler() #屏幕打印
        sh.setFormatter(formatter)
               
        #LOG_FORMAT ="'%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'"  #日志格式化
        #DATE_FORMAT="%y%m%d%H%M%S"  #日期格式化
        #logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT,datefmt=DATE_FORMAT,
        #                    handlers=[handler,handlerp])
        th = handlers.TimedRotatingFileHandler(filename=os.path.join(logPath,"output.log"),when='D',backupCount=3,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(formatter)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)

            
class MyLog:
    log = None
    mutex = threading.Lock()
    
    def __init__(self):
        pass
    
    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log=Log()
            MyLog.mutex.release()
        return MyLog.log
            

if __name__=="__main__":
    log = Log()
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('警告')
    log.logger.error('报错')
    log.logger.critical('严重')
    
        
