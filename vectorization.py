import numpy as np
import time
n=100
tic = time.time()
v=np.arange(1,100)
u=np.zeros((n,1))
u1=np.exp(v)
toc = time.time()
#u2=np.log(v)
#u3=np.abs(v)
#u4=np.maximum(v,0)
print(u1)
print("Time" + str((toc - tic)*1000) + 'ms')
#print(u2)
#print(u3)
#print(u4)
"""
import numpy as np
import math
import time

tic = time.time()
v = np.random.rand(100000)#生成100000个0~1之间的数
u = np.zeros((100000,1))
for i in range(100000):
    u[i] = math.exp(v[i])
toc = time.time()
print(u)
print("Time" + str((toc - tic)*1000) + 'ms')

tic = time.time()
w = np.exp(v)
print(w)
toc = time.time()
print("Time" + str((toc - tic)*1000) + 'ms')"""