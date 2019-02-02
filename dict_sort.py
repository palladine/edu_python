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