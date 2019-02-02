print("""---------------------------
    Таблица умножения
---------------------------""", end="")
for x in range(1, 10):
	print("", end="\n")
	for y in range(1,10):
		_unit = str(x*y)
		if len(_unit) == 1:
		 _unit = " "+_unit 
		print(_unit, end=" ")
print("\n---------------------------", end="")
