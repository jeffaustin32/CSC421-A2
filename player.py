import random

'Represent a player in Monopoly'

class Player:
    def __init__(self, space, jail, spacesCount):
        self.money = 0
        self.space = space
        self.jail = jail
        self.jailed = False
        self.jailedFor = 0
        self.spacesCount = spacesCount
        self.getOutOfJailFree = False
        self.rolls = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    'Simulate the players turn'
    def move(self):
        # Roll the die
        self.space += self.roll()
        # Wrap player around if they have gone around the board
        self.space = self.space % self.spacesCount

    'Player is going to jail'
    def goToJail(self):
        self.space = self.jail

        if self.getOutOfJailFree:
            self.getOutOfJailFree = False
        else:
            self.jailed = True
            self.jailedFor = 3

    'Simulate a dice roll'
    def roll(self, doublesRolled=0):
        # Check if doubles were rolled 3 times, if so player if jailed
        if doublesRolled == 3:
            self.goToJail()
            return 0

        # Generate two random rolls
        rollOne = int(round(random.random() * 5)) + 1
        rollTwo = int(round(random.random() * 5)) + 1

        # Check if player is in jail and didn't roll doubles
        if self.jailed:
            if not rollOne == rollTwo:
                self.jailedFor -= 1

                # Check if player has served their entire jail sentence
                if self.jailedFor == 0:
                    self.jailed = False
                return 0
            else:
                self.jailed = False
                return rollOne + rollTwo

        # Sum for roll
        totalRoll = rollOne + rollTwo

        # For stats, increment roll count
        self.rolls[totalRoll] += 1

        # Check if doubles were rolled, if so roll again and increment doublesRolled
        if rollOne == rollTwo:
            newRoll = self.roll(doublesRolled + 1)

            # Check if enough doubles were rolled to go to jail
            if self.jailed:
                return 0

            # Add the extra roll to the previous total
            totalRoll += newRoll

        return totalRoll
