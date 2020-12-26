
#准备工作
from numpy import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.datasets import make_blobs
from cmath import sqrt
from numpy.lib.scimath import power
from ipython_genutils.py3compat import xrange

#读取并查看数据表  读取用于聚类的数据并创建名为loan_data的数据表
#loan_data=pd.DataFrame(pd.read_csv('d:\\testSet.csv',header=0))
#查看数据表
#loan_data.head()

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(',')
        print (curLine)
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat
    
#计算两个向量的距离，用的是欧几里得距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

#随机生成初始的质心（ng的课说的初始方式是随机选K个点）    
def randCent(dataSet, k):
    #数组  维数  列
    n = shape(dataSet)[1]
    #66
    centroids = mat(zeros((k,n)))
    print ('centroids',centroids)
    for j in range(n):
        #某列中的最小值
        minJ = min(dataSet[:,j])
        #某列中最大值-最小值
        rangeJ = float(max(array(dataSet)[:,j]) - minJ)
        print ('rangeJ',rangeJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)
    return centroids
    
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    #create mat to assign data points to a centroid, also holds SE of each point
    clusterAssment = mat(zeros((m,2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        #for each data point assign it to the closest centroid
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: 
                clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        for cent in range(k):#recalculate centroids
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent,:] = mean(ptsInClust, axis=0) #assign centroid to mean 
    return centroids, clusterAssment
    
def show(dataSet, k, centroids, clusterAssment):
    #查看矩阵或者数组的维数 ，行数 列数
    numSamples, dim = dataSet.shape
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i, 0])  
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  
    for i in range(k):  
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)  
    plt.show()
      
def main():
    dataMat = mat(loadDataSet('d:\\testSet.csv'))
    myCentroids, clustAssing= kMeans(dataMat,4)
    show(dataMat, 4, myCentroids, clustAssing)  
    
    
if __name__ == '__main__':
    main()
