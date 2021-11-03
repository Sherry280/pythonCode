# n = 1
# while n <= 5:
#     m = 0
#     while m < n:
#         print('*', end='')
#         m += 1
#     n += 1
# 1+2+3+4+5=15
# 打印一个直角三角形
# n =0
# while n<5:
#     m=0
#     while m<=n:
#         print("*",end='')
#         m+=1
#     n+=1
#     print()

# 打印一个倒立的直角三角形
# n=5
# while n>0:
#     m=1
#     while m<=n:
#         print("*",end='')
#         m+=1
#     n-=1
#     print()
# '''
# 索引机制：1.索引范围：0~len(s1)-1
# 2.-len(s1)-1 -  -1
# 切片：字符串和列表
# step:1.步长；2.方向：正数：表示从左向右；负数：表示从右向左
#
# '''
# import random
#
# s1 = 'ABCDEFG'
# print(s1[-1], s1[6])
#
# print(s1[1:4])
# print(s1[:4])  # 起始可以省略
# print(s1[-3:-1])  # 切片也要注意切的方向
#
# print(s1[:-1:2])  # 注意切片包前不包后
# print(s1[1::2])  # 打印BDF
# print(s1[::4])
# print(s1[::-1])  # 逆向打印
# print(s1[::-2])  # GECA
# print(s1[:-1:-2])  # 起始位置为0，从右向左取数字，一个都取不到
# # print(s1[1:4:-2])#方向冲突，取不到任何值
# print(s1[-1:-6:-4])
#
# # 产生随机字母和数字,就是我们登录的时候出现的验证码
# filename = ''
# s = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
# for i in range(4):
#     index = random.randint(0, len(s) - 1)
#     filename += s[index]
# print(filename)
#
# # 判断是否是纯字母
# s = 'who'
# result = s.isalpha()
# print(result)  # True
#
# # 判断是否是纯数字
# s = '1234'
# result = s.isdigit()
# print(result)  # True
#
# # 判断是否包含数字或者字母，返回true不能有其他特殊字符
# # ,调用.isalnum()方法的时候必须是字符串
# a = 'A1234'
# result = a.isalnum()
# print(result)  # True
#
# # 判断是否是由纯空格组成s.isspace，如果为空返回false
# # 必须是要有空格
# s = ''
# result = s.isspace()
# print(result)
#
# # 判断是否全部是大写字母
# s = 'HELLO'
# result = s.isupper()
# print(result)
#
# # 判断是否全部由小写字母组成
# s = 'hello'
# result = s.lower()
# print(result)
'''
用户名或者手机号码登录+密码
# 用户名：全部小写，首字母不能是数字，长度必须6位以上
# 手机号码：纯数字 长度为11位
# 密码必须是6位数字
# 以上满足条件则进入下层验证：判断用户名+密码 是否正确
# 成功则登录成功，否则失败
用户名：xingyuyu123  手机号：13484627284  密码：131415


'''
# flag = True
# while flag:
#     username = input('用户名/手机号码：')
#     # 验证用户名和手机号码的格式是否正确
#     if (username.islower() and username[0].isalpha() and len(username) >= 6) or (
#             username.isdigit() and len(username) == 11):
#         #
#         while True:
#             # 继续输入密码 多次输入
#             password = input('请输入密码：')
#             # 判断是否是纯6位数字组成
#             if password.isdigit() and len(password) == 6:
#                 if (username == 'xingyuyu123' or username == '13484627284') and password == '131415':
#                     print("用户登录成功")
#                     flag = False
#                     break
#                 else:
#                     print('用户名或者密码错误')
#                     break
#             else:
#                 print('密码必须是6位数字')
#     else:
#         print('用户名或者手机格式错误')

#字符串替换
# s='阿泽：德善，你真好看，德善，你真漂亮'
# s=s.replace('德善','**',1)#默认是有几个就替换几个，但是如果指定数字，就只替换指定数字的几个
# print(s)

#split('分隔符',maxsplit(最多分割次数）)返回一个列表
# s='娟娟 胖墩 老谢'
# # result=s.rsplit(' ')
# # print(result)
# # result=s.split(' ')
# # print(result)

#
# s='''胖墩
# 老谢
# 娟娟
# 老杨
# '''
# result=s.splitlines()# 按行进行切割形成一个列表
# print(result)
#
# s='娟娟 胖墩 劳希尔'
# result=s.partition(' ')#按照输入的字符将内容分为三部分，分隔符作为一部分
# print(result)
#
# #大小写转换
# s='hello'
# result=s.title()
# print(result)
# result=s.upper()
# print(result)
# result=s.lower()
# print(result)
#
# username=input('请输入用户名：')#注册输入包含空格的时候，会把空格计算在内
# print(len(username))
# #真实场景中，应该对用户输入的空格进行处理
# s=' admin '
# print(len(s))
# result=s.strip()
# print(result)
# result=s.lstrip()#只去除左侧空格
# print(result)
# result=s.rstrip()#只去除右侧空格
# print(result)
# #调整对齐方式用：center
# s='  hello  world '
# result=s.center(30)#在30个给定字符中，将指定内容置于正中央
# print(result)
#
# result=s.ljust(30)#左对齐
# print(result)
#
# result=s.rjust(30)
# print(result)

#字符串拼接：join
#其实是将两个列表进行拼接，最终返回一个字符串


#格式化：
'''
1. %d %s %f 
2.format

'''
name='赵丽颖'
age=18
print('美女%s今年%d岁了'%(name,age))
result='美女{}今年{}岁了'.format(name,age)
print(result)

#数字字段名
#可以通过数字形式的简单字段名传递位置参数


