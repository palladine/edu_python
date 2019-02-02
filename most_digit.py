arr = [1, 200, 100000]

def find_longest(arr):
    return [x for x in arr if len(str(x))>=max([len(str(i)) for i in arr])][0]

# def find_longest(xs):
#     return max(xs, key=lambda x: len(str(x)))


print(find_longest((arr)))