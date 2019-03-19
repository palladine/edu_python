''' @decorator
    def base(arg):
     ...

    base(100)

      эквивалентно

    def base(arg):
     ...

    base = decorator(base)
    base(100)
'''


''' @decorator
    class Base:
     ...
    x = Base(100)

      эквивалентно

    class Base:
     ...
    Base = decorator(Base)
    x = Base(100)
'''


# function - decorator
def func_decorator(func):
    def in_func(*args):
        print(func.__name__)
        for x in args:
            print(x)
        func(*args)
    return in_func


# I
def sfunc(*args):
    print(sum(args))

sfunc(2, 3, 4)

sfunc = func_decorator(sfunc)
sfunc(2, 3, 4)


# II
@func_decorator
def nfunc(*args):
    print(sum(args))

nfunc(3, 4, 5)



#####  С атрибутами экземпляра класса ######
## ! Не применим к методам класса ###
class base():
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):    # Вызов при обращении
        self.calls += 1
        print('calls - {}, function - {}'.format(self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

@base
def func(a, b, c):    # func = base(func)
    print(a + b + c)

@base
def func2(a, b):      # func2 = base(func2)
    print(a * b)

func(3, 4, 5)    # base.__call__
func(4, 5, 6)

func2(3, 3)
func2(5, 5)
#############################################

##### Декоратор и к функциям и к методам классов ############
### С помощью вложенной функции ####
def base(func):
    calls = 0
    def callfunc(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('calls - {}, function/method - {}'.format(calls, func.__name__))
        return func(*args, **kwargs)
    return callfunc

# к функциям
@base
def func(a, b, c):
    print(a + b + c)

@base
def func2(a, b):
    print(a * b)

# к методам
class Person:
    def __init__(self, name):
        self.name = name

    @base
    def getname(self):
        return self.name

    @base
    def getmulname(self, num):
        return self.name * num

# вывод
func(3, 4, 5)
func(5, 6, 7)
func2(7, 8)
func2(8, 9)

jack = Person('Jack')
print(jack.getname())
print(jack.getname())
print(jack.getmulname(3))
print(jack.getmulname(4))
########################################################
