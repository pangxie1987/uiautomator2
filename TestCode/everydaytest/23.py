'''
题目：打印出如下图案（菱形）:
'''

for i in range(1, 5):
    print(' ' * (4 - i), end="")
    for j in range(1, 2 * i):
        print('*', end="")
    print()
for i in range(3, 0, -1):
    print(' ' * (4 - i), end="")
    for j in range(1, 2 * i):
        print('*', end="")
    print()