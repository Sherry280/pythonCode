import numpy as np
from sklearn.linear_model import LinearRegression

#噪音比较小

rng = np.random.RandomState(10)   # 设置随机局部种子
x = 100 * rng.rand(50, 4)     #设置一个50行 4列  所有值乘100的随机矩阵
x1=x[:,0]
x1.shape=50,1
x2=x[:,1]
x2.shape=50,1
x3=x[:,2]
x3.shape=50,1   
x4=x[:,3]
x4.shape=50,1
y = 1.25*x1+2.5*x2+3*x3+3.5*x4-20+5*rng.randn(50,1)#randn是标准正态分布   噪音设置为5
 

model = LinearRegression(fit_intercept=True)  
 #参数：是否要截距b LinearRegression线性回归
model.fit(x, y)#x和y的每一行是一个样本，即要求是列向量
  # 将真实数据传入到图中，构成回归模型
a = np.linspace(0,50,1000)    #从0到50创建1000个等差数列，验证模型
x1_fit= a[:,np.newaxis]       #将a转置成列
x2_fit =a[:,np.newaxis]
x3_fit =a[:,np.newaxis]
x4_fit =a[:,np.newaxis]
x_fit = np.hstack((x1_fit,x2_fit,x3_fit,x4_fit))    #将x1，x2，x3合并一起
y_fit = model.predict(x_fit)      #根据x对y的预测
print("Model slope: ", model.coef_[0])   #系数
print("Model intercept:", model.intercept_)   #截距
print('方程的判定系数(R^2): %.6f' % model.score(x, y))   
 
  #运行结果：可以明显地看出来模型运算结果的截距和自己设置的截距是基本一样的，判定系数
  #无限接近于1，那就说明这个模型是好的
  
  
  
rng = np.random.RandomState(10)   # 设置随机局部种子
x = 100 * rng.rand(50, 4)     #设置一个50行 3列  所有值乘100的随机矩阵
x1=x[:,0]
x1.shape=50,1
x2=x[:,1]
x2.shape=50,1
x3=x[:,2]
x3.shape=50,1   
x4=x[:,3]
x4.shape=50,1
y = 1.25*x1+2.5*x2+3*x3+3.5*x4-20+100*rng.randn(50,1)#randn是标准正态分布  加大了噪音
 

model = LinearRegression(fit_intercept=True)  
 #参数：是否要截距b LinearRegression线性回归
model.fit(x, y)#x和y的每一行是一个样本，即要求是列向量
  # 将真实数据传入到图中，构成回归模型
a = np.linspace(0,50,1000)    #从0到50创建1000个等差数列
x1_fit= a[:,np.newaxis]       #将a转置成列
x2_fit =a[:,np.newaxis]
x3_fit =a[:,np.newaxis]
x4_fit =a[:,np.newaxis]
x_fit = np.hstack((x1_fit,x2_fit,x3_fit,x4_fit))    #将x1，x2，x3合并一起
y_fit = model.predict(x_fit)      #根据x对y的预测
print("Model slope: ", model.coef_[0])   #系数
print("Model intercept:", model.intercept_)   #截距
print('方程的判定系数(R^2): %.6f' % model.score(x, y))   
 
  #运行结果：可以明显地看出来模型运算结果的截距和自己设置的截距是基本一样的，判定系数
  #无限接近于1，那就说明这个模型是好的
  
  
  
  
  
  
  
  


