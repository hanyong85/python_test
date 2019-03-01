'''
Created on 2019年2月26日

@author: Administrator
'''
import unittest
import HTMLTestRunner
import os
from datetime import datetime
import readConfig
from common import configDB

suite = unittest.TestSuite()
all_cases=unittest.defaultTestLoader.discover("D:\\eclipse-workspace\\inerfaceTest\\common", pattern='configDB.py', top_level_dir='D:\\')
print(all_cases)
for case in all_cases:
    suite.addTest(case)
suite.addTest(configDB.MyDB)
print(suite)
resultpath =os.path.join(readConfig.proDir,"result")
now = str(datetime.now().strftime('%y%m%d%H%M%S'))
fp=open(resultpath+'\\rusult'+now+'.html',"wb")
print(fp)
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="test report",description='test descroption')
runner.run(suite)
