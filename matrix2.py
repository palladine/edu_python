import random
razm = 2
L = [[random.randrange(1, 100) for j in range(razm)] for i in range(razm)]
max_sum = L[0][-1]

for i in range(1, razm):
    t1 = 0
    t2 = 0
    for j in range(razm-i):
        t1 += L[i+j][j]
        t2 += L[j][i+j]
    if t1 > max_sum: max_sum = t1
    if t2 > max_sum: max_sum = t2

print(L)
print(max_sum)