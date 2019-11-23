'''
题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：
前两个数之和
'''

# 方法一
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
 
# 输出了第10个斐波那契数列
print (fib(10))


#方法二：递归
def fib2(t):
    if t == 1 or t == 2:
        return 1
    else:
        return fib2(t-1)+fib2(t-2)
print(fib2(10))