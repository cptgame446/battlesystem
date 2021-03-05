from character import Character
from encounter import Encounter
import random
import time
player = Character("Jason", 1, 100, 10, 3)
easyEnemy = Character("Elton", 1, 25, 3, 1)
normalEnemy = Character("Norm", 1, 75, 6, 3)
hardEnemy = Character("Harold", 1, 105, 9, 5)
enemy = normalEnemy

def enemyRoll():
    global enemy
    enemyroll = random.randint(1, 3)
    if enemyroll == 1:
        enemy = easyEnemy
        return enemy
    elif enemyroll == 2:
        enemy = normalEnemy
        return enemy
    else:
        enemy = hardEnemy
        return enemy

def attackPhase():

    while player.alive == True and enemy.alive == True:
        if player.speed >= enemy.speed:

            decision = input("What would you like to do?: ").lower()
            if decision == "attack":
                if player.alive == True:
                    player.attackCharacter()
                    if player.attackSuccess == True:
                        enemy.takeDamage(player.dealDamage())
                    print()
                    time.sleep(.5)
                    print("--------------------------")
                    time.sleep(.5)
                    print()
            if enemy.alive == True:
                enemy.attackCharacter()
                if enemy.attackSuccess == True:
                    player.takeDamage(enemy.dealDamage())
                print()
                time.sleep(.5)
                print("--------------------------")
                time.sleep(.5)
                print()
        else:
            if enemy.alive == True:
                enemy.attackCharacter()
                if enemy.attackSuccess == True:
                    player.takeDamage(enemy.dealDamage())
                print()
                time.sleep(.5)
                print("--------------------------")
                time.sleep(.5)
                print()
            decision = input("What would you like to do?: ").lower()
            if decision == "attack":
                if player.alive == True:
                    player.attackCharacter()
                    if player.attackSuccess == True:
                        enemy.takeDamage(player.dealDamage())
                    print()
                    time.sleep(.5)
                    print("--------------------------")
                    time.sleep(.5)
                    print()



print()
time.sleep(.5)
player.name = input("Enter your name: ").capitalize()


print()
time.sleep(.5)
player.showStats()
enemyRoll()
print()
time.sleep(.5)

while player.alive == True and enemy.alive == True:
    encounter = Encounter(player, enemy)
    encounter.playerAction()

print()
time.sleep(.5)
print("Battle Over")
print(player.inventory)
player.showStats()





