from random import *

class guerrier:
    def __init__(self, name, hp, attaque):
        self.name = name
        self.attaque = attaque
        self.hp = hp

    def getHp(self):
        print("Le perso à ",self.hp, " hp")

    def getAtt(self):
        print("Le perso à ", self.attaque, " attaque")

    def setAttaque(self, attaque):
        self.attaque = attaque

    def setHp(self, hp):
        self.hp = hp


class Mage(guerrier):
    def __init__(self, name, hp, attaque, mana):
        super().__init__(name, hp, attaque)
        self.mana = mana


Axel = Mage("Axel", randint(0, 50), 20, 100)
Axel.getHp()
Axel.setHp(randint(100, 5000))
Axel.getHp()

b = 5
d = 3
d, b = b, d
print(b, d)
a = hex(30)
print(a)

#j'ai supprimé le travail au fur et a mesure....

