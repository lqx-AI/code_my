import random
import math
import time
Dot=10000000
hits=0.0
ahits=0.0
time.process_time()
for i in range(1,Dot+1):
    x,y=random.random(),random.random()
    dist=math.sqrt(pow(x,2)+pow(y,2))
    if dist<1:
        hits+=1
    elif dist==1:
        ahits+=1
    p=(hits/(Dot-ahits))*4
print('结果是{:10f}'.format(p))
print('运行时间{:2f}'.format(time.process_time()))


