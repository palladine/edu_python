'''
Написать функцию на Python, которая из входной строки генерирует словарь. 
Разделителем данных является символ ":" 
Пример строки: "key1:val1:key2:val2" 
Очень важно, чтобы функция не падала и всегда возвращала результат, 
по которому с точностью до порядка полей (порядок не важен) можно было 
восстановить строку.
'''

str1 = "key1:val1:key2:val2"
str2 = ""
str3 = "key1:val1:key2:"
str4 = "key1:val1:key2"


def make_dict(str_input):
    if str_input and not str_input.endswith(':'):
        str_input += ':' 
    L = str_input.split(':')
    return {k: v for k, v in zip([x for x in L[0::2]], [y for y in L[1::2]])}

if __name__ == '__main__':
    print(make_dict(str1))
    print(make_dict(str2))
    print(make_dict(str3))
    print(make_dict(str4))
