'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
'''

n = int(input('请输入计算的个数：'))

def total(n):
    count = 0
    a = 0
    t = 0
    for i in range(n+1):
        a = n*(10**i)
        
        t = t+a
        #print('a=%s'%a)
        print('t=%s'%t)
        count += t
    print('总和=%s'%count)

total(n)