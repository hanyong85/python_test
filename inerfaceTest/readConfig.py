#-*- coding:utf-8 -*-
import os
import codecs
import configparser

#获取当前路径
#proDir=os.path.split(os.path.realpath(__file__))[0]
proDir=os.path.dirname(os.path.realpath(__file__))
#print(proDir)
#获取配置路径
configPath = os.path.join(proDir,'config.ini')
#print(configPath)

class readConfig:
    def __init__(self):
        fd=open(configPath)
        data=fd.read()
        #remove Bom
        if data[0:3] == codecs.BOM_UTF8:
            data = data[3:]
            file=codecs.open(configPath,'w')
            file.write(data)
            file.close()
        fd.close()
        
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)
        s=self.cf.sections()
        #print('section',s)
        

    
    def get_email(self,name):
        value = self.cf.get('EMAIL',name)
        #print("Email",value)
        return value
    
    def get_http(self,name):
        value = self.cf.get('HTTP',name)        
        #print("HTTP",value)
        return value
    
    def get_db(self,name):
        value = self.cf.get('DATABASE',name)
        #print("db",value)
        return value
    
if __name__=='__main__':
    cig=readConfig()
    cig.get_db('host')
    cig.get_email(name='mail_user')
    cig.get_http(name='baseurl')

            
