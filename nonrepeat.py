# non_repeat('aaaaa') == 'a'
# non_repeat('abdjwawk') == 'abdjw'
# non_repeat('abcabcffab') == 'abcf'
# non_repeat('w') == 'w'
# non_repeat('fghfrtyfgh') == 'ghfrty'


def non_repeat(s):
    tmp = res = s[0] if s else ''
    for i in range(len(s)):
        tmp = s[i]
        for j in range(i+1, len(s)):
            tmp = s[j] if s[j] in tmp else tmp+s[j]
            if len(tmp) > len(res):
                res = tmp   
    return res   


print(non_repeat('aaaaa'))
print(non_repeat('abdjwawk'))
print(non_repeat('abcabcffab'))
print(non_repeat('w'))
print(non_repeat('fghfrtyfgh'))
print(non_repeat(''))

