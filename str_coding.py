# -*- coding: utf-8 -*-
import sys
print(sys.getdefaultencoding())

# 1 and 2-bytes symbols
for i in range(2047):
    print(i, 'Символ: '+chr(i), '\tByte:', (chr(i)).encode('utf-8'), '\tBin: '+bin(i), '\tHex: '+hex(i), sep='  ')


somestring = 'Строка String'
strtobytes = somestring.encode('utf-8')   # тоже самое strtobytes = bytes(somestring, 'utf-8')
bytestostr = strtobytes.decode()

print(strtobytes, list(strtobytes), bytestostr, sep=' ')

print(somestring.encode('cp866'))
print(somestring.encode('cp1251'))
print(somestring.encode('koi8-r'))
