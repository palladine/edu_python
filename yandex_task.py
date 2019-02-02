# Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
# Напишите функцию, которая создаёт из этих ключей и значений словарь.
# Если ключу не хватило значения, в словаре должно быть значение None.
# Значения, которым не хватило ключей, нужно игнорировать.
# Подробнее: http://company.yandex.ru/job/vacancies/dev_python_mysql.xml


L1 = [1, 2, 3, 4, 5, 6]
L2 = ["a", "b", "c", "d", "e"]

#function 1
def cr_dic(l1, l2):
    if len(l1) > len(l2):
        for n in range(len(l2), len(l1)):
            L2.append(None)
    return {k: v for k, v in zip(l1, l2) if k is not None}

#functon 2
def cr_dic2(l1, l2):
    return dict(zip(l1, l2)) if (len(l2) <= len(l1)) else dict(map(None, l1, l2))


print("cr_dic:   ", cr_dic(L1, L2))
print("cr_dic2:  ", cr_dic2(L1, L2))
