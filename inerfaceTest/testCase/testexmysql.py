'''
Created on 2019年2月25日

@author: Administrator
'''
import pymysql
import readConfig

localReadConfig =readConfig.readConfig()
host=localReadConfig.get_db('host')
username=localReadConfig.get_db('username')
port=localReadConfig.get_db('port')
password=localReadConfig.get_db('password')
database=localReadConfig.get_db('database')
config={
        'host':str(host),
        'user':username,
        'password':password,
        'port':int(port)}
#        'database':database}
db=pymysql.connect(**config)

cursor=db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
 
#print(data)
cursor.execute("use testdb;")
#print(cursor)
#创建数据库
#cursor.execute('create database if not exists testdb default CHARSET utf8 collate utf8_general_ci;')
#创建表
cursor.execute("drop table if exists user")
#sql="""create table 'user'('id' int(11) NOT NULL,'name' varchar(255) NOT NULL,'age' int(11) NOT NULL,PRIMARY KEY('id'));"""
sql="""create table user (
         id char(20) not null,
         name char(20),
         Age int,
         Sex char(1),
         Income float )  """

cursor.execute(sql)
cursor.execute("desc user")
data = cursor.fetchall()
#print(data)