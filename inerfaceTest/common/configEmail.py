'''
Created on 2019年2月25日

@author: Administrator
'''
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import threading
import readConfig
from common.Logtest import Log
#import zipfile
#import glob
from email.mime.application import MIMEApplication
#from email.mime.image import MIMEImage
from common import testzipfile
localReadConfig=readConfig.readConfig()

class Email:
    def __init__(self):
        global host,user,password,port,sender,title,content
        host=localReadConfig.get_email('mail_host')
        user=localReadConfig.get_email('mail_user')
        password=localReadConfig.get_email('mail_pass')
        port=localReadConfig.get_email('mail_port')
        sender=localReadConfig.get_email('sender')
        title=localReadConfig.get_email('subject')
        content=localReadConfig.get_email('content')
        self.log=Log()
        self.value=localReadConfig.get_email("receiver")
        self.receiver=[]
        for n in self.value.split('/'):
            self.receiver.append(n)
            
        #defind email subject
        date=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        self.subject=title+ " " +date
        
        #self.logger=self.log.get_logger()
        self.msg = MIMEMultipart("mixd")
        
    def config_header(self):
        self.msg["subject"]=self.subject
        self.msg['from'] =sender
        self.msg['to']=':'.join(self.receiver)
    
    #邮件正文    
    def config_content(self):
        content_plain = MIMEText(content,'plain','utf-8')
        self.msg.attach(content_plain)
            
    def config_file(self):
        #if self.check_file():
        reportpath=os.path.join(readConfig.proDir,'result','report')            
        #files = glob.glob(reportpath +'\*')
        #print(files)
        zippath=reportpath+datetime.datetime.now().strftime("%H%M%S")+'.zip'
        #f=zipfile.ZipFile(zippath,'w',zipfile.ZIP_DEFLATED)
            #for file in files:
                #f.write(file)
            #f.close()
        #压缩文件    
        testzipfile.zipDir(dirpath=reportpath,outFullName=zippath)
        #构造邮件附件                    
        reportfile = zippath
                #文本附件
            #filehtml=MIMEText(reportfile,'base64','utf-8')
            #压缩文件附件
        filehtml=MIMEApplication(open(reportfile,'rb').read())
            #图片附件
            #filehtml=MIMEImage()
            #ilehtml['Content-Type']='application/octet-stream'
            #filehtml['Content-Disposition']="attachment';  filename='test.zip'"
        filehtml.add_header('Content-Disposition', 'attachment',filename='report.zip')
        self.msg.attach(filehtml)
    #检查文件是否存在                
#    def check_file(self):
#        reportpath=os.path.join(readConfig.proDir,'result','rusult190227111450.html')        
#        if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
#            return True
#        else:
#            return False
            
    def send_email(self):
        self.config_header()
        self.config_content()
        self.config_file()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user,password)
            smtp.sendmail(sender,self.receiver,self.msg.as_string())
            self.log.logger.info("The test report has send to developer by email.")
        except Exception as ex:
            print(ex)
            self.log.logger.error(str(ex))
        finally:
            smtp.quit()
                
class MyEmail:
    email = None
    mutex= threading.Lock()
    def __init__(self):
        pass
    
    @staticmethod
    def get_email():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email=Email()
            MyEmail.mutex.release()
            return MyEmail.email

if __name__ =="__main__":
    email=Email()
    #email.check_file()
    #email.config_file()
    email.send_email()
            
            
                    
                
                