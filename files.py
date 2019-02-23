L = [str(x) for x in range(11)]
# запись элементов списка в файл
f = open('filename.txt', 'w')
for unit in L:
    f.write(unit+'\n')
f.close()

# запись списка строк
g = open('filename2.txt', 'w')
g.writelines(L)
g.close()

# чтение файла
h = open('filename.txt', 'r')
for line in h:
    print(line)
h.close()