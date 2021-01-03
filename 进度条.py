import time
scale=20
print('---开始执行---')
t=time.clock()
for i in range(scale+1):
    a,b='**'*i,'..'*(scale-i)
    c=(i/scale)*100
    t-= time.clock()
    print('\r{:^3.0f}%[{}->{}]'.format(c,a,b),end='')
    time.sleep(0.1)
print('---程序结束---')
