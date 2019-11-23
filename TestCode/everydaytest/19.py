'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。

程序分析：请参照程序Python 练习实例14。
'''

for i in range(1, 1001):
    sum = 0
    for j in range(1, i):
        if i%j == 0:
            sum += j
    if sum == i:
        print(i)
