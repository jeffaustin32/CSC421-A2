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

        # Create the players
        self.players = [Player("Player 1"), Player("Player 2"), Player("Player 3")]

        # Read spaces data from JSON
        with open('spaces.json') as space:
            spacesData = json.load(space)

        # Generate spaces
        for spaceData in spacesData:
            self.spaces.append(Space(spaceData["id"], spaceData["color"], spaceData["name"], spaceData["cost"], spaceData["rent"], SpaceType[spaceData["type"]]))

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

    'Simulates 100 turns'
    def simulate(self):
        # Simulate 100 turns for player
        for i in range(100):
            for player in self.players:
                # This player is broke and out of the game
                if player.money < 0:
                    continue

                # Record the player's current space
                space = player.space
                # Let the player make their move
                roll = player.move()
                space = self.spaces[player.space]
                # Visit the space and perform any space type specific actions
                space.visit(player, roll, self.spaces, self.chance, self.communityChest)
                
                # Position may have changed by chance or community chest
                newSpace = self.spaces[player.space]
                if not newSpace == space:
                    # Visit the space and perform any space type specific actions
                    space.visit(player, roll, self.spaces, self.chance, self.communityChest)

                # Player has gone broke and must relinquish all properties
                if player.money < 0:
                    for property in player.properties:
                        property.owner = None

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
        for i, player in enumerate(board.players):
            for roll in player.rolls:
                player.rolls[roll] = self.players[i].rolls[roll] + other.players[i].rolls[roll]
        
        return board
