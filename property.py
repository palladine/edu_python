class Base():
    def __init__(self):
        self._age = None

    def getage(self):
        return self._age
    
    def setage(self, val):
        self._age = val
    
    #              getter  setter deleter doc
    age = property(getage, setage, None, None)

x = Base()
print(x.age)   # None
x.age = 43
print(x.age)   # 43


# with decorators
class Base(object):

        def __init__(self):
            self._x = None

        x = property()

        @x.getter
        def x(self):
            """Это свойство x."""
            return self._x

        @x.setter
        def x(self, value):
            self._x = value

        @x.deleter
        def x(self):
            self._x = 'No more'
