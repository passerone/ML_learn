import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #正常显示中文

decisionnode = dict(boxstyle="sawtooth",fc="0.8")
leafnode=dict(boxstyle="round4",fc="0.8")
arrow_args=dict(arrowstyle="<-")

def plotnode(nodetxt,centerpt,parentpt,nodetype):
    createPlot.ax1.annotate(nodetxt,xy=parentpt,xycoords='axes fraction',
                            xytext=centerpt,textcoords='axes fraction',
                            va="center",ha="center",bbox=nodetype,arrowprops=arrow_args)

def plotmidtext(cntrpt,parentpt,txtstring):
    xmid=(parentpt[0]-cntrpt[0])/2.0+cntrpt[0]
    ymid=(parentpt[1]-cntrpt[1])/2.0+cntrpt[1]
    createPlot.ax1.text(xmid,ymid,txtstring)

def plottree(mytree,parentpt,nodetxt):
    numleafs=getnumleaf(mytree)
    depth=gettreedepth(mytree)
    firstside = list(mytree.keys())
    firststr=firstside[0]
    cntrpt=(plottree.xoff+(1.0+float(numleafs))/2.0/plottree.totalw,plottree.yoff)
    plotmidtext(cntrpt,parentpt,nodetxt)
    plotnode(firststr,cntrpt,parentpt,decisionnode)
    seconddict=mytree[firststr]
    plottree.yoff=plottree.yoff-1.0/plottree.totald
    for key in seconddict.keys():
        if type(seconddict[key]).__name__=='dict':
            plottree(seconddict[key],cntrpt,str(key))
        else:
            plottree.xoff=plottree.xoff + 1.0/plottree.totalw
            plotnode(seconddict[key],(plottree.xoff,plottree.yoff),cntrpt,leafnode)
            plotmidtext((plottree.xoff,plottree.yoff),cntrpt,str(key))
    plottree.yoff=plottree.yoff+1.0/plottree.totald


def createPlot(intree):
    fig=plt.figure(1,facecolor='white')
    fig.clf()
    axprops=dict(xticks=[],yticks=[])
    createPlot.ax1=plt.subplot(111,frameon=False,**axprops)
    plottree.totalw=float(getnumleaf(intree))
    plottree.totald = float(gettreedepth(intree))
    plottree.xoff=-0.5/plottree.totalw
    plottree.yoff=1.0
    plottree(intree,(0.5,1.0),'')
    plt.show()

def getnumleaf(mytree):
    numleafs=0
    firstside = list(mytree.keys())
    firststr=firstside[0]
    seconddict=mytree[firststr]
    for key in seconddict.keys():
        if type(seconddict[key]).__name__=='dict':
            numleafs+=getnumleaf(seconddict[key])
        else:
            numleafs+=1
    return numleafs

def gettreedepth(mytree):
    maxdepth=0
    firstside = list(mytree.keys())
    firststr=firstside[0]
    seconddict=mytree[firststr]
    for key in seconddict.keys():
        if type(seconddict[key]).__name__=='dict':
            thisdepth = 1+gettreedepth(seconddict[key])
        else:
            thisdepth = 1
        if thisdepth>maxdepth: maxdepth=thisdepth
    return maxdepth

def retrievetree(i):
    listoftrees=[{'no surfacing':{0:'no',1:{'flippers':\
                    {0:'No',1:'yes'}}}},
                 {'no surfacing':{0:'no',1:{'flippers':\
                    {0:{'head':{0:'no',1:'yes'}},1:'no'}}}}
                 ]
    return listoftrees[i]

