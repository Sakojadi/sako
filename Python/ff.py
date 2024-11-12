from time import time
from random import randint
from collections import defaultdict
a = [[randint(10,100) for i in range(1000)] for i in range(10000)]

# start = time()
# resr = []
# for i in a:
#     sumr = 0
#     for u in i:
#         sumr+=u
#     resr.append(sumr)
# end = time()
# print(end-start)

# star = time()
# resc = defaultdict(int)
# for i,x in enumerate(a):
#     sumc = 0
#     for o,u in enumerate(x):
#         resc[o]+=u
# en = time()
# print(en - star)

start = time()
resr = [0]*len(a)
for x, i in enumerate(a):
    k= 0
    b = 0
    for u,o in enumerate(i):
        if k>len(i)-1:
            b+=1
            k = b
        resr[x]+=a[x][k]
        k = k+10
end = time()
print(end-start)
