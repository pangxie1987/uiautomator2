'''
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
'''
from math import sqrt

h = 0
leap = 1

for m in range (101, 200):
    k = int(sqrt(m+1))
    for i in range(2, k+1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print('%-4d'%m)
        h += 1
    leap = 1
print('total is %s'%h)
