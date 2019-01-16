import requests
from bs4 import BeautifulSoup

from util import db

original_url = 'https://movie.douban.com/top250'
douban_url = 'https://movie.douban.com/top250?start=0&filter='
url_list = []
movie_name_list = []
movies = {}
movies_list = []
def getRequest():
    url = 'http://www.itest.info/courses'

    # response = requests.request("GET", url)
    # print(response.text)
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    # 遍历页面上所有的h4
    for course in soup.find_all('h4'):

        print(course.text)


def douBan(douban_url):
    #url = 'https://book.douban.com/'
    #url = 'https://book.douban.com/top250?icn=index-book250-all'

    soup = BeautifulSoup(requests.get(douban_url).text, 'html.parser')
    print(soup.find('title').text)
    ol = soup.find('ol', class_='grid_view')
    for li in ol.find_all('li'):
        em = li.find('em', attrs={'class': ''}).get_text()  # 排名
        hd = li.find('div', attrs={'class': 'hd'})
        movie_name = hd.find(
            'span', attrs={'class': 'title'}).get_text()  # 电影名字
        other_name = hd.find('span', attrs={'class': 'other'}).get_text()  # 别名
        # print(movie_name)
        movie_name_list.append(movie_name)
        bd = li.find('div', attrs={'class': 'bd'})
        info = bd.find('p', attrs={'class': ''}).get_text()  # 导演，主演信息
        star = bd.find('span', attrs={'class': 'rating_num'}).get_text()  # 评分
        inq_span = bd.find('span', attrs={'class': 'inq'})  # 主题
        if inq_span is not None:
            inq = inq_span.get_text()
        else:
            inq = "无主题"
        # print(info)
        movies['rank'] = em
        movies['name'] = movie_name
        movies['other_name'] = other_name.replace(' ', '').replace(u'\xa0', '').replace('/', ' ')
        movies['info'] = info.replace(' ', '').replace('\n', '')
        movies['star'] = star
        movies['inq'] = inq
        # print(movies)
        movies_list.append(movies.copy())
        # print(movies_list)
    next_page_url = soup.find('span', attrs={'class': 'next'}).find('a')  # 获取下一页地址

    if next_page_url:
        url = original_url + next_page_url['href']
        url_list.append(url)
        return url
def get_movie_top_250():
    url = douban_url
    while url:
        url = douBan(url)

def save_movie():
    with open('movie.txt', 'w', encoding='utf-8') as f:
        i = 1
        # for movie_name in movie_name_list:
        #     f.write(str(i) + '.' + movie_name + '\n')
        #     i += 1
        for movie in movies_list:
            f.write(str(i) + str(movie) + '\n')
            i += 1
def insert_into_db(rank, movie_name, other_name, detail, star, inq):
    sql_query = "SELECT * from douban_movie where movie_name = '%s'" % movie_name
    sql = """INSERT INTO douban_movie(`rank`, movie_name, other_name, detail, star, inq) VALUES("%s", "%s", "%s", "%s", "%s", "%s")""" % (rank, movie_name, other_name, detail, star, inq)
    # data = db.db_query('test', sql_query)
    # if len(data) == 0:
    #     db.db_update('test', sql)
    db.db_update('test', sql)

if __name__ == '__main__':
    get_movie_top_250()
    save_movie()
    print(movies_list)
    for movie in movies_list:
        insert_into_db(movie['rank'], movie['name'], movie['other_name'], movie['info'], movie['star'], movie['inq'])