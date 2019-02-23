class Base():
    def __init__(self):
        self._age = None

    def getage(self):
        return self._age
    
    def setage(self, val):
        self._age = val

    age = property(getage, setage, None, None)

x = Base()
print(x.age)
x.age = 43
print(x.age)
print(x.name)
