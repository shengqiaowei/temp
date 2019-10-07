# author: xiaxiang   time:2019/10/7

from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint
from openpyxl import Workbook
#请求数据
def get_data():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,python%25E5%25BC%2580%25E5%258F%2591,2,1.html'
    #创建Request对象,指定url和header
    req = request.Request(url,headers=header)
    response = request.urlopen(req)

    if response.getcode() == 200:
        data = response.read() #读取响应结果
        #print(type(data)) #bytes类型
        data = str(data,encoding='gbk')#转换为str
        #print(data)

        #将数据写入文件中
        with open('index.html','w',encoding='gbk') as f:
            f.write(data)

#解析数据
def parse_data():
    with open('index.html','r',encoding='gbk') as r:
        html = r.read()

    #创建BeautifulSoup实例,解析html数据
    bs = BeautifulSoup(html,'html.parser') #指定使用html解析parser

    '''
    查找数据（推荐使用css方法）
    '''
    #1.find方法 获取第一个标签
    # meta = bs.find('meta')
    # print(meta)
    # print(bs.find('script')) #返回的是整个标签
    # print(type(meta)) #返回的Tag类型

    #2. find_all()方法,获取所有匹配的标签
    # links = bs.find_all('link')
    # print(links) #返回的是一个集合
    # print(bs.find_all('span'))
    # print(bs.find_all(class_='on')[0])#获取class=on的第一个标签数据
    # print(bs.find_all(id='pageCode'))#id=pageCode的标签数据


    #3.select()方法,推荐使用
    #print(bs.select('#topIndex')) #获取id=topIndex标签的所有数据
    #获取id=topIndex标签下href的职场资讯标签数据
    #print(bs.select('''#topIndex [href="https://mkt.51job.com/careerpost/default_res.php"]'''))
    #print(bs.select('.on')[0]) #获取class=on的第一个标签数据

    #4.获取Tag中的文本 get_text()
    #print(bs.select('.err')[0].get_text(strip=True)) # 获取class=err的第一个标签里的Tag的值,去除空格
    divs = bs.select('#resultList .el')
    result = []
    for div in divs[1:]:
        title = div.select('.t1')[0].get_text(strip=True)
        company = div.select('.t2')[0].get_text(strip=True)
        addr = div.select('.t3')[0].get_text(strip=True)
        salary = div.select('.t4')[0].get_text(strip=True)
        pubData = div.select('.t5')[0].get_text(strip=True)
        row = {
            'title':title,
            'company':company,
            'addr':addr,
            'salary':salary,
            'pubData':pubData
        }
        result.append(row)
    pprint(result)
    return result

#保存数据到excel
def sava_to_excel(data):
    #创建工作薄
    book = Workbook()

    #创建工作表
    sheet = book.create_sheet('上海python招聘',0)

    #写第一行的标题
    sheet.append(['职位名','公司名','工作地点','薪资','发布时间'])

    #插入所有数据
    for item in data:
        row = [item['title'],item['company'],item['addr'],item['salary'],item['pubData']]
        sheet.append(row)

    #输出保存
    book.save('51job.xlsx')


if __name__=='__main__':
    #get_data()
    parse_data()
    sava_to_excel(parse_data())

