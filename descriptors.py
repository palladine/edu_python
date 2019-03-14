class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep="\n")
        
class Base:
    attr = Descriptor()
    
x = Base()
print(x.attr)
