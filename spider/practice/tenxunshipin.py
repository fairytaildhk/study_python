# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 10:20
# @Author  : huangkaiding
import json
import re
import urllib
import urllib.request

import requests


def tencent_v():
    url = "https://video.coral.qq.com/filmreviewr/c/upcomment/xmw2gfef226jygj?reqnum=2&callback=jQuery1124003648157680859265_1547956670506&_=1547956670507 "
    for i in range(0, 10):
        pat1 = '"content":"(.*?)"'
        pat2 = '<p>(.*?)<\\\/p>'
        pat3 = '"last":"(.*?)"'
        print("第" + str(i + 1) + "页")
        # url = "https://video.coral.qq.com/filmreviewr/c/upcomment/xmw2gfef226jygj?reqnum=2&callback=jQuery112405663457159547933_1547953743135&_=1547953743136 "
        data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
        cid = re.compile(pat3, re.S).findall(data)[0]
        print(cid)
        url = "https://video.coral.qq.com/filmreviewr/c/upcomment/xmw2gfef226jygj?commentid=" + str(
            cid) + "&reqnum=3&callback=jQuery112405663457159547933_1547953743140"
        contents = re.compile(pat1, re.S).findall(data)
        for content in contents:
            texts = re.compile(pat2, re.S).findall(content)
            for text in texts:
                print(eval('u"'+str(text)+'"'))

def tencent_get():
    url = 'https://video.coral.qq.com/filmreviewr/c/upcomment/xmw2gfef226jygj?reqnum=2&callback=jQuery1124003648157680859265_1547956670506&_=1547956670507 '
    px = {'http': 'http://10.10.2.188:8888'}

    response = requests.get(url=url, proxies=px, verify=False).text
    resp = response.split('(')[1].split(')')[0]
    commentids = json.loads(resp)['data']['commentid']
    for commentid in commentids:
        contents = commentid['content']
        print(contents)

if __name__ == '__main__':

    # tencent_v()
    tencent_get()