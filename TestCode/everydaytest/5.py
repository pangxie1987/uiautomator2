'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

t = []
for i in range(1,4):
    c = int(input('请输入第%s个数字：'%i))
    t.append(c)
t.sort()
print(t)
