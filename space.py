import random
from spaceType import SpaceType

'Represents a space on a Monopoly game'
'https://en.wikipedia.org/wiki/Template:Monopoly_board_layout'
class Space:

    def __init__(self, id, color, name, cost, rent, spaceType):
        self.id = id
        self.color = color
        self.name = name
        self.cost = cost
        self.rent = rent
        self.visited = 0
        self.spaceType = spaceType
        self.owner = None

    'This space was landed on'
    def visit(self, player, roll, spaces, chance, communityChest):
        # Player did not move (in jail)
        if roll == 0:
            return

        self.visited += 1
        
         # Perform action depending on space type
        if self.spaceType == SpaceType.GO:
            player.money += 200
            return
        elif self.spaceType == SpaceType.CHANCE:
            # No more chance cards
            if len(chance) == 0:
                return
                
            # Draw and play a chance card
            card = chance.pop()
            card.play(player)
            return
        elif self.spaceType == SpaceType.COMMUNITY_CHEST:
            # No more community chest cards
            if len(communityChest) == 0:
                return

            # Draw and play a community chest card
            card = communityChest.pop()
            card.play(player)
            return
        elif self.spaceType == SpaceType.TAX:
            player.money -= self.cost
            return
        elif self.spaceType == SpaceType.GO_TO_JAIL:
            player.goToJail()
            return
        
        # Pay rent or attempt to buy property
        self.payRent(roll, player)        

    def payRent(self, roll, player):
        # If space is not owned, let player try to buy
        if not self.owner:
            self.buy(player)
            return

        # Space is owned, pay rent to owner
        if self.spaceType == SpaceType.RAILROAD:
            # Determine how many railroads are owned
            railroadsOwned = 0
            for property in self.owner.properties:
                if property.spaceType == SpaceType.RAILROAD:
                    railroadsOwned += 1

            # They must own one utility
            rentDue = 25
            # If more are owned, increase rent
            if railroadsOwned == 2:
                rentDue = 50
            elif railroadsOwned == 3:
                rentDue = 100
            elif railroadsOwned == 4:
                rentDue = 200

            player.money -= rentDue
            self.owner.money += rentDue
            
        elif self.spaceType == SpaceType.UTILITY:
            # Determine how many utilities are owned
            utilitiesOwned = 0
            for property in self.owner.properties:
                if property.spaceType == SpaceType.UTILITY:
                    utilitiesOwned += 1
            
            # They must own one utility
            rentDue = 4 * roll
            # If they own both, increase rent
            if utilitiesOwned == 2:
                rentDue = 10 * roll

            player.money -= rentDue
            self.owner.money += rentDue
        else:            
            player.money -= self.rent
            self.owner.money += self.rent

    'Give the player an opportunity to buy the property'
    def buy(self, player):
        # Check that player has enough money to buy the property
        if player.money < self.cost:
            return

        # 50% chance to buy the property
        if random.random() > 0.5:
            player.money -= self.cost
            self.owner = player
            player.properties.append(self)