D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = 'CDXCIX'
rs = s[::-1]
symb = rs[0]
res = D[rs[0]]
for x in rs[1:]:
    if D[x] >= D[symb]:
        symb = x
        res = res + D[x]
    else:
        symb = x
        res = res - D[x]
print(res)