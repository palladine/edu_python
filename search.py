import random
from datetime import datetime
arr = [random.randint(1, 10) for x in range(10)]
el = random.randint(1, 10)
print(arr)


# Linear search
def lsearch(arr, z):
    count = 0
    # for x in arr:
    #     if x == z
    for x in range(len(arr)):
        if arr[x] == z:
            count += 1
    return count

n1 = datetime.now()
print('Количество вхождений (элемент {}): {}'.format(el, lsearch(arr, el)))
print('Линейный поиск: ', (datetime.now()-n1).total_seconds())


# Binary search in sorted array
# upperbound
def bsearch_lower(arr, z):
    left = 0
    right = len(arr)-1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] > z:
            right = middle-1
        elif arr[middle] < z:
            left = middle+1
        else:
            return middle
    return False


# lowerbound
def bsearch_upper(arr, z):
    left = 0
    right = len(arr)-1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] >= z:
            right = middle-1
        elif arr[middle] < z:
            left = middle+1
        else:
            return middle
    return False


# sarr = sorted(arr)
# print('Отсортированный массив: ', sarr)
# n2 = datetime.now()
# print('Поиск индекса левого элемента {} в отсортированном массиве: {}'.format(el, bsearch_lower(sarr, el)))
# print('Поиск индекса правого элемента {} в отсортированном массиве: {}'.format(el, bsearch_upper(sarr, el)))
# print('Бинарный поиск: ', (datetime.now()-n2).total_seconds())


# min and max
def min_max(arr):
    mn = mx = arr[0]
    for x in range(1, len(arr)):
        if arr[x] < mn:
            mn = arr[x]
        if arr[x] > mx:
            mx = arr[x]
    return mn, mx

print(min_max(arr))

