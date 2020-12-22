import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#%% 当噪声较小时

rng = np.random.RandomState(10)   # 设置随机局部种子
x =rng.normal(100,100,50) #正态分布 （均值、标准差、返回数的个数）
x =x[:, np.newaxis]    #增加维度
 # 人为的设置真实的Y一列，np.random.randn(100, 1)是设置error
y = 1.25 * x - 20 + 5 * rng.randn(50, 1) #预测y=1.25x-20
# randn是标准正态分布，randn函数返回的是一个或一组样本，shape（50，1）

model = LinearRegression(fit_intercept=True)  
 #参数：是否要截距b LinearRegression线性回归
model.fit(x, y)#x和y的每一行是一个样本，即要求是列向量
  # 将真实数据传入到图中，构成回归模型

x_fit = np.linspace(min(x), max(x), 1000) #linspace：在指定的间隔内返回均匀间隔的数字
#x_fit =x_fit[:, np.newaxis]
y_fit = model.predict(x_fit)  #根据模型预测y_fit的值

print("Model slope: ", model.coef_[0])  #输出斜率
print("Model intercept:", model.intercept_)  #输出截距
print('方程的判定系数(R^2): %.6f' % model.score(x, y))   #准确率的得分
plt.figure(figsize=(16, 12))
plt.scatter(x, y, s=10, c='k', marker='.')
plt.plot(x_fit, y_fit)
ax = plt.gca()   #获得当前对象
ax.set_aspect("equal")    # 纵横坐标单位相同
plt.grid(True) #网格
plt.xlabel('x')
plt.ylabel('y')
plt.title('noise is samll')
plt.show()

#%% 当噪声较大时

rng = np.random.RandomState(10)   # 设置随机局部种子
x =rng.normal(100,100,50)
x =x[:, np.newaxis]
y = 1.25 * x - 20 + 100 * rng.randn(50, 1)   # 加大了噪声 （真实值）

model = LinearRegression(fit_intercept=True)
model.fit(x, y)  # x,y的每一行是一个样本，即要求是列向量

x_fit = np.linspace(min(x), max(x), 1000)
#x_fit =x_fit[:, np.newaxis]
y_fit = model.predict(x_fit) #（预测值）
print("Model slope: ", model.coef_[0])
print("Model intercept:", model.intercept_)
print('方程的判定系数(R^2): %.6f' % model.score(x, y))
plt.figure(figsize=(16, 12))
plt.scatter(x, y, s=10, c='k', marker='.')
plt.plot(x_fit, y_fit)
ax = plt.gca()
ax.set_aspect("equal")    # 纵横坐标单位相同
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('noise is big')
plt.show()
