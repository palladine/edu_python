import random
import msvcrt
from time import sleep

L = [random.randint(1, 10000) for j in range(1000)]

while True:
    if msvcrt.kbhit():
        print('process stop')
        break
    print('Length of queue =', len(L))
    L += [random.randint(1, 10000) for j in range(3)]
    print(23*'-', '3 elements added', 23*'-', sep='\n')
    count = 0
    for x in L:
        if count != 3:
            print('[{}] - {}'.format(L.index(x), x))
            L.pop(L.index(x))
            count += 1
        else:
            print(23*'-', '3 elements deleted', 23*'-', sep='\n')
            sleep(1)
            break
