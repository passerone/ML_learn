from numpy import *

def sigmoid(x,deriv=False):
    if (deriv==True):
        return multiply(x,1-x)
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
    datamat=mat(datamat)
    data=datamat[:,1:n-1]
    labels = datamat[:,-1]
    return data,labels



class NeuralNetwork:
    def __init__(self,layers,learning_rate=1):
        '''
        :param layers: list [input num,hide num,output num]
        :param activation: activation funtion
        '''
        self.input_nodes = layers[0]
        self.hidden_nodes = layers[1]
        self.output_nodes = layers[2]

        self.weight_i2h = random.rand(self.input_nodes+1,self.hidden_nodes)
        self.weight_h2o = random.rand(self.hidden_nodes+1,self.output_nodes)
        self.lr = learning_rate

    def dataxiu(self,inputset):
        bias = ones([len(inputset),1])
        inputset = hstack((inputset,bias))
        return inputset

    def train(self,inputset,labels,limit=10000):
        inputset = self.dataxiu(inputset)
        for i in range(limit):
            for j in range(len(inputset)):
                #forword pass
                #hidden layer
                hidden_inputs = dot(inputset[j],self.weight_i2h)
                hidden_outputs = sigmoid(hidden_inputs)

                #output layer
                pre_final_inputs = self.dataxiu(hidden_outputs)
                final_inputs = dot( pre_final_inputs,self.weight_h2o)
                final_outputs = sigmoid(final_inputs)
                #backward pass

                output_errors = labels[j] - final_outputs
                hidden_errors = dot(output_errors,self.weight_h2o.T)
                hidden_errors=hidden_errors[:,0:-1]


                output_delta = multiply(output_errors,sigmoid(final_outputs,True))
                hidden_delta = multiply(hidden_errors,sigmoid(hidden_outputs,True))
                # update weight
                self.weight_h2o += (output_delta*pre_final_inputs).T*self.lr
                self.weight_i2h += dot(inputset[j].T,hidden_delta)*self.lr


        print ('trained over!')

    def predict(self,inputlist):
        #forward pass
        inputlist = self.dataxiu(inputlist)
        # hidden layer
        hidden_inputs = dot(inputlist,self.weight_i2h)
        hidden_outputs = sigmoid(hidden_inputs)
        # output layer
        pre_final_inputs = self.dataxiu(hidden_outputs)
        final_inputs = dot(pre_final_inputs,self.weight_h2o)
        final_outputs = sigmoid(final_inputs)
        return final_outputs

if __name__ == '__main__':
    mydata=loaddata('xiguan30.txt')
    input,labels = datachange(mydata)
    #input=mat([[0,1],[1,0],[0,0],[1,1]])
    #labels = mat([[0],[0],[1],[1]])
    m,n = shape(input)
    nn = NeuralNetwork((n,n+10,1),2)
    nn.train(input,labels)
    result=nn.predict(input)
    print(result)

