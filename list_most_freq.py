# most frequent element in a list
a = [1,2,3,1,2,3,4,5,3,2,3,2,2,2,1,2,3,2]
print(max(set(a), key = a.count))

