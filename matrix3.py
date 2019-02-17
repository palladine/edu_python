# Условие
# Дано число n. Создайте массив размером n×n и заполните его по следующему
# правилу. На главной диагонали должны быть записаны числа 0. На двух диагоналях, 
# прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.

# Вариант 1
a = int(input())
L = [['0' for x in range(a)] for y in range(a)]
for i in range(1, a):
    for j in range(a-i):
            L[i+j][j] = str(i)
            L[j][i+j] = str(i)
for g in L:
    print(' '.join(g))

# Вариант 2
n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))
