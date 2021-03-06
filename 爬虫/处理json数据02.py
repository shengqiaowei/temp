# author: xiaxiang   time:2019/10/7
import requests
import json

#获取数据
def get_data():
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=400&page_start=40'
    response = requests.get(url,headers=header)
    if response.status_code == 200:
        result = response.json() #将response的json转换为python的dict
        #print(result)
        return result

#解析json数据
def parse_data(html):
    movies = html['subjects']
    for movie in movies:
        print(movie['title'],movie['rate'])
if __name__=='__main__':
    parse_data(get_data())