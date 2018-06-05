'Represents a Chance card in Monopoly'
'http://monopoly.wikia.com/wiki/Chance'


class Chance:
    def __init__(self, index):
        self.index = index
        self.description = "CHANCE"
        self.cards = {
            0: self.advanceToGo,
            1: self.advanceToIllinois,
            2: self.advanceToCharles,
            3: self.advanceToUtility,
            4: self.advanceToRailroad,
            5: self.dividend,
            6: self.outOfJailFree,
            7: self.goBackThree,
            8: self.goToJail,
            9: self.makeRepairs,
            10: self.poorTax,
            11: self.goToReadingRailroad,
            12: self.advanceToBoardwalk,
            13: self.electedChairman,
            14: self.loanMatures,
            15: self.crosswordCompetition,
        }

    def play(self, player):
        self.cards[self.index](player)

    def advanceToGo(self, player):
        self.description = "Advance to Go (Collect $200) (Mr. M hops on both feet.)"
        player.money += 200
        player.space = 0
    
    def advanceToIllinois(self, player):
        self.description = "Advance to Illinois Ave. - If you pass Go, collect $200 {Second sentence omitted.} (Mr. M has tied a cloth bundle onto his cane to make a bindle, carried over his right shoulder, and is smoking a cigar)"
        if player.space > 24:
            player.money += 200
        player.space = 24
    
    def advanceToCharles(self, player):
        self.description = "Advance to St. Charles Place – If you pass Go, collect $200 (Mr. M hurries along, hauling a little boy by the hand)"
        if player.space > 11:
            player.money += 200
        player.space = 11
    
    def advanceToUtility(self, player):
        self.description = "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown. (Mr. M trudges along with a huge battleship token on his back)"
        if player.space < 12:
            player.space = 12
        elif player.space < 28:
            player.space = 28
        else:
            player.space = 28
            player.money += 200
    
    def advanceToRailroad(self, player):
        self.description = "Advance token to the nearest Railroad and pay owner twice the rental to which he/she {he} is otherwise entitled. If Railroad is unowned, you may buy it from the Bank. (There are two of these.) (At lower left, Mr. M carries a large flatiron token with two hands; at upper right a railroad crossing is seen)"
        if player.space < 5:
            player.space = 5
        elif player.space < 15:
            player.space = 15
        elif player.space < 25:
            player.space = 25
        elif player.space < 35:
            player.space = 35
        else:
            player.space = 5
            player.money += 200

    def dividend(self, player):
        self.description = "Bank pays you dividend of $50 (With his feet up on a telephone-bearing desk, Mr. M leans back in an overstuffed chair, blowing cigar smoke rings)"
        player.money += 50

    def outOfJailFree(self, player):
        self.description = "Get out of Jail Free – This card may be kept until needed, or traded/sold {This card may be kept until needed or sold - Get Out of Jail Free}{The first sentence is much smaller than the second} (Mr. M, in close-fitting one-piece prison stripes, is literally kicked out)"
        player.getOutOfJailFree = True
    
    def goBackThree(self, player):
        self.description = "Go Back 3 Spaces (Mr. M is hauled back by a cane hooked around his neck) {Presumably an allusion to amateur nights at theaters}"
        player.space -= 3

    def goToJail(self, player):
        self.description = "Go to Jail – Go directly to Jail – Do not pass Go, do not collect $200 (A truncheon-carrying policeman in a dark-colored uniform hauls a surprised Mr M along by the feet)"
        player.goToJail()
    
    def makeRepairs(self, player):
        self.description = "Make general repairs on all your property – For each house pay $25 – For each hotel $100 (Consulting a 'How to Fix It' brochure, a hammer-wielding Mr. M sits astride a house not much larger than he is; it buckles under his weight)"
        return

    def poorTax(self, player):
        self.description = "Pay poor tax of $15 (His trouser pockets pulled out to show them empty, Mr. M spreads his hands) (The video game version replaces this with Speeding fine $15, reportedly also in the UK version.)"
        player.money -= 15

    def goToReadingRailroad(self, player):
        self.description = "Take a trip to Reading Railroad {Take a ride on the Reading} – If you pass Go, collect $200 (Mr. M rides astride the TOOTing engine of a train)"
        player.space = 5
        player.money += 200

    def advanceToBoardwalk(self, player):
        self.description = "Take a walk on the Boardwalk – Advance token to Boardwalk. {Board Walk in both sentences} (Mr. M, a smallish dog hung over one arm, with the other pushes a squalling baby in a small pram; behind them, birds fly in the sky above a low fence)"
        player.space = 39

    def electedChairman(self, player):
        self.description = "You have been elected Chairman of the Board – Pay each player $50 (A newsboy shouts an Extra with Mr. M's headshot on its front page)"
        return
    
    def loanMatures(self, player):
        self.description = "Your building {and} loan matures – Collect $150 {Up until the 1980s a 'building and loan' was a financial institution.} (Mr. M joyfully embraces an apparent wife)"
        player.money += 150
    
    def crosswordCompetition(self, player):
        self.description = "You have won a crossword competition - Collect $100 {Not in the deck}"
        player.money += 100