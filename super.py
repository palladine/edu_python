# Главная задача это возможность использования в классе потомке, методов класса-родителя.
class Base:
    def __init__(self):
        print("__init__ class Base")


class A(Base):
    def __init__(self):
        print("__init__ class A")
        super().__init__()


class B(Base):
    def __init__(self):
        print("__init__ class B")
        Base.__init__(self)


# difference
# method __init__ of class Base will call once
class C(A, B):
    def __init__(self):
        print("__init__ class C")
        super().__init__()


c1 = Base()
c2 = A()
c3 = B()
print('---------')
c4 = C()
