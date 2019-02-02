class Warrior:
    health = 50
    attack = 5
    is_alive = True

class Knight(Warrior):
    attack = 7

a = Warrior()
b = Warrior()

def fight(a,b):
    while True:
        b.health -= a.attack
        if b.health < 0:
            b.is_alive = False
            return True
        a.health -= b.attack
        if a.health < 0:
            a.is_alive = False
            return False

print(fight(a,b))