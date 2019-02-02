# Рекурсивный подсчет суммы элементов списка (последовательности)

def sum_rec(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sum_rec(lst[1:])

print(sum_rec([1, 2, 3]))
