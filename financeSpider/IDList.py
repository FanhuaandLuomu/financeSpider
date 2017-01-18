#coding:utf-8
#step2:从source中提取唯一的id all 2752
import re

# 使用正则表达式提取url中的股票id
def getIdFromUrl(url):
	ulist=[]
	cont=re.findall(r'&list=(.*)',url)[0]
	#print cont
	ulist=cont.split(',')
	return ulist

def getIDList(filename):
	idList=[]
	for line in open(filename,'r'):
		#print line
		ilist=getIdFromUrl(line)
		for item in ilist:  #唯一化idList
			if item not in idList:
				idList.append(item)
	return idList

def saveIDList(filename,idList):
	f=open(filename,'w')
	f.write('\n'.join(idList))
	f.close()

####################################
# if __name__ == '__main__':
# 	idList=getIDList('source.txt')
# 	print len(idList)
# 	saveIDList('ID.txt',idList)
###########################
