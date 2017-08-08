#!/usr/local/bin python3

# -*- coding: utf-8 -*-

# 导入mysql驱动
import mysql.connector

# 注意把 password设为你到root口令
conn = mysql.connector.connect(user='root', password='1234', database='Copper')
cursor = conn.cursor()

# 创建user表
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一条记录, 注意MySQL的占位符是 %s
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print('cursor.rowcount: %s' % cursor.rowcount)

# 提交事务
conn.commit()
cursor.close()
# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))

values = cursor.fetchall()
print('values:', values)

# 关闭Cursor和Connection
cursor.close()
conn.close()