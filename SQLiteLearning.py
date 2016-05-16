#/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename mysql.py

# 需要安装PYmysql，
# 方式1：使用pip install pymysql
# 方式2：使用git clone之后直接到pymysql目录中执行python setup.py install


import pymysql
conn = pymysql.connect(user='root',password='',database='test')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print('cursor.rowcount:',cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
