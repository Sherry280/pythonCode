import random

'''
键盘上输入以下内容并打印出来：
默认：admin，1234
用户名：username
密码：password
是否记住密码bool类型，is_remember
如果用户名和密码都正确并且is_remember是True，则表示记住密码，则
打印已经记住用户XX的密码，否则打印，没有记住密码，需要下次继续输入密码
'''
# username=input("用户名")
# password=input("密码")
# is_remember=False
# if username=='admin' and password=='1234':
#     if is_remember:
#         print('已经记住用户%s的密码啦'%username)
#     else:
#         print('没有记住密码需要下次继续输入')
# else:
#     print('用户名或者密码错误')

'''
模拟超市付款：商品单价  商品数量
键盘上输入商品单价，以及商品数量
然后计算应付总额，总额float
提示用户有4种付款方式：
不同的付款方式有不同的折扣：先展示四种付款方式
现金没有折扣
微信0.95折
支付宝 鼓励金付款金额的10%，鼓励金可以直接折算到付款金额中
刷卡 满100减20
'''

print('欢迎光临一四元超市')
price = float(input('商品的单价：'))
number = int(input('商品的数量：'))
# 计算总额
total = price * number
# 选择付款的方式
choice = input('选择的方式有：1.现金 2.微信 3.支付宝 4.刷卡')
# 判断
if choice == '1':
    print('现金没有折扣，应付金额为:%.2f' % total)
elif choice == '2':
    # 微信0.95折
    print('微信支付')
    total *= 0.95
    print('支付金额为：%.2f' % total)
elif choice == '3':
    total = total - total * 0.1
    print('支付宝支付金额为：%.2f' % total)
elif choice == '4':
    print('刷卡支付')
    if total >= 100:
        total -= 20
        print('刷卡支付的金额为：%.2f' % total)
    else:
        print('没有折扣')
else:
    print("输入错误")
