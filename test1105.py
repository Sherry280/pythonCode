'''
列表中添加  删除  修改  查询

'''
# list1 = []
# list2 = ['面包']
# list1.append('火腿肠')
# print(list1)
# list1.append('西瓜')
# # 将list2中元素一个一个进行添加到list1中
# list1.extend(list2)  # 将list2中元素添加到list1中
#
# list2.append('薯条')
# # 将list1，list2进行合并
# list1 = list1 + list2
#print(list1)
'''
加号：用在数字上，字符串上进行拼接，对于列表进行拼接
'''

'''
买多件商品：商品名称，价格，数量
要用到列表的嵌套
# '''
# container = []  # 保存多件商品的一个容器
# flag = True
# while flag:
#     name = input('商品名称：')
#     price = input('商品价格：')
#     number = input('商品数量：')
#     goods = [name, price, number]
#     container.append(goods)
#     answer = input('是否继续添加，按q或者Q退出：')
#     if answer.lower() == 'q':
#         flag = False
# print('*' * 20)
# print('名称\t价格\t数量')
# # 遍历容器里面的元素
# for goods in container:
#     print(goods)
#     print('{}\t{}\t{}'.format(goods[0], float(goods[1]), int(goods[2])))

# 列表的删除  pop  remove   clear
# pop（index）：根据下标删除列表中的元素，下标在写的时候注意不要超出范围 index out 哦福
# pop（）：默认删除最后一个，要是不添加参数的话
# list1 = ['火腿肠', '面包']
# list1.pop(list1[-1])  # 删除的永远是最后一个

# remove：想要删除的元素名称,不是根据下标删除
# list1.remove('面包')
# 判断是否存在要删除的元素：使用in 来进行判断
# if '面包呀' in list1:
#     print('存在')
#     list1.remove('面包')  # 只删除第一个遇到的关键字
# else:
#     print('不存在')

# clear():
# 删除多个相同的元素
# for i in list1:
#     if i=='酸奶':因为它是根据下表进行取值删除，在删除一个之后，下标会变化，所以会跳过一个紧挨着后面的值
#         list1.remove(i)#只要两个关键词连在一块就会露删一个
#
# print(list1)
# n = 0
# while n < len(list1):
#     if list1[n] == '酸奶':
#         list.remove('酸奶')
#     else:
#         n += 1

#使用for来进行删除
# list3=[1,1,1,3,5,1]
# result_i=[]
# index=1
# for i in list3:
#     if list3[i]!=index:
#         result_i.append(list3[i])
# list3=result_i
# print(list3)

#删除的时候也可以倒着取元素，正着删除元素
# li=[2,1,4,5,4,4,4,7]
# for i in li[::1]:
#     if i==4:
#         li.remove(i)
# print(li)


'''
修改：insert
'''
# list1=[1,2,3,4,5]
# list1.insert(1,8)#将8插入到1后面，相当于插队，将原来元素向后移
# print(list1)

# list1=['火腿','酸奶','h','酸奶','酸奶','臭豆腐','酸奶']
# t=0
# for i in list1:
#     if i=='酸奶':
#         list1.remove(i)
#         list.insert(i,str(t))
#         t+=1
# print(list1)

#修改某个位置的元素值：列表[index]=新值
# list1=[]
# list1.clear()#清空列表元素

'''
随机生成8个1-100之间的随机整数，保存到列表中，键盘随机
输入一个1-100之间的整数，将整数插入到排序后的列表中
[1,9,6,8,0]
[0,1,6,8,9]
5
[0,1,5,6,8,9]
'''
import random
list5=[]
for i in range(8):
    ran=random.randint(1,100)
    list5.append(ran)
list5.sort()
print(list5)
a=int(input('请输入一个整数：'))
list5.append(a)
list5.sort()
print(list5)






