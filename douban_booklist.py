# /usr/bin/env python
# coding: utf-8
# filename douban_booklist.py

import time
import requests
from bs4 import BeautifulSoup
import random
import lxml
import pymysql

headers = [
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
]

def book_spider(book_tag,conn):
    global headers
    cursor = conn.cursor()

    url = "https://book.douban.com/tag/%s" % book_tag
    source_code = requests.get(url, headers=random.choice(headers))
    # just get the code, no headers or anything
    plain_text = source_code.text

    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text,"lxml")

    # 得到书籍列表的soup对象
    list_soup = soup.find('ul', {'class': 'subject-list'})
    count = 1

    for book_info in list_soup.find_all('li'):
        # print('tag: %s, count: %d' % (book_tag, count))

        # 书名
        title = book_info.find('a', {'title': True}).string.strip()
        # 评分
        try:
            rating = int(book_info.find('span', {'class': 'rating_nums'}).string.strip())
        except AttributeError: # 可能无人评分
            rating = 0

        # 多少人评论过这本书（看这本书的热度）
        comment = book_info.find('span', {'class': 'pl'}).string.strip()  # ddd人评论
        comment_nums = int(re.search(r"\d+",comment).group()) # 转化为整数
        # 简介
        brief_info = book_info.find('p').string.strip()
        # 豆瓣购买价格
        buy_info = book_info.find('span', {'class': 'buy-info'}).string.strip()

        # 书的描述，需要分解为 作者，译者，出版社，出版时间，目录价 ，其中有一些书没有译者，直接是作者
        desc = book_info.find('div', {'class': 'pub'}).string.strip()
        desc_list = desc.split('/')

        list_price = desc_list.pop()
        pub_time = desc_list.pop()
        publishing = desc_list.pop()
        if len(desc_list) > 1:
            trans_info = desc_list.pop()
            author_info = desc_list.pop()
        else:
            author_info = desc_list.pop()
            trans_info = "无"

        # 插入一行记录，注意MySQL的占位符是%s:
        sql =  "insert into 'DOUBAN_BOOKLIST' ('title', 'rating', 'comment_nums', 'brief_info', 'buy_info', 'author_info', 'trans_info', 'publishing', 'pub_time', 'list_price') values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, [title, rating, comment_nums, brief_info, buy_info, author_info, trans_info, publishing, pub_time, list_price])

        count += 1

    # for 循环结束，提交事务
    conn.commit()
    cursor.close()


def do_spider(book_lists,conn):
    for book_tag in book_lists:
        book_spider(book_tag,conn)


if __name__ == "__main__":

    # 初始化数据库
    conn = pymysql.connect(user='root',password='root',database='DOUBAN_DATA')

    # 执行爬虫
    book_lists = ['心理学', '人物传记', '中国历史', '旅行', '生活', '科普']
    do_spider(book_lists,conn)
