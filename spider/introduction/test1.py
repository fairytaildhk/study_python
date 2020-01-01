import requests


def test_6v():
    res = requests.get("http://www.6vhao.tv/")
    res.encoding = 'GBK'
    print(res.text)


def test_douban():
    original_url = 'https://movie.douban.com/top250'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
                }
    res = requests.get(url=original_url, headers=headers)
    print(res.status_code)
    print(res.text)


if __name__ == '__main__':
    test_douban()
