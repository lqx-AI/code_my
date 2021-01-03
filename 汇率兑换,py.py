i=1
while i==1:
    a=input('请输入带单位的数字（美元或元）:')
    if a[-1]!=a[0]:
        if a[-2] in ['美']:
            if a[-1] in ['元']: 
                y=eval(a[0:-2])*6
                print('{:.2f}元'.format(y))
    elif a[-2] not in ['美']:
        if a[-1] in ['元']: 
            z=(eval(a[0:-1]))/6
            print('{:.2f}美元'.format(z))
    else:
        print('输入错误，请重新输入')

