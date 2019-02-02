s1 = "asdfghjkl"
s2 = "afjlyur"

def com_unit(a, b):
    return sorted(list(set(a) & set(b)))

print(com_unit(s1, s2))


