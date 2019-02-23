import base64
import hashlib
import hmac


stroke = 'bla_bla_bla'
stroke_b = b'bytecode'      # строка в байткоде
print("Строка 'stroke': {0}".format(stroke))

stroke_utf8 = stroke.encode('utf8')       # в utf8
print("Строка 'stroke' в кодировке utf-8: {0}".format(stroke))

key = b'123456'    # ключ должен быть в байткоде
sign = hmac.new(key, stroke_utf8, hashlib.sha1)        # Снимаем hmac-sha1 подпись
print('Type of sign: {0}\tValue: {1}'.format(type(sign), sign))

sign_digest = hmac.new(key, stroke_utf8, hashlib.sha1).digest()                   # + метод digest
print('Type of sign: {0}\t\tValue: {1}'.format(type(sign_digest), sign_digest))

sign_base64 = base64.b64encode(sign_digest)
print("Закодированная строка 'stroke' в base64 кодировку:\t{0}".format(sign_base64))

sign_a85 = base64.a85encode(sign_digest)
print("Закодированная строка 'stroke' в a85 кодировку:\t\t{0}".format(sign_a85))