'''
猜拳游戏：3局

'''
import random


n=1
p_count=0
m_count=0
while n<=3:
    #机器产生的数字（0，1，2）
    ran1 = random.randint(0,2)
    #人猜数字
    guess=int(input('请输入:剪刀0，石头1，布2：'))
    #比较判断
    if guess==0 and ran1==2 or guess==1 and ran1==0 or guess==2 and ran1==1:
        print('我赢了')
        p_count+=1
    elif ran1==0 and guess==2 or ran1==0 and guess==1 or ran1==2 and ran1==1:
        print('机器赢了')
        m_count+=1
    else:
        print('平局')
    n+=1
#比较三局两胜的胜负
if p_count>m_count:
    print('最终人获胜')
elif p_count<m_count:
    print('机器获胜')
else:
    print('当前为平局')

