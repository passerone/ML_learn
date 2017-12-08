import xlrd
from numpy import *

def sigmoid(x,deriv=False):
    if (deriv==True):
        return x*(1-x)
    return 1/(1+exp(-x))

def loaddata(filename):
    datamat=[]
    fr=open(filename)
    for line in fr.readlines():
        curline = line.strip().split(',')
        datamat.append(curline)
    return datamat

def datachange(datamat):
    m,n = shape(datamat)
    for i in range(m):
        for j in range(n):
            if datamat[i][j] == '青绿': datamat[i][j] = 0
            if datamat[i][j] == '乌黑': datamat[i][j] = 1
            if datamat[i][j] == '浅白': datamat[i][j] = 2
            if datamat[i][j] == '蜷缩': datamat[i][j] = 0
            if datamat[i][j] == '稍蜷': datamat[i][j] = 1
            if datamat[i][j] == '硬挺': datamat[i][j] = 2
            if datamat[i][j] == '浊响': datamat[i][j] = 0
            if datamat[i][j] == '沉闷': datamat[i][j] = 1
            if datamat[i][j] == '清脆': datamat[i][j] = 2
            if datamat[i][j] == '清晰': datamat[i][j] = 0
            if datamat[i][j] == '稍糊': datamat[i][j] = 1
            if datamat[i][j] == '模糊': datamat[i][j] = 2
            if datamat[i][j] == '凹陷': datamat[i][j] = 0
            if datamat[i][j] == '稍凹': datamat[i][j] = 1
            if datamat[i][j] == '平坦': datamat[i][j] = 2
            if datamat[i][j] == '硬滑': datamat[i][j] = 0
            if datamat[i][j] == '软粘': datamat[i][j] = 1
            if datamat[i][j] == '否': datamat[i][j] = 0
            if datamat[i][j] == '是': datamat[i][j] = 1
            datamat[i][j]=float(datamat[i][j])
    data=datamat[:][1:n]
    return mat(data)

class NeuralNetwork:
    def __init__(self,layers):
        '''
        :param layers: list [input num,hide num,output num]
        :param activation: activation funtion
        '''

        self.layers = layers
        self.num_layers = len(layers)



class Neuron:
    def __init__(self,len_input):
        self.weight=random.rand((len_input,1))*0.1
        self.offset=0

        self.input = np.ones(len_input)
        # 对下一层的输出值
        self.output = 1
        # 误差项
        self.deltas_item = 0

    def get_back_weight(self):
        # 获取反馈差值
        return self.weights * self.deltas_item

    def update(self,dweight,doffset):
        self.dweight+=dweight
        self.offset+=doffset

    def calcout(self,input):
        output=sigmoid(dot(input,self.weight))
        return output

class NetLayer:
    def __init__(self,layer_name,len_node,len_input):
        '''
        :param layer_name: 'Hidden' or 'Output'
        :param len_node:
        :param len_input:
        '''
        self.neurons=[Neuron(len_input) for _ in fange(len_node)] #对于无需关注其实际含义的变量可以用_代替
        self.next_layer = None   # 记录下一层的引用，方便递归操作
        self.layer_name = layer_name

    def calcout(self,input):
        output = array([ node.calcout(input) for node in self.neurons])
        if self.next_layer is not None:
            return self.next_layer.calc_output(output)
        return output

    def get_back_weight(self):
        return sum([node.get_back_weight() for node in self.neurons])

    def update(self,input,labels,learning_rate):
        if self.layer_name == 'Output':
            back_weight = zeros(len(self.neurons))
        elif self.layer_name == 'Hidden':
            back_weight = self.next_layer.update(input,labels,learning_rate)



            dweight = learning_rate*sigmoid(self.calcout(input),True)*(labels-self.calcout(input))*input
            doffset = -1*learning_rate*sigmoid(self.calcout(input),True)*(labels-self.calcout(input))
        elif self.layer_name == 'Hidden':
            dweight = learning_rate*sigmoid(self.calcout(input),True)*(labels-self.calcout(input))*input
            doffset =

if __name__=='__main__':
    mydat=loaddata('xiguan30.txt')
    mydata=datachange(mydat)
    m,n=shape(mydata)
    random.seed(1)   #你的随机数设定产生种子是一个良好的习惯。这样一来，你得到的权重初始化集仍是随机分布的，但每次开始训练时，得到的权重初始集分布都是完全一致的。
    syn0=random.rand(n-1,n)
    syn1=random.rand(n,1)
    eta=1
    a=mat(ones((1,n)))*(-1)
    nsyn0=vstack((syn0,a))
    nsyn1=vstack((syn1,a))
    theta=mat(zeros((m,n)))
    gamma=mat(zeros((m,1)))    #阈值作为系数为-1的特征带入计算

    l0=hstack((mydata[:,:-1],theta))
    l1=hstack((sigmoid(dot(l0,syn0)),gamma))
    l2=sigmoid(dot(l1,syn1))

    l2error=mydata[:,-1]-l2
    dsyn0=eta*sigmoid(l2,True)*l2error*l1
    dsyn1=-1*eta*sigmoid(l1,True)*l2_delta.dot(syn1.T)
    dtheta=-1*eta*sigmoid(l2,True)*l2error*mydata[:,:-1]
    for i in range(1):
        syn1[:,j] += dtheta
    for j in range(n):
        syn0[:,k] += dgamma






