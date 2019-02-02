import random
 
def scan(_answ, _numer):
    _cnt = 0
    for a in range(len(_answ)):
        for b in range(len(_numer)):
            if (_answ[a] == _numer[b]) and (a == b):
                _cnt += 1
    aa = len(set(_answ).intersection(set(_numer)))
    print("{0} цифр присутствуют в числе, {1} цифр стоят на своих местах".format(aa, _cnt))
 
 
_try = True
while _try == True:
    _count = 6
    _num = random.randint(1000,9999)
    print("Отгадайте четырехзначное число. У вас 6 попыток.")
    for x in range(1,_count+1):
        _answer = input("Введите число: ")
        
        if (x == _count) and (int(_answer) != _num):
            print("Число - {}. Игра окончена. Вы проиграли.\n".format(_num))
            _game = input("Сыграть еще?(y/n): ")
            if _game == 'y':
                _try = True
            elif _game == 'n':
                _try = False
                break
        else:
            if int(_answer) == _num:
                print("Вы выиграли!\n")
                _game = input("Сыграть еще?(y/n): ")
                if _game == 'y':
                    _try = True
                    break
                elif _game == 'n':
                    _try = False
                    break
            elif int(_answer) > _num:
                scan(_answer, str(_num))
                print('Загаданное число меньше')
            else:
                scan(_answer, str(_num))
                print('Загаданное число больше')
        print("Попыток осталось: {}".format(_count-x))