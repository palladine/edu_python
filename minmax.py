import random

L = [random.randint(0, 100) for x in range(10)]
print(L)

def minmax(l):
    min = max = l[0]
    for x in l[1:]:
        if x < min:
            min = x
        if x > max:
            max = x
    return min, max

print(minmax(L))
