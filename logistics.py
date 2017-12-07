from numpy import *
import matplotlib.pyplot as plt
import csv

#读入文件
def loadDateSet():
	dataMat=[];
	labelMat=[];
	fr=open('watermelon.csv')
	for line in csv.DictReader(fr):
		dataMat.append([1.0,float(line['密度']),float(line['含糖率'])])
		labelMat.append(int(line['好瓜']))
	return dataMat,labelMat

#sigmoid函数
def sigmoid(inX):
	return 1.0/(1+exp(-inX))
	
#梯度上升算法(牛顿法)
def gradAsent(dataMatIn,classLabels):
	dataMat=mat(dataMatIn)
	labelMat=mat(classLabels).transpose()
	m,n=shape(dataMat)
	alpha=0.5
	maxcycle=500
	weigths=array(ones((n,1)))
	for k in range(maxcycle):
		h=sigmoid(dot(dataMat,weigths))
		error=(labelMat-h)
		weigths=weigths+alpha*dot(dataMat.transpose(),error)
	return weigths
	
def plotBestFit(weigths):
	dataMat,labelMat=loadDateSet()
	dataArr=array(dataMat)
	n=shape(dataArr)[0]
	xcord1=[];ycord1=[]
	xcord2=[];ycord2=[]
	for i in range(n):
		if int(labelMat[i])==1:
			xcord1.append(dataArr[i,1]);ycord1.append(dataArr[i,2])
		else:
			xcord2.append(dataArr[i,1]);ycord2.append(dataArr[i,2]);
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
	ax.scatter(xcord2,ycord2,s=30,c='green')
	x=arange(0.2,0.8,0.1)
	y=array((-weigths[0]-weigths[1]*x)/weigths[2])
	print(x)
	print(y[0])
	ax.plot(x,y[0])
	plt.xlabel('密度')
	plt.ylabel('含糖率')
	plt.show()
	
	
dataMat,labelMat=loadDateSet()
weigths=gradAsent(dataMat,labelMat)
plotBestFit(weigths)
