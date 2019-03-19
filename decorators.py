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
## ! Не пременим к методам класса ###
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
