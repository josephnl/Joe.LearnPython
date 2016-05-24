# /usr/bin/python
# coding: utf-8
# filename s.py

import pymysql

conn = pymysql.connect(user='root', password='', database='DOUBAN_DATA', charset='utf8')
cursor = conn.cursor()

# 形成内容
title = '认识商业'
rating = 8.5
comment_nums = 666
brief_info = '《认识商业》是全美高等院校采用量最大的商业入门教材，出版三十多年来，在西方国家长销不衰，并被全球几百所大专院校列为企业管理课程、MBA教程的必选教材。历经七...'
buy_info = '纸质版 52.40 元起'
author_info = '[美] 威廉·尼科尔斯、[美] 詹姆斯·麦克修、[美] 苏珊·麦克修'
trans_info = '陈智凯、黄启瑞'
publishing = '世界图书出版公司'
pub_time = '2009-10'
list_price = '68.00元'
book_tag = '经济学'

# 执行SQL
sql = "insert into DOUBAN_BOOKLIST (title, rating, comment_nums, brief_info, buy_info, author_info, trans_info, publishing, pub_time, list_price, book_tag) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
print(sql)
cursor.execute(sql, [title, rating, comment_nums, brief_info, buy_info, author_info, trans_info, publishing, pub_time, list_price, book_tag])

# 提交事物
conn.commit()
cursor.close()
