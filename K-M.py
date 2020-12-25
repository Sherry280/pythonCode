import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
# from sklearn.cluster import KMeans


# b=type(x,y)
# print(b)
data = pd.read_csv(r"D:\testSet.csv",names =[1,2])
#names:指定列名;<class 数据类型'pandas.core.frame.DataFrame'>
x=np.array(data)
plt.title("Raw Data")
plt.scatter(x[:,0],x[:,1])
plt.show()
#无监督算法，学习过程就是训练质心的位置，进行聚类
class Kmeans:
    #初始化构造函数
    def __init__(self,k):
        self.k = k
        #初始化  k：聚成K个类
    
    def calc_distance(self,x1,x2):
        diff = x1 - x2
        distances = np.sqrt(np.square(diff).sum(axis=1))#欧几里得距离
        #np.square：平方，np.sqrt：平方根
        return distances
    
    #训练模型
    a = 0
    def fit(self,x):
        self.x = x
        m,n = self.x.shape
        #随机选定k个数据作为初始质心，不重复选取
        self.original_ = np.random.choice(m,self.k,replace=False)#随机选取索引值
        #默认类别是从0到k-1
        self.original_center = x[self.original_]
        print("初始质心为：",self.original_center)
        
        a=0
        while True:
            #初始化一个字典，以类别作为key，赋值一个空数组
            y=self.original_center
            dict_y = {}
            for j in range(self.k):
                dict_y[j] = np.empty((0,n))
                #print("字典",dict_y)
                
            for i in range(m):
                distances =self.calc_distance(x[i],self.original_center)
                #把第i个数据分配到距离最近的质心，存放在字典中
                #np.argsort：将元素从小到大排序，返回排序后的下标，[0]：取出数组中的最小值
                label = np.argsort(distances)[0]
                # print("label",label ).
                #np.r_:按列连接两矩阵，上下相加，要求列数相等
                #reshape:将数据变为一行，只指定行数，对列数无要求
                dict_y[label] = np.r_[dict_y[label],x[i].reshape(1,-1)]
        
            y_preds = model.predict(x)
            plt.scatter(x[:,0],x[:,1],c=y_preds)
            plt.plot(y[:,0],y[:,1],'*',color='r')  #打印新的更新后的质心点
            plt.title('Iteration Result:the num%d'%a)
            plt.show()
            
            
            centers = np.empty((0,n))
            #对每个类别的样本重新求质心
            for i in range(self.k):
                center = np.mean(dict_y[i],axis=0).reshape(1,-1)#求平均值
                centers = np.r_[centers,center]
            # 与上一次迭代的质心比较，如果没有发生变化，则停止迭代（也可考虑收敛时停止）
            result = np.all(centers == self.original_center)
            if result == True:
                break
            else:
                #继续更新质心
                a=a+1
                print("第%d次迭代"%a)
                self.original_center = centers
                print("新的质心为：",self.original_center)
                
               
                

    def predict(self,x):
        """
        预测样本属于哪个簇
        X:训练数据特征矩阵，数组类型[样本数量，特征数量]
        返回类数组，每一个x所属的簇
        """#[1,2,3,3,0,3,2,1,...=80]
        y_preds = []
        m,n = x.shape
        for i in range(m):
            distances =self.calc_distance(x[i],self.original_center)
            y_pred = np.argsort(distances)[0]
            y_preds.append(y_pred)
        return y_preds

k=int(input("请输入聚类的个数："))
model = Kmeans(k)
model.fit(x)
y_preds = model.predict(x)
plt.scatter(x[:,0],x[:,1],c=y_preds)
plt.title("Final Result")
plt.show()


# model_1 = KMeans(n_clusters=4)
# y_pred_1 = model_1.fit_predict(x)
# plt.scatter(x[:,0],x[:,1],c=y_pred_1)
# plt.show()