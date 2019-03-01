'''
Created on 2019年2月22日

@author: Administrator
'''
import os
from xlrd import open_workbook
from xml.etree import ElementTree
from common.Logtest import MyLog
from common.configHttp import ConfigHttp
from  readConfig import proDir
import logging

localConfig=ConfigHttp()
log = MyLog.get_log()
#logger=loging.get_logger()

#从excel文件中读取测试用例
def get_xls(xls_name,sheet_name):
    cls=[]
    #获取文件路径
    xlspath=os.path.join(proDir,'testFile',xls_name)
    #打开xls文件
    file =open_workbook(xlspath)
    #用sheet名称获取sheet页
    sheet=file.sheet_by_name(sheet_name)
    
    #get sheet one rows  按行获取
    nrows = sheet.nrows
    #print(nrows)
    for i in range(nrows):
        if sheet.row_values(i)[0] != 'case_name':
            cls.append(sheet.row_values(i))
    #print(cls)
    return cls
        
    #get sheet one cols  按列获取
    #cols = sheet.cols
    #for i in range(cols):
     #   if sheet.col_values(i)[0] != 'case_name':
    #        cls.append(sheet.col_values(i))
        
  #从xml 文件中读取sql语句
database = {}
def set_xml():
    if len(database) == 0:
        sql_path=os.path.join(proDir,'testFile','sql.xml')
        tree = ElementTree.parse(sql_path)
        for db in tree.findall('database'):
            db_name =db.get('name')
            #print(db_name)
            table ={}
            for tb in db.getchildren():
                table_name=tb.get('name')
                #print(table_name)
                sql={}
                for data in tb.getchildren():
                    sql_id =data.get('sql_id')
                    sql[sql_id]=data.text
                    #print(sql)
                    table[table_name]=sql
        database[db_name] = table
        #print(database)
            
def get_xml_dict(database_name,table_name):
    set_xml()
    database_dict=database.get(database_name).get(table_name)
    #print(database_dict)
    return database_dict

def get_sql(database_name,table_name,sql_id):
    db = get_xml_dict(database_name, table_name)
    sql=db.get(sql_id)
    print(sql)
    return sql

get_xls('xls_name.xlsx','Sheet1')
#get_sql('newsitetest','rs_member_wa_llet_bill',sql_id='select_member') 
#get_sql('newsitetest','rs_member_wa_llet_bill','delete_user')       
