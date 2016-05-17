# usr/bin/env python
# coding=utf-8
# filename LearnSpider.py

import requests
import urllib
import re
import random
from time import sleep


def main():
    i = 1
    url = 'https://www.zhihu.com/question/22591304/followers'
    #   感觉这个话题下面美女多

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4',
        'Cookie': '_za=edfabb4a-14ed-4cec-823b-90ec7777a115; udid="AIAAVdhAlAmPTncTpTSdtVdksyogo0w0zOs=|1457515850"; _ga=GA1.2.1401064362.1450455198; _zap=224b8bae-fcc6-466f-b815-3d668126c3a2; d_c0="ACDADuv9oQmPTkKtsNWu5C2bvsfWx7uShiY=|1461289972"; q_c1=0c8f1b92d4364bb8b2370440679ec27f|1461551143000|1448108303000; l_cap_id="NWRhMzZjNjQzOWY4NDI2NThhMDgyY2EwZDM1M2YwNTI=|1461556490|73c37be27633717a4989d1a8bd71afe0ac696fb9"; cap_id="NmM5YmI0ZWJkMzIxNGUwZGFhZDQyYjg1OWFhM2M1NDY=|1461556490|bbc139a83e3d9f4c1c2b8e0df281d72050b18fd9"; login="NTQ2NGY5MjkzM2JhNDJmZTgyMzk2M2I3MzgzYjNkOGI=|1461556503|3d8ff250e9a5fd6a3c650dbf59401b35431a18d2"; z_c0=Mi4wQUJCS0w2akNrUWdBSU1BTzZfMmhDUmNBQUFCaEFsVk5JaUpGVndCMzRFTmt2a0RZY2FaSkx5UjRmd1dLRGNIMW1R|1461556514|0d42c35b9490f72669bb3431267c4c3a047a36e0; _xsrf=52749ce4dc67ad20c2060ee5bac3fea1; __utma=51854390.1401064362.1450455198.1463461338.1463463613.4; __utmc=51854390; __utmz=51854390.1463392235.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.110-1|2=registration_date=20150820=1^3=entry_date=20150820=1',
        'host': 'www.zhihu.com'
    }

    for x in range(20, 3600, 20):
        data = {
            'start': '0',
            'offset': x,
            '_xsrf': '52749ce4dc67ad20c2060ee5bac3fea1'
        }
        # 知乎用offset控制加载的个数，每次响应加载20

        s = requests.Session()
        r = s.post(url, headers=headers, data=data, timeout=10)
        # 用Session 加上post提交form data

        imgs = re.findall('<img src=\\\\\"(.*?)_m.jpg', r.text)
        # 在爬下来的json上用正则提取图片地址，去掉_m为大图

        for img in imgs:
            try:
                img = img.replace('\\', '')
                # 去掉\字符这个干扰成分
                pic = img + '.jpg'
                path = 'd:\\bs4\\zhihu\\jpg\\' + str(i) + '.jpg'
                # 声明存储地址及图片名称
                urllib.request.urlretrieve(pic, path)
                # 下载图片
                print('You Downloading No.' + str(i) + 'picture')
                i += 1
                sleep(random.uniform(0.5, 1))
                # 睡眠函数用于防止爬取过快被封IP
            except:
                print('You missing 1 picture')
                pass
                sleep(random.uniform(0.5, 1))

if __name__ == '__main__':
    main()
