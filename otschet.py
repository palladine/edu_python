import time
_timer = input('Секунд до начала? - ')
_count = 1
for _line in range(int(_timer),0,-1):
	print(" ",_line, end=" \r")
	# print(" *"*_count, end=" \r")
	# _count += 1
	time.sleep(1)
print ('\nПуск!')