import time


class Encounter:
    def __init__(self, character1, character2):

        self.start = ""
        self.command = ""
        self.commands = ["battle", "heal", "run"]
        self.decided = False
        self.character1 = character1
        self.character2 = character2

    def playerAction(self):

        print(self.character1.name, "you have encountered", self.character2.name)
        print()
        time.sleep(.5)
        self.character2.showStats()
        print()
        time.sleep(.5)

        while self.decided == False:
            print("What would you like to do?")
            time.sleep(.5)
            decision = input('''You can say: "BATTLE", "HEAL", or "RUN": ''').lower()
            self.command = decision
            if self.command in self.commands:
                print()
                time.sleep(.5)
                print("Ok")
                time.sleep(.5)
                self.decided = True
            else:
                print()
                time.sleep(.5)
                print("No! Try again!")

        if self.decided == True and self.command == "battle":
            while self.character1.alive == True and self.character2.alive == True:
                if self.character1.speed >= self.character2.speed:
                    self.character1.characterTurn(self.character1, self.character2)
                    self.character2.enemyTurn(self.character1, self.character2)
                else:
                    self.character2.enemyTurn(self.character1, self.character2)
                    self.character1.characterTurn(self.character1, self.character2)
            self.decided = False
            if self.character2.alive == False:
                self.character2.randomDrop(self. character1, self.character2)

        if self.decided == True and self.command == "heal":
            self.healPhase()




    def healPhase(self):
        self.decided = False
        if self.character1.inventory["Medicine"] > 0:
            print()
            time.sleep(.5)
            print("You use your medicine")
            self.character1.inventory["Medicine"] -= 1
            self.character1.healCharacter("medicine")
