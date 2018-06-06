import json
import random
from player import Player
from space import Space
from communityChest import CommunityChest
from chance import Chance
from spaceType import SpaceType

'Represents a Monopoly board. 4 corners with 9 spaces between'

class Board:
    def __init__(self):
        self.spaces = []
        self.communityChest = []
        self.chance = []

        # Read spaces data from JSON
        with open('spaces.json') as space:
            spacesData = json.load(space)

        # Generate spaces
        for spaceData in spacesData:
            self.spaces.append(Space(spaceData["id"], spaceData["color"], spaceData["name"], spaceData["cost"], SpaceType[spaceData["type"]]))

        # Generate community chest cards
        for i in range(17):
            self.communityChest.append(CommunityChest(i))
        # Shuffle community chest deck
        random.shuffle(self.communityChest)

        # Generate chance cards
        for i in range(16):
            self.chance.append(Chance(i))
        # Shuffle chance deck
        random.shuffle(self.chance)
        
        # Create the player
        self.player = Player(0, 10, len(self.spaces))

    'Simulates 100 turns'
    def simulate(self):
        # Simulate 100 turns for player
        for i in range(100):
            # Record the player's current space
            space = self.player.space
            # Let the player make their move
            self.player.move()
            space = self.spaces[self.player.space]

            # Perform action depending on space type
            if space.spaceType == SpaceType.GO:
                self.player.money += 200
            elif space.spaceType == SpaceType.CHANCE:
                # Draw and play a chance card
                card = self.chance.pop()
                card.play(self.player)
            elif space.spaceType == SpaceType.COMMUNITY_CHEST:
                # Draw and play a community chest card
                card = self.communityChest.pop()
                card.play(self.player)
            elif space.spaceType == SpaceType.TAX:
                self.player.money -= space.cost
            elif space.spaceType == SpaceType.GO_TO_JAIL:
                self.player.goToJail()
                
            # For stats, increase time spent in the new space (or same if jail)
            space.visited += 1

    def __str__(self):
        output = ""
        for space in self.spaces:
            output += space.name + " | " + str(space.visited) + "\n"
        return output
            
    def __add__(self, other):
        board = Board()
        
        # Sum the visited count for each space of both boards
        for i in range(len(self.spaces)):
            board.spaces[i].visited = self.spaces[i].visited + other.spaces[i].visited
        
        # Sum the roll distribution for both players
        for roll in board.player.rolls:
            board.player.rolls[roll] = self.player.rolls[roll] + other.player.rolls[roll]
        
        return board
