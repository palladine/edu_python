def non_unique(data):
    L = []
    for x in data:
        if isinstance(x,str):
            L.append(x.upper())
        else:
            L.append(x)
    return [x for x in data if L.count(L[data.index(x)]) > 1]

a = non_unique(['P', 7, 'j', 'A', 'P', 'N', 'Z', 'i',
                'A', 'X', 'j', 'L', 'y', 's', 'K', 'g',
                'p', 'r', 7, 'b'])

print(a)