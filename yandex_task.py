# Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
# Напишите функцию, которая создаёт из этих ключей и значений словарь.
# Если ключу не хватило значения, в словаре должно быть значение None.
# Значения, которым не хватило ключей, нужно игнорировать.
# Подробнее: http://company.yandex.ru/job/vacancies/dev_python_mysql.xml


import itertools

L1 = [1, 2, 3, 4, 5, 6]   # key
L2 = ["a", "b", "c"]   # val

M1 = [1, 2, 3, 4, 5, 6]   # key
M2 = ["a", "b", "c", "d", "e", "f", "g", "h"]   # val


# function 1
def create_dict(list1, list2):
    return dict(itertools.zip_longest(list1, list2)) if len(list1) >= len(list2) else dict(zip(list1, list2))


# function 2 without itertools
def create_dict2(list1, list2):
    tmp_list = list2[:]
    if len(list1) > len(list2):
        tmp_list.extend([None]*(len(list1) - len(list2)))
    return {k: v for k, v in zip(list1, tmp_list)}

print(create_dict(L1, L2))
print(create_dict(M1, M2))

print(create_dict2(L1, L2))
print(create_dict2(M1, M2))
