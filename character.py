import random
import time
class Character:
    def __init__(self, name, lvl, hp, dp, speed):
        self.name = name
        self.lvl = lvl
        self.hp = int((hp) + ((hp/4)*lvl))
        self.dp = int((dp) + ((dp/4)*lvl))
        self.maxhp = self.hp
        self.xp = 0
        self.alive = True
        self.attackSuccess = False
        self.damage = 1
        self.speed = speed
        self.inventory =  {"Inventory" : {"Lint" : 1},
                           "Heals" : {"Medicine" : 1, "Potion" : 0},
                           "Wallet" : {"Gold" : 0}}
        self.starter = False
        self.item = None
        self.commands = ["attack", "heal", "run"]
        self.healtotal = 0

    def showStats(self):
        time.sleep(.5)
        print("Name:", self.name)
        time.sleep(.5)
        print("Level:", self.lvl)
        time.sleep(.5)
        print("HitPoints:", str(self.hp) + "/" + str(self.maxhp))
        time.sleep(.5)
        print("DamagePoints:", self.dp)
        time.sleep(.5)
        print("Speed:", self.speed)

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        time.sleep(.5)
        print()
        print(self.name, "hp", self.hp)
        if self.alive == False:
            time.sleep(.5)
            print()
            print(self.name, "is dead.")
            time.sleep(.5)
            print()

    def levelUp(self):
        if xp == 100:
            lvl += 1

    def damageMultiplyer(self):
        damageMultiplyerRoll = random.randint(1,10)
        if damageMultiplyerRoll <= 4:
            print()
            time.sleep(.5)
            print("Normal Attack")
            time.sleep(.5)
            print()
            self.damage = self.dp
        elif damageMultiplyerRoll <= 7:
            print()
            time.sleep(.5)
            print("Strong attack!")
            time.sleep(.5)
            print()
            self.damage = (self.dp) + (2 * damageMultiplyerRoll)
        elif damageMultiplyerRoll <= 9:
            print()
            time.sleep(.5)
            print("Very Strong attack!")
            time.sleep(.5)
            print()
            self.damage = (self.dp) + (3 * damageMultiplyerRoll)
        elif damageMultiplyerRoll == 10:
            print()
            time.sleep(.5)
            print("CRITICAL HIT!")
            print()
            time.sleep(.5)
            self.damage = (self.dp) + (4 * damageMultiplyerRoll)

    def attackCharacter(self):
        if random.randint(1, 10) >= 3:
            print()
            time.sleep(.5)
            print(self.name, "attacks")
            time.sleep(.5)
            self.damageMultiplyer()
            print(self.name, "deals", self.damage, "damage")
            time.sleep(.5)
            print()
            time.sleep(.5)
            print(self.name + "'s", "hp:", self.hp)
            time.sleep(.5)
            print()
            time.sleep(.5)
            self.attackSuccess = True
        else:
            time.sleep(.5)
            print()
            time.sleep(.5)
            print(self.name + "'s attack missed!")
            time.sleep(.5)
            self.attackSuccess = False

    def characterTurn(self, character1, character2):
        turnOver = False
        while turnOver == False:
            print()
            time.sleep(.5)
            print("What would you like to do?")
            time.sleep(.5)
            decision = input('You can say "ATTACK", "HEAL, or "RUN": ').lower()
            if decision in self.commands:

                if decision == "attack":
                    if character1.alive == True:
                        character1.attackCharacter()
                        if character1.attackSuccess == True:
                            character2.takeDamage(character1.dealDamage())
                        print()
                        time.sleep(.5)
                        print("--------------------------")
                        time.sleep(.5)
                        print()

                if decision == "heal":
                    character1.healCharacter()


                turnOver = True
            else:
                print()
                time.sleep(.5)
                print("What?")


    def enemyTurn(self, character1, character2):
        if character2.alive == True:
            character2.attackCharacter()
            if character2.attackSuccess == True:
                character1.takeDamage(character2.dealDamage())
            print()
            time.sleep(.5)
            print("--------------------------")
            time.sleep(.5)
            print()

    def dealDamage(self):
        return self.damage

    def healCharacter(self):
        medicine = self.inventory["Heals"]["Medicine"]
        potion = self.inventory["Heals"]["Potion"]
        print()
        time.sleep(.5)
        print()
        if medicine > 0 or potion > 0:
            for keys, values in self.inventory["Heals"].items():
                if values > 0:
                    time.sleep(.5)
                    print("You have", str(values) + ":", keys)
                    time.sleep(.5)
            decided = False
            while decided == False:

                print()
                decision = input("Which would you like to use? ").lower()
                if decision == "potion":
                    if potion > 0:
                        potion -= 1
                        if self.hp <= 50 - self.maxhp:
                            self.hp += 50
                            self.healtotal = 50
                        else:
                            self.hp += self.maxhp - self.hp
                            self.healtotal = self.maxhp - self.hp
                        print()
                        time.sleep(.5)
                        print("You regain", self.healtotal, "HP.")
                        time.sleep(.5)
                        print(self.name + "'s HP, now:", str(self.hp) + "/" + str(self.maxhp))
                        decided = True
                    else:
                        time.sleep(.5)
                        print("You have no potions")
                elif decision == "medicine":
                    if medicine > 0:
                        medicine -= 1
                        if self.hp <= 25 - self.maxhp:
                            self.hp += 25
                            self.healtotal = 25
                        else:
                            self.hp += self.maxhp - self.hp
                            self.healtotal = self.maxhp - self.hp
                        print()
                        time.sleep(.5)
                        print("You regain", self.healtotal, "HP.")
                        time.sleep(.5)
                        print(self.name + "'s HP, now:", str(self.hp) + "/" + str(self.maxhp))
                        decided = True
                    else:
                        time.sleep(.5)
                        print("You have no potions")
                else:
                    print()
                    time.sleep(.5)
                    print("What is that?")



    def randomDrop(self, character1, character2):

        dropChance = random.randint(1, 10)
        if dropChance >= 7:
            itemDrop = random.randint(1, 3)
            if itemDrop == 1:
                self.item = "Medicine"
                print()
                time.sleep(.5)
                print(character2.name, "dropped", self.item +".  You put it in your inventory.")
                character1.inventory["Heals"][self.item] += 1
                print(character1.inventory)

            elif itemDrop == 2:
                self.item = "Potion"
                print()
                time.sleep(.5)
                print(character2.name, "dropped", self.item + ".  You put it in your inventory.")
                character1.inventory["Heals"][self.item] += 1
                print(character1.inventory)

            else:
                self.item = "Gold"
                print()
                time.sleep(.5)
                print(character2.name, "dropped", self.item + ".  You put it in your inventory.")
                character1.inventory["Wallet"][self.item] += 1
                print(character1.inventory)
        else:
            time.sleep(.5)
            print()
            print(self.name, "didn't drop anything.")




