# -*- coding: utf-8 -*-
n = '7777'
l = len(n)
summ = 0

# for x in range(1,l+1):
#     print("x ",x)
#     for y in range(x,l):
#         print("y ", y+1)
#         if n[x] == n[y+1]:
#             summ = summ + 1
# print("summ ", summ)

for x in range(0, l-1):
    print("x ", x)
    for y in range(x, l-1):
        print("y ", y+1)
        if n[x] == n[y+1]:
            print("*")
