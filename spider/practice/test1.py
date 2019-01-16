import random
import re
import urllib

import urllib.request


def test():
    data = urllib.request.urlopen("http://www.jd.com").read().decode("utf-8", "ignore")
    print(len(data))
    pat = "<title>(.*?)</title>"
    title = re.compile(pat, re.S).findall(data)
    print(title)
    print(len(data))
    urllib.request.urlretrieve("http://www.jd.com", filename="jd.htm")


def test1():
    # 浏览器伪装
    opener = urllib.request.build_opener()
    ua = ("User-Agent",
          "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36")
    opener.addheaders = [ua]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen("https://www.qiushibaike.com/").read().decode("utf-8", "ignore")
    pat = "<title>(.*?)</title>"
    title = re.compile(pat, re.S).findall(data)
    print(title)
    print(len(data))


def simulateBrowser():
    uas = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"]
    opener = urllib.request.build_opener()
    ua = ("User-Agent", random.choice(uas))
    opener.addheaders = [ua]
    urllib.request.install_opener(opener)
    print("当前使用的ua: " + str(ua))


def getQiuShiBaiKeMsg():
    simulateBrowser()
    data = urllib.request.urlopen("https://www.qiushibaike.com/").read().decode("utf-8", "ignore")
    pat = "<div class=\"content\">.*?<span>(.*?)</span>.*?</div>"
    content = re.compile(pat, re.S).findall(data)
    for i in range(0, len(content)):
        print(content[i])



if __name__ == '__main__':
    # for i in range(0, 5):
    #     simulateBrowser()
    #     data = urllib.request.urlopen("https://www.qiushibaike.com/").read().decode("utf-8", "ignore")
    #     pat = "<title>(.*?)</title>"
    #     title = re.compile(pat, re.S).findall(data)
    #     print(title)
    getQiuShiBaiKeMsg()
