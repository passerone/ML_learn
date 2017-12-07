from math import log
import matplotlib.pyplot as plt
import operator

def createdataset():
    dataset=[[1,1,'yes'],
             [1,1,'yes'],
             [1,0,'no'],
             [0,1,'no'],
             [0,0,'no']]
    labels=['no surfacing','flippers']
    return dataset,labels

def calcshannonent(dataset):
    numentries = len(dataset)
    labelcount = {}
    for featvec in dataset:
        currentlabel = featvec[-1]
        if currentlabel not in labelcount.keys():
            labelcount[currentlabel]=0
        labelcount[currentlabel]+=1
    shannonent = 0.0
    for key in labelcount:
        prob = float(labelcount[key])/numentries
        shannonent -=prob*log(prob,2)
    return shannonent

def splitdataset(dataset,axis,value):
    retdataset=[]
    for featvec in dataset:
        if featvec[axis]==value:
            reducedfeatvec=featvec[:axis]
            reducedfeatvec.extend(featvec[axis+1:])
            retdataset.append(reducedfeatvec)
        return retdataset

def choosebestfeaturetosplit(dataset):
    numentries=len(dataset[0])-1
    baseentropy = calcshannonent(dataset)
    bestinfogain = 0.0; bestfeature=-1
    for i in range(numentries):
        featlist = [example[i] for example in dataset]
        uniquevals = set(featlist)
        newentropy=0.0
        for value in uniquevals:
            subdataset = splitdataset(dataset,i,value)
            prob = len(subdataset)/float(len(dataset))
            newentropy += prob*calcshannonent(subdataset)
        infogain = baseentropy - newentropy
        if (infogain>bestinfogain):
            bestinfogain = infogain
            bestfeature=i
    return bestfeature

def majoritycnt(classlist):
    classcount={}
    for vote in classlist:
        if vote not in classcount.keys():
            classcount[vote]=0
        classcount[vote]+=1
    sortedclasscount = sorted(classcount.items(),\
                              key=operator.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]

def createtree(dataset,labels):
    classlist = [example[-1] for example in dataset]
    if classlist.count(classlist[0])==len(classlist):
        return classlist[0]
    if len(dataset[0])==1:
        return majoritycnt(classlist)
    bestfeat= choosebestfeaturetosplit(dataset)
    bestfeatlabel=labels[bestfeat]
    mytree = {bestfeatlabel:{}}
    del(labels[bestfeat])
    featvalues = [example[bestfeat] for example in dataset]
    uniquevals = set(featvalues)
    for value in uniquevals:
        sublabels = labels[:]
        mytree[bestfeatlabel][value]=createtree(splitdataset\
                                                (dataset,bestfeat,value),sublabels)
    return mytree

def classify(inputtree,featlabels,testvec):
    firstvec=list(inputtree.keys())
    firststr=firstvec[0]
    seconddict=inputtree[firststr]
    featindex=featlabels.index(firststr)
    for key in seconddict.keys():
        if testvec[featindex]==key:
            if type(seconddict[key]).__name__=='dict':
                classlabel=classify(seconddict[key],featlabels,testvec)
            else: classlabel=seconddict[key]
    return classlabel

def storetree(inputtree,filename):
    import pickle
    fw=open(filename,'w')
    pickle.dump(inputtree,fw)
    fw.close()

def grabtree(filename):
    import pickle
    fr=open(filename)
    return pickle.load(fr)
