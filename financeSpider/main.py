#coding:utf-8
# author:yinhao
# qq:1049755192 欢迎骚扰 聊学术、动漫、人生
# source site:http://finance.sina.com.cn/data/#stock-schq
# 以前写的一个爬虫小脚本，最近打上注释(灰常详细的注释)，存入仓库...(其实是纪念一下旧时光)
# 代码很烂,不过可以给python爬虫新手作为示例教程,给股票数据研究者一个数据收集的思路..
# 功能：多线程爬取source site中的当天股票数据，并处理成json格式
# 相关：selenium+PhantomJS
#step4: main all time cost 168sec
from spiderData import createUrlList
from spiderData import writeUrlToFile
from IDList import getIDList
from IDList import saveIDList
from saveData import startSpider
from parserData import createFormatData
import time

def main():
	# 1获取数据的来源url
	urlList=createUrlList()
	print len(urlList)
	# 2将抓取的url存入文本文件
	writeUrlToFile('source.txt',urlList)
	# 3从抓取的url中提取股票的id
	idList=getIDList('source.txt')
	print len(idList)
	# 4将股票id保存至文本文件
	saveIDList('ID.txt',idList)

	# 5多线程爬取数据并写入文件
	startSpider()
	# 6raw数据 预处理 形成json格式
	createFormatData('formatData.txt')

if __name__ == '__main__':
	main()

