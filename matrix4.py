# Условие
# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.

# Вариант 1
a = int(input())
L = [['0' for x in range(a)] for y in range(a)]
for i in range(a):
    for j in range(a-1, -1, -1):
        if i+j == a-1:
            L[i][j] = '1'
        if i+j > a-1:
            L[i][j] = '2'
for g in L:
    print(' '.join(g))

