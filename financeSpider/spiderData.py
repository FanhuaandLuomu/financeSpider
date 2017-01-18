#coding:utf-8
#step1:得到元数据 source 35条左右的url
import requests
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
import time

def getDataFromPage(page):
	idList=[]
	ilist=Selector(text=page).xpath('//*[@id="block_1"]/tbody/tr/td[1]/a/text()')
	for item in ilist:
		#print item.extract()
		idList.append(item.extract())
	return idList

def getId(url,browser):
	browser.get(url)
	idList=[]
	for i in range(68):
		page=browser.page_source
		#time.sleep(0.5)
		idList+=getDataFromPage(page)
		browser.find_element_by_xpath('//*[@id="pageDiv_0"]/span[3]').click()
	print len(idList)
	return idList

def writeIdToFile(filename,idList):
	f=open(filename,'a')
	s='\n'.join(idList)
	f.write(s)
	print '%s write success!' %filename
	f.close()

def writeUrlToFile(filename,urlList):
	f=open(filename,'w')
	s='\n'.join(urlList)
	f.write(s)
	f.close()
	print('%s add success!' %filename)

# 获取数据的来源link
def getSrc(page):
	srcList=[]
	srcs=Selector(text=page).xpath('//*[@id="get_data_div"]/script/@src')
	for item in srcs:
		src=item.extract()
		if(src not in srcList):  #srcList唯一化
			srcList.append(src)
	return srcList

def createUrlList():
	urlList=[]
	for j in range(3):
		browser=webdriver.PhantomJS()
		browser.get('http://finance.sina.com.cn/data/#stock-schq')
		# 每页展示80条信息
		browser.find_element_by_xpath('//*[@id="numberDiv_0"]/a[3]').click()
		# 跳转页数的文本框
		elem=browser.find_element_by_xpath('//*[@id="pageDiv_0"]/input[1]')
		elem.clear()
		# 防止下一页按钮按得过多卡死 分三次爬取链接 1  13  25
		elem.send_keys(12*(j)+1)
		#elem.send_keys(31)
		# 跳转到相关页数
		browser.find_element_by_xpath('//*[@id="pageDiv_0"]/input[2]').click()
		srcL=[]
		if(j==2):
			k=13   # 页数共有38页 随着上市公司增多会变化
		else:
			k=12  # 前两次点击next按钮12次 1~13 13~25 25~38
		for i in range(k):
			page=browser.page_source
			srcList=getSrc(page)
			print('page%d get success!' %(j*12+i+1))
			#urlList+=srcList
			for src in srcList:
				if(src not in srcL):  #唯一化srcL
					srcL.append(src)
			#time.sleep(1)
			print('sleep!')
			# 下一页
			browser.find_element_by_xpath('//*[@id="pageDiv_0"]/span[3]').click()
		
		for src in srcL:
			if(src not in urlList): #唯一化urlList 有点冗余。。以前的代码 现在打上注释存仓库 懒得修改
 				urlList.append(src)	
		#urlList=set(urlList)
		#browser.close()
		browser.quit()
	return urlList
##############################
# if __name__ == '__main__':
# 	urlList=createUrlList()
# 	print len(urlList)
# 	writeUrlToFile('source.txt',urlList)
###################################

	#browser.close()
	#browser.quit()
	#browser==webdriver.Firefox()
	# browser.get('http://finance.sina.com.cn/data/#stock-schq')
	# elem=browser.find_element_by_xpath('//*[@id="pageDiv_0"]/input[1]')
	# elem.send_keys('25')
	# browser.find_element_by_xpath('//*[@id="pageDiv_0"]/input[2]').click()
	# for i in range(10):
	# 	time.sleep(1)
	# 	print('sleep!')
	# 	browser.find_element_by_xpath('//*[@id="pageDiv_0"]/span[3]').click()
	# 	print('page%d' %(i+1))





