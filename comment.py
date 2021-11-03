


msg=input('发表一句话：')
print('-'*50)
print('以下为回复内容：')
while True:
    #输入用户名
    username=input('用户名：')
    #输入回复的内容
    while True:
        comment=input('评论：')
        comment=comment.strip()
        #验证内容
        if len(comment)!=0:
            #验证长度是否超过20个字符
            if len(comment)<=20:
                #是否存在敏感词汇
                comment=comment.replace('靠','**')
                print('\t{}发表的评论是：\n\t{}'.format(username,comment))


            else:
                print('评论内容不能超出20个字符')
        else:
            print('评论内容不能为空！')
        #成功则发表，否则重新输入
    pass