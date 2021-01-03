import random
a=eval(input('请猜一个数字，并输入：'))
key=random.randint(0,9)
n=1
if a in list(range(0,10)):
    for i in range(0,9):
        while a!=key:
            if a>key:
                n+=1
                print('大了')
                a=eval(input('请猜一个数字，并输入：'))
            elif a<key:
                n+=1
                print('小了')
                a=eval(input('请猜一个数字，并输入：'))
            else:
                a==key
                print('你猜了{}次'.format(n))
            break
    else:
        print('游戏结束')
else:
    print('不按套路出牌，我不玩了')



