#coding:utf-8
#step5:将数据提取成规范的格式 Json {'sid':{'name':name,'new':new,...},'sid':{,...}}
from __future__ import division

import os
import re
import time

 #获取每个股票的信息sid:{name:name,...}
def getDataFromFile(path,filename): 
	item={}    
	f=open(path+os.sep+filename,'r')
	line=f.readlines()[0].strip()
	#print line
	dataStr=re.findall(r'="(.*)";',line,re.S)[0]
	#print dataStr   
	# sid=filename.split('_')[0]  #股票sid
	# print sid   
	dataList=dataStr.split(',')
	#print len(dataList)
	if(len(dataList)==33):
		#name=dataList[0]    #name
		today=dataList[1]    #today
		yesterday=dataList[2]   #yesterday
		new=dataList[3]        #new
		high=dataList[4]       #high
		low=dataList[5]        #low
		buy=dataList[6]        #buy
		sale=dataList[7]         #sale
		tradeCount=dataList[8]   #tradeCount
		tradeCount=int(round(float(tradeCount)/100))
		tradeSum=dataList[9]      #tradeSum
		tradeSum=(round(float(tradeSum)/100))/100
		addCount=float(new)-float(yesterday)
		addRate=addCount/float(yesterday)
		addRate=str(int(round(addRate*10000))/100)+'%'
	else:
		#name='0'   #name
		today='0'   #today
		yesterday='0'   #yesterday
		new='0'      #new
		high='0'     #high
		low='0'        #low
		buy='0'      #buy
		sale='0'        #sale
		tradeCount='0'   #tradeCount
		tradeSum='0'      #tradeSum
		addCount='0'
		addRate='0'
	#item['name']=name
	item['today']=today
	item['yesterday']=yesterday
	item['new']=new
	item['high']=high
	item['low']=low
	item['buy']=buy
	item['sale']=sale
	item['tradeCount']=str(tradeCount)
	item['tradeSum']=str(tradeSum)
	item['addCount']=str(addCount)
	item['addRate']=addRate
	return item

def createFormatData(savefile):  #整合数据 dict
	dataList=[]
	  
	t=time.localtime()
	y=t.tm_year
	m=t.tm_mon
	d=t.tm_mday
	path='%d_%d_%d' %(y,m,d)
	for filename in os.listdir(path):
		#print filename
		item={}
		sid=filename.split('_')[0]  #股票sid
		print sid 
		item[sid]=getDataFromFile(path,filename)
		dataList.append(item)
		#print item[sid]['name']
		#print item
		
	#以json形式写入文件
	f=open(path+os.sep+savefile,'w')
	f.write('{')
	for item in dataList[:-1]:
		s=str(item)[1:-1]
		s=s.replace("'",'"')
		#print s
		f.write(s+',\n')
	f.write(str(dataList[-1])[1:-1].replace("'",'"')+'}')
	f.close()
	print len(dataList)

if __name__ == '__main__':
	#item=getDataFromFile('2015_12_6','sh600005_11_43_46.txt')
	# for key in item:
	# 	print key,item[key]
	createFormatData('formatData.txt')