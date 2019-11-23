'''
题目：求1+2!+3!+...+20!的和。
'''

s = 1
t = []
for i in range(1, 21):
    s *= i
    t.append(s)
print(sum(t))