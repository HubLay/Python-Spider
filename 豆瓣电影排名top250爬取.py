# python-hello
#第一页【豆瓣电影 Top 250】https://movie.douban.com/top250?start=0&filter=
#第二页【豆瓣电影 Top 250】https://movie.douban.com/top250?start=25&filter=
#第三页【豆瓣电影 Top 250】https://movie.douban.com/top250?start=50&filter=
import requests
#from bs4 import BeautifulSoup
from lxml import etree

n=[0,25,50,75,100,125,150,175,200,225]
#n=[0]
for n in n :
	url='https://movie.douban.com/top250?start='+str(n)+'&filter='
	headers={'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_3)AppleWebkit/537.36(KHTML,like Gecko)Chrome/65.0.3325.162 Safari/537.36'}
	html=requests.get(url,headers=headers)
#	soup=BeautifulSoup(html.text,'html.parser')#可以获取网页源代码
#	print(soup.prettify())#可以获取网页源代码
	e=etree.HTML(html.text)
	h=e.xpath('//span[@class="title"][1]/text()')#获取电影名称，自动储存在一个列表内
	p=e.xpath('//em[@class=""]/text()')#获取电影排名，自动储存在一个列表内
	s=e.xpath('//span[@class="rating_num"]/text()')#获取该电影豆瓣评分，自动储存在一个列表内
	lj=e.xpath('//div[@class="hd"]/a/@href')#获取在电影详情页面的链接，自动储存在一个列表内
	for i in range(0,25):
		print('电影排名:'+str(p[i]))#第1次循环时，i=0，获取电影排名列表里的第1个
		print('电影名称:'+str(h[i]))
		print('豆瓣评分:'+str(s[i]))
		print('详情链接:'+str(lj[i]))
		print('='*50)#每循环完一次（即打印出一部电影信息），就打印一行=
