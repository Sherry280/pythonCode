'''
将列表[1,2,3...100]进行分割为[1,2,3],[4,5,6]...

'''
# list=[i for i in range(1,101)]
# list=[]
# list1=[]
# for i in range(1,101):
#     list1.append(i)
#     if len(list1)==3:
#         list.append(list1)
#         list1=[]
#     #当最后一个不足三个元素的时候
# list.append([100])

# if count>0:
#     list1.append(i)
#     count-=1
# else:
#     count=3
#     #     list.append(list1)
# print(list)
#
#
# #方法2：可以利用切片
# a=[x for x in range(1,101)]
# b=[a[x:x+3] for x in range(0,len(a),3)]
# print(b)

# 方法3：
# list=[[i,i+1,i+2] if i<=98 else [i for i in range(i,101)] for i in range(1,101,3)]
# print(list)


# 函数的使用
import random


def generate_code(n):
    # 生成随机验证码
    s = '1234567890'
    code = ''
    for i in range(n):
        r = random.choice(s)
        code += r
    print(code)


# <function generate_code at 0x000002181375C378>
print(generate_code)  # 加载给函数分配一块内存空间，不会执行
# 验证函数是否可用？调用函数
generate_code(4)

'''
定义一个login函数，admin 1234 输入用户名和密码，验证是否正确

'''


def login():
    user = input('请输入用户名：')
    password = input('请输入密码：')
    if user == 'admin' and password == '1234':
        print('登录成功')
    else:
        print('用户名或者密码错误')


# login()

'''
定义有参数的函数
login 带参数，n表示允许输入错误的次数
2.求1-n的累加和
'''
def login(n):
    if n>0:
        user = input('请输入用户名：')
        password = input('请输入密码：')
        if user == 'admin' and password == '1234':
            print('登录成功')
        else:
            print('用户名或者密码错误')

def sum(n):
    count=0
    for i in range(n+1):
        count+=i
    print(count)
sum(4)