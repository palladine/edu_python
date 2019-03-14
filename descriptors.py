class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep="\n")
        
class Base:
    attr = Descriptor()
    
x = Base()
print(x.attr)



##
class SuperDesc:

    def __get__(self, instance, owner):
        return instance._num

    def __set__(self, instance, val):
        instance._num = val

       
class Base:
    def __init__(self, num):
        self._num = num
    num = SuperDesc()

x = Base(34)
print(x.num)
x.num = 76
print(x.num)
