# coding:utf-8
from bs4 import BeautifulSoup
import requests


print("正在爬取...")
page = 10
for num in range(1, page+1):
    url = 'http://www.mzitu.com/page/%d/' % num                   # 爬取十页的链接内容
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}
    cont = requests.get(url, header)
    soup = BeautifulSoup(cont.text, "lxml")
    meizi = soup.find("ul", id="pins").find_all("img")
    for girl in meizi:
        html = girl["data-original"]
        title = girl['alt'][0:7]               # 截取img中的前七个文字作为文件名
        name = str(title).replace("?", '_')    # 有个地方有'？',这个符号Windows系统是不能创建文件夹的所以要替换掉
        heihei = requests.get(html, header)
        fout = open(name+".jpg", "wb")
        fout.write(heihei.content)            # 图片格式用content获取内容
        fout.close()
