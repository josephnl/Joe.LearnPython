# /usr/bin/env python3
# -*- coding: utf-8 -*-
# filename urllib2.py


from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))
#

req = request.Request('http://www.zhihu.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode(encoding='utf-8'))


# 可能因为在公司环境中，陈炜在抓豆瓣数据，所以，对于豆瓣的页面抓取总是出差错，回家试一试
# 错了，从今天的经验来看，是豆瓣禁止爬虫了，需要在request中做一些伪装，把headers，Cookie, host加入，
