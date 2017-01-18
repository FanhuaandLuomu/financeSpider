#coding:utf-8
#step3:根据抓到的股票ID来抓取该id对应的信息 多线程 8进程 43sec!
import requests
import time
import os
import threading

def getAndSaveSource(url,sid,rootPath):
	t=time.localtime()
	# y=t.tm_year
	# m=t.tm_mon
	# d=t.tm_mday
	# rootPath='%d_%d_%d' %(y,m,d)
	# print 'rootPath:'+rootPath   #当天数据的文件夹名
	# if(os.path.exists('./%s' %rootPath)==False):
	# 	os.mkdir('./%s' %rootPath)
	h=t.tm_hour
	mi=t.tm_min
	sec=t.tm_sec
	filename='%s_%d_%d_%d.txt' %(sid,h,mi,sec)
	print 'filename:'+filename  #保存数据源的文件名

	html=requests.get(url).content
	#print(html)
	f=open(rootPath+os.sep+filename,'w')
	f.write(html)
	print('%s/%s write ok!\n' %(rootPath,filename))
	f.close()

def getAllUrl(filename):
	rootUrl='http://hq.sinajs.cn/?func=getData._hq_cron();&list='
	idList=[]
	s=open(filename,'r').read()
	idList=s.split()
	for item in idList:
		rootUrl+=(item+',')
	url=rootUrl[:-1]
	print 'url:'+url
	return url

def getSingleUrl(filename):
	#rootUrl='http://hq.sinajs.cn/?func=getData._hq_cron();&list='
	urlList=[]
	for line in open(filename,'r'):
		#url=rootUrl+line
		line=line.strip()  #careful!!
		urlList.append(line)
		#print line
	return urlList

def multiSpider(urllistSon,label,rootPath):
	for i,sid in enumerate(urllistSon):
		url='http://hq.sinajs.cn/?func=getData._hq_cron();&list='+sid
		print 'thread_%d_url%d:'%(label,i+1)+url
		# 爬取数据并写入相应文件
		getAndSaveSource(url,sid,rootPath)

def startSpider():
	# 日期
	t=time.localtime()
	y=t.tm_year
	m=t.tm_mon
	d=t.tm_mday
	rootPath='%d_%d_%d' %(y,m,d)
	print 'rootPath:'+rootPath   #当天数据的文件夹名
	if(not os.path.exists('./%s' %rootPath)):
		os.mkdir('./%s' %rootPath)
	# 从文件读取id
	urlList=getSingleUrl('ID.txt')
	# 将id分组，350个id为一组 多线程爬取
	urlList1=urlList[:350]
	urlList2=urlList[350:700]
	urlList3=urlList[700:1050]
	urlList4=urlList[1050:1400]
	urlList5=urlList[1400:1750]
	urlList6=urlList[1750:2100]
	urlList7=urlList[2100:2450]
	urlList8=urlList[2450:]
	tmpList=[urlList1,urlList2,urlList3,urlList4,urlList5,urlList6,urlList7,urlList8]

	threads=[]
	# t1=threading.Thread(target=multiSpider,args=(urlList1,1,rootPath))
	# threads.append(t1)
	# t2=threading.Thread(target=multiSpider,args=(urlList2,2,rootPath))
	# threads.append(t2)
	# t3=threading.Thread(target=multiSpider,args=(urlList3,3,rootPath))
	# threads.append(t3)
	# t4=threading.Thread(target=multiSpider,args=(urlList4,4,rootPath))
	# threads.append(t4)
	# t5=threading.Thread(target=multiSpider,args=(urlList5,5,rootPath))
	# threads.append(t5)
	# t6=threading.Thread(target=multiSpider,args=(urlList6,6,rootPath))
	# threads.append(t6)
	# t7=threading.Thread(target=multiSpider,args=(urlList7,7,rootPath))
	# threads.append(t7)
	# t8=threading.Thread(target=multiSpider,args=(urlList8,8,rootPath))
	# threads.append(t8)
	for i in xrange(len(tmpList)):
		t=threading.Thread(target=multiSpider,args=(tmpList[i],i+1,rootPath))
		threads.append(t)

	for t in threads:
		t.start()
	t.join()

###########################
# if __name__ == '__main__':
# 	#url=getAllUrl('ID.txt') #全部获取
# 	#getAndSaveSource(url)
# 	startSpider()
####################################
	


