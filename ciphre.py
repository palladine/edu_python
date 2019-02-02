def ciph(s, num):
    symbs = 'abcdefghijklmnopqrstuvwxyz'
    s2 = ''
    for x in s:
        if x != ' ':
            if symbs.index(x)+num > 26:
                s2 += symbs[(symbs.index(x) + num)-26]
            else:
                s2 += symbs[(symbs.index(x) + num)]
        else:
            s2 += ' '
    return s2


print(ciph('a b c', -3))

