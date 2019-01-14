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
        hd = li.find('div', attrs={'class': 'hd'})
        movie_name = hd.find(
            'span', attrs={'class': 'title'}).get_text()  # 电影名字
        # print(movie_name)
        movie_name_list.append(movie_name)
        bd = li.find('div', attrs={'class': 'bd'})
        info = bd.find('p', attrs={'class': ''}).get_text()
        # print(info)
        movies['name'] = movie_name
        movies['info'] = info.replace(' ', '').replace('\n', '')
        # print(movies)
        movies_list.append(movies.copy())
        # print(movies_list)
    next_page_url = soup.find('span', attrs={'class': 'next'}).find('a')

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
            f.write(str(i) + movie['name'] + '信息：' + movie['info'] + '\n')
            i += 1
def insert_into_db(movie_name, detail):
    sql_query = "SELECT * from douban_movie where movie_name = '%s'" % movie_name
    sql = """INSERT INTO douban_movie(movie_name, detail) VALUES('%s', '%s')""" % (movie_name, detail)
    data = db.db_query('test', sql_query)
    if data is not None:
        db.db_update('test', sql)

if __name__ == '__main__':
    get_movie_top_250()
    save_movie()
    print(movies_list)
    for movie in movies_list:
        # print(len(movie['info']))
        # if len(movie['info']) > 100:
        #     info = movie['info'][0:50]
        #     print(info)
        # else:
        #     info = movie['info']
        insert_into_db(movie['name'], movie['info'])