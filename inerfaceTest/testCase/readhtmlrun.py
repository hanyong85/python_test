'''
Created on 2019年2月26日

@author: Administrator
'''
import os
from datetime import datetime
import readConfig

resultpath =os.path.join(readConfig.proDir,"result")
now = str(datetime.now().strftime('%y%m%d%H%M%S'))
print(now)
print(resultpath+'\\rusult'+now+'.html')
fp=open(resultpath+'\\rusult'+now+'.html',"wb")

fp.close()
