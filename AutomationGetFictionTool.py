#导入requests,lxml,os包
import requests
from lxml import etree
import os
#创建文件夹
path="斗罗大陆合集"
if not os.path.exists(path):
    os.mkdir(path)
#获取地址标头
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
#获取网址url
url="https://www.85xscc.com/book/"
req=requests.get(url=url,headers=headers)
#将数据字符转为utf-8格式
req.encoding="utf-8"
#解析格式化HTML文档的数据
e=etree.HTML(req.text)
#获取所有书的url地址
bookurl=e.xpath("//li[@class='pop-book']/a[1]/@href")
#遍历地址列表
for i in bookurl:
    book_suburl=f"https://www.85xscc.com{i}"
    book_subreq=requests.get(url=book_suburl,headers=headers)
    book_subreq.encoding="utf-8"
    sub_e=etree.HTML(book_subreq.text)
    #获取书名与作者
    bookname=sub_e.xpath("//div[@class='book-describe']/h1/text()")[0]
    author=sub_e.xpath("//div[@class='book-describe']/p/text()")[0]
    bookname_author=f"{bookname}--{author}"
    #获取第一章的地址
    xsbox_clearfix=sub_e.xpath('//div[@class="xsbox clearfix"]/ul/li[1]/a/@href')[1]
    fiction_url=f"https://www.85xscc.com{xsbox_clearfix}"
    print(f"<---{bookname_author}>--开始下载-->")
    #进入循环
    while True:
        fiction_req=requests.get(url=fiction_url,headers=headers)
        fiction_req.encoding="utf-8"
        sub_sub_e=etree.HTML(fiction_req.text)
        # print(fiction_req.text)
        #获取小说内容
        info="\n".join(sub_sub_e.xpath('//div[@class="m-post"]/p/text()'))
        #获取小说章节
        title=sub_sub_e.xpath('//div[@class="entry-tit"]/h1/text()')[0]
        #获取进入下一章的url
        fiction_url=f'https://www.85xscc.com{sub_sub_e.xpath("//tr/td[2]/a/@href")[1]}'
        #判断当为最后一章时候跳出循环
        if fiction_url==book_suburl:
            break
        #将数据写入txt文件存储
        with open(path+"/"+f"{bookname_author}.txt","a",encoding="UTF-8") as f:
            f.write(title+"\n"+info+"\n\n\n")
        print(f"<---{title}--下载完成--->")
    print(f"<---{bookname_author}>--下载完成-->")