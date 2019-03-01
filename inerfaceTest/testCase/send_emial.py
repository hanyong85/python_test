'''
Created on 2019年2月27日

@author: Administrator
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

import readConfig
from email.mime.application import MIMEApplication

localReadConfig=readConfig.readConfig()
host=localReadConfig.get_email('mail_host')
user=localReadConfig.get_email('mail_user')
password=localReadConfig.get_email('mail_pass')
port=localReadConfig.get_email('mail_port')
sender=localReadConfig.get_email('sender')
title=localReadConfig.get_email('subject')
content=localReadConfig.get_email('content')
value=localReadConfig.get_email("receiver")
receiver=[]
for n in value.split('/'):
    receiver.append(n)
    
message=MIMEMultipart()
message["subject"]=Header(title,'utf-8')
message['from'] =Header(sender,'utf-8')
message['to']=Header(':'.join(receiver),'utf-8')

message.attach(MIMEText("测试报告",'plain','utf-8'))
#附件
att1=MIMEApplication(open('D:\\eclipse-workspace\\inerfaceTest\\result\\test.zip','rb').read())
att1.add_header('Content-Disposition','attachment',filename='abc.zip')
message.attach(att1)
try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('1985453012@163.com','han19851015')
    smtp.sendmail('1985453012@163.com','1985453012@163.com',message.as_string())
    smtp.quit()
    print("The test report has send to developer by email.")
except Exception as ex:
    print(ex)

