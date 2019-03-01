'''
Created on 2019年2月22日
#配置文件中读取
@author: Administrator
'''
import requests
import readConfig
from common.Logtest import MyLog,Log
from test.test_decimal import file
from pip._vendor.urllib3 import response

localReadConfig=readConfig.readConfig()
class ConfigHttp:
    def __init__(self):
        global host,port,timeout
        host=localReadConfig.get_http('baseurl')
        port=localReadConfig.get_http('port')
        #timeout=localReadConfig.get_http('timeout')
        self.log = MyLog.get_log()
        #self.logger =Log.get_logger()
        timeout=1.5
        #self.headers={'content-type':'application/json'}
        self.params={'user_id':'123456','email':'123456@163.com'}
        #self.data={'password':'han19851015','email':'1985453012@163.com'}
        #self.url='http://mail.163.com'
        self.files={}
    
    def set_url(self,url):
        #self.url=host+url  接口参数固定模式
        self.url=url     #接口参数全链接模式
        
    def set_headers(self,header):
        self.headers=header
    
    def set_params(self,param):
        self.params=param
        
    def set_data(self,data):
        self.data=data
        
    def set_files(self,file):
        self.files=file
        
    #定义 http 获取方式:get
    def get(self):
        try:
            response =requests.get(
                self.url,
                params=self.params,
                headers=self.headers,
                timeout=float(timeout))
            self.log.logger.info(response.status_code)
            return response
        except Exception as es:
            self.log.logger.error(es)
            return None
        
    #定义 http 获取方式:post    
    def post(self):
        try:
            response =requests.post(
                self.url,
                data=self.data,
                headers=self.headers,
                files=self.files,
                timeout=float(timeout))
            self.log.logger.info(response.status_code)               
            return response
        
        except Exception as es:
            self.log.logger.error(es)
            return None    
        
#if __name__=='__main__':
#    C=ConfigHttp()
#    C.get()
#    C.post()
    
    
    
        