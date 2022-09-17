import random
class Hero:
    def __init__(self, x):
            self.MaxHealth = x[0]
            self.CurrentHealth = x[1]
            self.Attack = x[2]
            self.Defense = x[3]
            self.Status = x[4]
            self.lvl = x[5]
            self.exp = x[6]
            self.PoisonDMG = 0
            self.FreezeTurn = 0
    def exp_add(self,x):
        self.exp += x
        if self.lvl == 3:
            self.exp = 0
            return
        elif self.exp > 30:
            self.exp -= 30
            self.lvl += 1
            return
        else:
            return
    def damage(self,x): #x = attack from enemy
        defense = self.Defense[self.lvl - 1]
        attack = x - defense
        Hero.exp_add(self,defense)
        self.CurrentHealth -= attack
        return attack
    def attack(self):
        BonusDamage = random.randint(-2, 5)
        Attack = int(self.Attack[self.lvl-1]) + BonusDamage
        Hero.exp_add(self, Attack)
        return Attack
    def __str__(self):
        if self.Status == "" or self.Status.isspace():
            self.Status = "None"
        return "Health: " + str(self.CurrentHealth) + "/" + str(self.MaxHealth[self.lvl - 1]) + "\n Status:" + self.Status + "\n Level/EXP: " + str(self.lvl) + "/" + str(self.exp) + "\n"
# HeroType = [{Max Health}, [currecnt Health], (Attack), (Defense), "status", lvl, exo]
Warrior = [(50, 60, 70), 50, (13, 14 ,16), (3, 4, 5), "", 1, 0]
Tanker = [(60, 70, 80), 60, (9, 10, 12), (5, 6, 8), "", 1, 0]
Wizard = [(40, 50, 60), 40, (7, 8, 9), (2, 3, 4), "", 1, 0]
#STATUS = (Poison)
STATUS = (3, 5, 8)
def Heal(x, y): # x = Target, y = HERO
    Healing = [5, 8 ,10]
    y.exp_add(5)
    x.CurrentHealth += Healing[y.lvl - 1]
    if x.CurrentHealth > x.MaxHealth[x.lvl - 1]:
        x.CurrentHealth = x.MaxHealth[x.lvl -1]
        return x, y
    else:
        return x, y
def Poison(x, YourPoisonDMG, y): #x = target
    y.exp_add(5)
    x.PoisonDMG = YourPoisonDMG
    return x
def Cure(x,y): # x = target
    y.exp_add(5)
    x.Status = x.Status.replace("Poison", "").strip()
    x.PoisonDMG = 0
    return x
def Freeze(x, Turn, y): #x = self.Freeze
    y.exp_add(5)
    x.FreezeTurn = Turn + 3
    return x, Turn
def Revive(x):
    x.CurrenHealth = x.MaxHealth
