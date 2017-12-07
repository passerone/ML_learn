from numpy import *
import matplotlib.pyplot as plt
import csv

#读入文件
def loadDateSet():
    haoMat=[];
    bhaoMat=[];
    fr=open('watermelon.csv')
    for line in csv.DictReader(fr):
        if line['好瓜']=='1':
            haoMat.append([float(line['密度']),float(line['含糖率'])])
        else:
            bhaoMat.append([float(line['密度']),float(line['含糖率'])])
    return haoMat,bhaoMat

def calculate(haoMat,bhaoMat):
    haoMat=mat(haoMat)
    bhaoMat=mat(bhaoMat)
    m1=shape(haoMat)
    m2=shape(bhaoMat)
    print(m1)
    meanhao=mean(haoMat,axis=0)
    meanbhao=mean(bhaoMat,axis=0)
    print(meanhao)
    print(haoMat[1])
    sw=mat(zeros((2,2)))
    print(sw)
    for i in range(m1[0]):
        xm=haoMat[i]-meanhao
        xz=dot(xm.T,xm)
        print(xz)
        sw+=xz
    for i in range(m2[0]):
        xm=bhaoMat[i]-meanbhao
        xz=dot(xm.T,xm)
        sw+=xz
    w=dot((meanhao-meanbhao),sw.I)
    return w

	
haoMat,bhaoMat=loadDateSet()
w=calculate(haoMat,bhaoMat)
print(w)
