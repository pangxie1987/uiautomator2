'''
Python 100例
https://www.runoob.com/python/python-100-examples.html
'''

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0
for a in (1,2,3,4):
    for b in (1,2,3,4):
        for c in (1,2,3,4):
            if a!=b and b!=c and a!=c:
                print(a,b,c)
                count += 1
print(count)
