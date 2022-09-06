import json
import requests
from lxml import etree
import time

data_folder = "data"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
# }
# response = requests.get("https://cn.bing.com/search?q=经济", headers=headers)


# r = response.text
# print("len(r)=", len(r))
# # print(r)
# html = etree.HTML(r, etree.HTMLParser())
# r1 = html.xpath("//div[@class='c-container']")
# print('r1=', r1)
# # r2 = html.xpath('//*[@class="c-abstract"]')
# r2 = html.xpath('//*[@class="content-right_8Zs40"]')
# # print('r2=', r2)
# # r3 = html.xpath('//*[@class="t"]/a/@href')
# r3 = html.xpath("//a/@href")
# print("r3=", r3)
# for i in range(10):
#     print("i=", i)
#     if len(r1) > 0:
#         if not (len(r1) > i and len(r2) > i and len(r3) > i):
#             print("break")
#             break
#         r11 = r1[i].xpath("string(.)")
#         r22 = r2[i].xpath("string(.)")
#         r33 = r3[i]
#         with open(data_folder + "/i1baidu.txt", "a", encoding="utf-8") as c:
#             c.write(json.dumps(r11, ensure_ascii=False) + "\n")
#             c.write(json.dumps(r22, ensure_ascii=False) + "\n")
#             c.write(json.dumps(r33, ensure_ascii=False) + "\n")
#             c.write("------------------------\n")
#         print(r11, end="\n")
#         print("------------------------")
#         print(r22, end="\n")
#         print(r33)
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
# import xlwt

def get_list(url):
    
    # 新闻链接
    res=requests.get(url)
    res.encoding='utf-8'
    
    # 完整HTML
    html=BeautifulSoup(res.text,'html.parser')
    
    # 新闻列表
    newList=[]
    
    for item in html.select('.news-item'):
        try:
            newObj={}
            newObj['title']=item.select('h2 a')[0].text
            newObj['url']=item.select('h2 a')[0].get('href')
            newList.append(newObj)
        except:
            print('出现异常')
    return newList
    

def get_detail(url):

    # 新闻链接
    res=requests.get(url)
    res.encoding='utf-8'
    
    # 完整HTML
    html=BeautifulSoup(res.text,'html.parser')
    
    # 新闻对象
    result={}
    
    # 新闻标题
    result['title']=html.select('.main-title')[0].text
    
    # 发布时间
    timesource=html.select('.date-source span')[0].text
    createtime=datetime.strptime(timesource,'%Y年%m月%d日 %H:%M')
    createtime.strftime('%Y-%m-%d')
    result['createtime']=createtime
    
    # 新闻来源
    result['place']=html.select('.date-source a')[0].text
    
    # 新闻内容
    article=[]
    for p in html.select('#article p')[:-1]:
        article.append(p.text.strip())
    articleText=' '.join(article)
    result['article']=articleText
    
    # 新闻作者
    result['author']=html.select('.show_author')[0].text.strip('责任编辑：')
    
    # 新闻链接
    result['url']=url
    
    return result




if __name__ == "__main__":          #主函数

    newList=get_list('https://news.sina.com.cn/world/')
    # print(newList)
    
    # newObj=get_detail('http://news.sina.com.cn/c/2020-10-19/doc-iiznctkc6335371.shtml')
    # print(newObj)
    
    # book = xlwt.Workbook(encoding='utf-8')
    # sheet = book.add_sheet('ke_qq')
    head = ['标题','时间','作者','链接','来源','内容'] #表头
    # for h in range(len(head)):
    #     sheet.write(0,h,head[h]) #写入表头
  
    for i,item in enumerate(newList):
        try:
            newObj=get_detail(item['url'])

            time.sleep(1.5)
            with open(data_folder + "/i1sina.txt", "a", encoding="utf-8") as c:
                print(newObj['title'])
                c.write(newObj['title'] + "\n\n")                
                print(newObj['article'],'#'*20)
                # c.write(newObj['createtime'] + "\n")
                # c.write(newObj['url'] + "\n")
                # c.write(newObj['place'] + "\n")


                c.write(newObj['article'] + "\n")
                c.write("------------------------\n")
            print (str(i),'写入成功')


        except:
            print (str(i),'出现异常')
            
    # book.save('F:\ke.xls')

