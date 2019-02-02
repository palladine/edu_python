import copy
M = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

M1 = copy.deepcopy(M)
for i1 in range(len(M1)):
    M1[i1][i1] = 1
print(M1)

M2 = copy.deepcopy(M)
for i2 in range(len(M2)):
    M2[i2][abs(i2-len(M2)+1)] = 1

print(M2)
