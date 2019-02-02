a = 'find the river'
b = 'e'
first = a.find(b)
second = a.find(b, first+1)
print(second) if second != -1 else print(None)