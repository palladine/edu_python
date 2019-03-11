_dict = {'1': "Меркурий", '2': 'Венера', '3': 'Земля', '4': 'Марс', '5': 'Юпитер', '6': 'Сатурн', '7': 'Уран', '8': 'Нептун', '9': 'Плутон'}
print ("\nСловарь:\n",_dict)

# Сортировка словаря по ключу
print ("\nСортировка по ключу:")
for key in sorted(_dict.keys()):
	print (key, " ", _dict[key])

#Сортировка словаря по значению
print ("\nСортировка по значению (по алфавиту):")
for val in sorted(_dict.values()):
	for kv in _dict.keys():
		if _dict[kv] == val:
			print (kv, " ", val)

print ("\nСортировка по значению (по количеству букв):")
for val in sorted(_dict.values(), key=lambda x: len(x), reverse=True):
	for kv in _dict.keys():
		if _dict[kv] == val:
			print (kv, " ", val)

print ("\nСортировка по значению (по количеству букв, в обратном порядке):")
for val in sorted(_dict.values(), key=lambda x: len(x)):
	for kv in _dict.keys():
		if _dict[kv] == val:
			print (kv, " ", val)
			
# II part expert		
D = {'a': 1, 'g': 4, 'f': 2, 'd': 5, 'b': 3, 'e': 2, 'c': 4}

print(D)
print(sorted(D.keys()))
print(sorted(D.values()))


# сортировка по ключу
print({k: D[k] for k in sorted(D.keys())})
print({k[0]: k[1] for k in sorted(D.items(), key=lambda x: x[0])})
print({k[0]: k[1] for k in sorted(D.items(), key=lambda x: x[0], reverse=True)})

# сортировка по значению
print({k[0]: k[1] for k in sorted(D.items(), key=lambda x: x[1])})
print({k[0]: k[1] for k in sorted(D.items(), key=lambda x: x[1], reverse=True)})

# сортировка по значению, затем по ключу
print({k[0]: k[1] for k in sorted(D.items(), key=lambda x: (x[1], x[0]))})
print({k[0]: k[1] for k in sorted(D.items(), key=lambda x: (x[1], x[0]), reverse=True)})

# сортировка по ключу, затем по значению
print({k[0]: k[1] for k in sorted(D.items(), key=lambda x: (x[0], x[1]))})
print({k[0]: k[1] for k in sorted(D.items(), key=lambda x: (x[0], x[1]), reverse=True)})
