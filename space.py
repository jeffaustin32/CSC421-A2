from spaceType import SpaceType

'Represents a space on a Monopoly game'
'https://en.wikipedia.org/wiki/Template:Monopoly_board_layout'


class Space:

    def __init__(self, id, color, name, cost, spaceType):
        self.id = id
        self.color = color
        self.name = name
        self.cost = cost
        self.visited = 0
        self.spaceType = spaceType

    'This space was landed on'

    def visit(self):
        self.visited += 1
        # TODO: Perform special action based on space type

    'Draw this space on the board'

    def draw(self):
        # TODO: Draw the space
        # Note: Dimensions depend on position
        return
