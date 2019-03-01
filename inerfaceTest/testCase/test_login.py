'''
Created on 2019年2月27日

@author: Administrator
'''
from common.commontest import *
from common.configHttp import ConfigHttp
import unittest
class Login(unittest.TestCase):
            
    def test_baidu(self):
        longin=get_xls('xls_name.xlsx','Sheet1')
        list_num=len(longin)
        for i in range(list_num):
            url=longin[i][2]
            methon =longin[i][1]
            username = longin[i][3]
            passwd = longin[i][4]
            header={'content-type':'application/json'}
            long_params=ConfigHttp()
            long_params.set_url(url)
            long_params.set_headers(header)
            parms={'user_id':username,'email':username}
            data={'email':username,'password':passwd}
            long_params.set_params(parms)
            long_params.set_data(data)  
    
            print(url,methon,username,passwd)
            if methon == 'post':
                long_params.post()
                print(long_params.post().status_code)
            elif methon=='get':
                long_params.get()
                print(long_params.get().status_code)
            else:
                print("end")    
