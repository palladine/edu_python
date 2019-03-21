# I code Caesar 
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


# II
a = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. 
       rfyrq ufyr amknsrcpq ypc dmp. 
       bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
       sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
       lmu ynnjw ml rfc spj.'''


def ciph2(s, num):
    symbs = 'abcdefghijklmnopqrstuvwxyz'
    s2 = ''
    for x in s:
        if x.isalpha():
            if symbs.index(x)+num >= 26:
                s2 += symbs[(symbs.index(x) + num)-26]
            else:
                s2 += symbs[(symbs.index(x) + num)]
        else:
            s2 += x
    return s2

print(ciph2(a, 2))
