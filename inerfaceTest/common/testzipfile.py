'''
Created on 2019年2月28日

@author: Administrator
'''
import zipfile
import os
import datetime

def zipDir(dirpath,outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zipp = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')

        for filename in filenames:
            zipp.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zipp.close()

#dirpath='D:\\eclipse-workspace\\inerfaceTest\\result\\report'
#outFullName='D:\\eclipse-workspace\\inerfaceTest\\result\\report'+datetime.datetime.now().strftime("%H%M%S")+'.zip'    
#zipDir(dirpath,outFullName)