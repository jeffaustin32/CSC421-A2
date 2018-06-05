'Represents a Community Chest card in Monopoly'
'http://monopoly.wikia.com/wiki/Community_Chest'


class CommunityChest:
    def __init__(self, index):
        self.index = index
        self.description = "COMMUNITY CHEST"
        self.cards = {
            0: self.advanceToGo,
            1: self.bankError,
            2: self.doctorFee,
            3: self.stockSale,
            4: self.outOfJailFree,
            5: self.goToJail,
            6: self.operaNight,
            7: self.holiday,
            8: self.incomeTaxRefund,
            9: self.birthday,
            10: self.lifeInsurance,
            11: self.hospitalFees,
            12: self.schoolFees,
            13: self.consultancyFee,
            14: self.streetRepairs,
            15: self.beautyContest,
            16: self.inheritance
        }

    def play(self, player):
        self.cards[self.index](player)

    def advanceToGo(self, player):
        self.description = "Advance to Go (Collect $200) <Mr. M strides in 7-league boots>"
        player.space = 0
        player.money += 200

    def bankError(self, player):
        self.description = "Bank error in your favor – Collect $200 <Mr. M falls back in astonishment as an arm presents a sheaf of cash out of a bank teller's window>"
        player.money += 200

    def doctorFee(self, player):
        self.description = "Doctor's fees {fee} – Pay $50 <Mr. M angrily brandishes crutches as he stomps with a leg cast>"
        player.money -= 50

    def stockSale(self, player):
        self.description = "From sale of stock you get $50 {$45} <Mr. M, happily entangled in the tape of a stock ticker, waves cash (with no $ sign this time)>"
        player.money += 50

    def outOfJailFree(self, player):
        self.description = "Get Out of Jail Free {Get out of Jail, Free} – This card may be kept until needed or sold <A winged Mr. M flutters out of a bird cage>"
        player.getOutOfJailFree = True

    def goToJail(self, player):
        self.description = "Go to Jail – Go directly to jail – Do not pass Go – Do not collect $200 <A truncheon-wielding policeman in a light-colored uniform lifts a surprised Mr M by the collar>"
        player.goToJail()

    def operaNight(self, player):
        self.description = "Grand Opera Night {Opening} – Collect $50 from every player for opening night seats <A wall sign near steps reads 'Opera Tonite - 8 PM Sharp'; Mr. M leans against it checking his pocket watch in annoyance>"
        player.money += 50

    def holiday(self, player):
        self.description = "Holiday {Xmas} Fund matures - Receive {Collect} $100 <Mr. M carries along a giant Xmas sock containing a sheaf of cash>"
        player.money += 100

    def incomeTaxRefund(self, player):
        self.description = "Income tax refund – Collect $20 <Mr M faints back against a man displaying the Refund paper>"
        player.money += 20

    def birthday(self, player):
        self.description = "It is your birthday - Collect $10 from each player {Not in the deck}"
        return

    def lifeInsurance(self, player):
        self.description = "Life insurance matures – Collect $100 <Below an I N S sign stands a bent Mr M, his long beard brushing the floor>"
        player.money += 100

    def hospitalFees(self, player):
        self.description = "Pay hospital fees of $100 {Pay hospital $100} <A bored nurse holds out her hand for payment while Mr. M holds 2 swaddled infants, one in each arm>"
        player.money -= 100

    def schoolFees(self, player):
        self.description = "Pay school fees {tax} of $150 <A bespectacled schoolboy unhappily receives a head pat and a dime ((Rockefeller style) from Mr. M.>"
        player.money -= 150

    def consultancyFee(self, player):
        self.description = "Receive $25 consultancy fee {Receive for services $25} <As Justice of the Peace, a stern Mr. M holds out his hand for fee from an embarrassed groom whose bride hold a bouquet behind him>"
        player.money += 25

    def streetRepairs(self, player):
        self.description = "You are assessed for street repairs – $40 per house – $115 per hotel <Mr. M., supported by his near-ubiquitous cane in his left hand, holds a pick and shovel over his right shoulder>"
        return

    def beautyContest(self, player):
        self.description = "You have won second prize in a beauty contest – Collect $10 <Mr. M preens with a sash and large bouquet>"
        player.money += 10

    def inheritance(self, player):
        self.description = "You inherit $100 <Mr M. holds his head as unseen people's hands offer brochures titled 'Buy Yacht', 'World Tour', and 'Rolls Royce'>"
        player.money += 100
