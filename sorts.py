import time
import random
arr = [random.randint(1, 1000) for x in range(1000)]


# Selection sort
def ss(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# Bubble sort
def bs(arr):
    n = 0
    while n <= len(arr)-2:
        for m in range(len(arr)-1):
            if arr[m] > arr[m+1]:
                arr[m], arr[m+1] = arr[m+1], arr[m]
        n += 1
    return arr


# Quick sort
def qs(arr):
    if len(arr) > 1:
        l = [x for x in arr[1:] if x < arr[0]]
        h = [x for x in arr[1:] if x >= arr[0]]
        return qs(l) + [arr[0]] + qs(h)
    return arr


# Insertion sort
def iis(arr):
    if len(arr) > 1:
        for i in range(1, len(arr)):
            k = i
            for j in range(i-1, -1, -1):
                tmp = arr[k]
                if tmp <= arr[j]:
                    arr.pop(k)
                    arr.insert(j, tmp)
                    k -= 1
    return arr


# Merge sort
def ms(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        lh = arr[:mid]
        rh = arr[mid:]

        ms(lh)
        ms(rh)

        i = j = k = 0
        while i < len(lh) and j < len(rh):
            if lh[i] < rh[j]:
                arr[k] = lh[i]
                i += 1
            else:
                arr[k] = rh[j]
                j += 1
            k += 1

        while i < len(lh):
            arr[k] = lh[i]
            i += 1
            k += 1

        while j < len(rh):
            arr[k] = rh[j]
            j += 1
            k += 1
    return arr


print('\n[Исходный массив]: {} элементов'.format(len(arr)))
print(arr)

n1 = time.perf_counter()
print('\n[Selection sort]: ', ss(arr[:]))
# ss(arr[:])
print('Время (selection sort): {:0.6f}'.format(time.perf_counter()-n1))


n2 = time.perf_counter()
print('\n[Bubble sort]: ', bs(arr[:]))
# bs(arr[:])
print('Время (bubble sort): {:0.6f}'.format(time.perf_counter()-n2))


n3 = time.perf_counter()
print('\n[Quick sort]: ', qs(arr[:]))
# qs(arr[:])
print('Время (quick sort): {:0.6f}'.format(time.perf_counter()-n3))

n4 = time.perf_counter()
print('\n[Insertion sort]: ', iis(arr[:]))
# iss(arr[:])
print('Время (Insertion sort): {:0.6f}'.format(time.perf_counter()-n4))

n5 = time.perf_counter()
print('\n[Merge sort]: ', ms(arr[:]))
# ms(arr[:])
print('Время (Merge sort): {:0.6f}'.format(time.perf_counter()-n5))
