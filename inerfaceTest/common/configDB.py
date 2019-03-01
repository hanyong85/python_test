'''
Created on 2019年2月24日

@author: Administrator
'''
import pymysql
import readConfig
from common.Logtest import MyLog as Log
from common.commontest import get_sql


localReadConfig =readConfig.readConfig()

class MyDB:
    global host,username,password,port,database,config
    host=localReadConfig.get_db('host')
    username=localReadConfig.get_db('username')
    port=localReadConfig.get_db('port')
    password=localReadConfig.get_db('password')
    database=localReadConfig.get_db('database')
    config={
        'host':str(host),
        'user':username,
        'password':password,
        'port':int(port),
        'database':database}
    print(config)
    
    def __init__(self):
        self.log=Log.get_log()
        #self.logger=self.log.get_logger()
        self.db= None
        self.cursor=None
        
    def connectDB(self):
        try:
            #connect to DB
            #self.db = pymysql.connect(host='localhost',user='root',password='han123456',port=3306,database='mysql',charset='utf8')
            self.db = pymysql.connect(**config)
            #create cursor
            self.cursor =self.db.cursor()
            print("Connect DB successfully")
        except ConnectionError as ex:
            print(ex)
            self.logger.error(str(ex))
    
    def executeSQL(self,sql):
        self.connectDB()
        #execute sql
        self.cursor.execute(sql)
        #executing by commiting to DB
        self.db.commit()
        return self.cursor
    
    def get_all(self,cursor):
        value=cursor.fetchall()
        return value
    
    def get_one(self,cursor):
        value=cursor.fetchone()
        print(value)
        return value
    
    def closeDB(self):
        self.db.close()
        print('DATABSE closed!')            
    
if __name__=='__main__':
    db=MyDB()
    sql1= "insert into user(id,name,Age,Sex,Income)values(1001,'张三',30,'男',1.0);"
    sql="select * from user;"
    #db.executeSQL(sql1)
    db.get_one(db.executeSQL(get_sql('newsitetest','rs_member_wa_llet_bill',sql_id='select_member') )) 
      
    db.closeDB()
    
    