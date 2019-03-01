'''
Created on 2019��2��22��

@author: Administrator
'''
import unittest
import HTMLTestRunner_cn
import readConfig
import os
from common.configEmail import Email
#from common.configDB import localReadConfig
from common.Logtest import MyLog 
import logging
from datetime import datetime

class MyTest(unittest.TestCase):
    def __init__(self):
        global log
        log=MyLog.get_log()
        self.caseListFile =os.path.join(readConfig.proDir,"caselist.txt")
        self.caseList=[]
        self.reportpath=os.path.join(readConfig.proDir,'result','report')
        if not os.path.exists(self.reportpath):
            os.mkdir(self.reportpath)
    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data=str(value)
            print(data)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n",""))
                print(self.caseList.append(data.replace("\n","")))
                fb.close()
            
    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_model = []
        for case in self.caseList:
            case_file=os.path.join(readConfig.proDir,'testCase')
            print(case_file)
            case_name=case.split("/")[-1]
            print(case_name+".py")
            all_case = unittest.defaultTestLoader.discover(case_file, pattern=case_name+".py", top_level_dir=None)
            suite_model.append(all_case)
        print(suite_model)
        if len(suite_model) >0:
            for suite in all_case:
                for test_name in suite:
                    print(test_name)
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite
    def run(self):
        try:
            suit = self.set_case_suite()
            if suit is not None:
                log.logger.info("Test START")
                now = str(datetime.now().strftime('%y%m%d%H%M%S'))
                fp=open(self.reportpath+'\\'+now+'.html',"wb")
                print(fp)
                runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="自动化测试学习用例报告",description='自动化测试学习用例报告')
                runner.run(suit)
            else:
                print("hava no case to test.")
                log.logger.info("hava no case to test.")
        except Exception as ex:
            print(ex)
            log.logger.error(str(ex))
        finally:
            print("test end")
            log.logger.info("test end")
            
            email =Email()
            localReadConfig=readConfig.readConfig()
            on_off = localReadConfig.get_email("on_off")
            if int(on_off) ==0:
                email.send_email()
            elif int(on_off) ==1:
                print("doesn't send report email to developer")
                log.logger.info("doesn't send report email to developer")
            else:
                print("Unknow state.")
                log.logger.info("Unknow state.")
                
if __name__=="__main__":
    C=MyTest()
    C.run()
            
        