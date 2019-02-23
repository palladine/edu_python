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
