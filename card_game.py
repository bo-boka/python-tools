import random


class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __cmp__(self, other):  # arbitrarily deciding suit is more important than rank for the sake of comparison
        # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # suits are the same... check ranks
        if self.rank == 1:  # checking if my card's an Ace
            if other.rank == 1: return 0
            else: return 1
        if other.rank == 1:  # checking if other is an Ace
            if self.rank == 1: return 0
            else: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # ranks are the same... it's a tie
        return 0
        #  In this ordering, Aces appear lower than Deuces (2s)

    def __str__(self):
        return self.ranks[self.rank] + " of " + self.suits[self.suit]


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    # def print_deck(self):     # simple deck print
    #     for card in self.cards:
    #         print card

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + '\n'  # using s as an accumulator to make one giant string
        return s                                         # that indents each iteration by one space

    def shuffle(self):
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def is_empty(self):
        return len(self.cards) == 0

    def deal_one(self):  # but deals from bottom of deck rather than top because of list pop functionality
        return self.cards.pop()

    def deal(self, hands, num_cards=999):  # takes in list of hands and total number of cards to deal
        for i in range(num_cards):
            if self.is_empty(): break
            hand = hands[i % len(hands)]
            hand.add_card(self.deal_one())


class Hand(Deck):   # inherits from Deck
    def __init__(self, name=""):
        self.name = name
        self.cards = []

    def __str__(self):
        s = str(self.name) + "'s hand"
        if self.is_empty():
            return s + ' is empty.\n'
        else:
            return s + ' contains:\n' + Deck.__str__(self)

    def add_card(self, card):
        self.cards.append(card)


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


class OldMaidHand(Hand):    # inherits from Hand which inherits from Deck
    def remove_matches(self):
        count = 0
        cards_copy = self.cards[:]
        for card in cards_copy:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(match)
                self.cards.remove(card)
                print "In %s's hand, the %s matches the %s." % (self.name, card, match)
                count += 1
        return count


class OldMaidGame(CardGame):
    def play(self, names):
        self.hands = []
        self.deck.remove_card(Card(0, 12))  # remove Queen of Clubs
        self.add_players_and_deal(names)
        matches = self.remove_all_matches()
        # self.print_hands()
        # turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            for turn in range(num_hands):  # occasionally tries to pick a card from empty neighbor after game over?
                matches = matches + self.take_turn(turn)
            # turn = (turn + 1) % num_hands
            print matches
        print '=======GAME OVER======='
        # add winner info

    def take_turn(self, player_num):
        p_hand = self.hands[player_num]
        if p_hand.is_empty():
            return 0
        neighbor = self.find_neighbor(player_num)
        picked_card = self.hands[neighbor].deal_one()
        p_hand.add_card(picked_card)
        print p_hand.name, 'chose card from', self.hands[neighbor].name  # add player name
        count = p_hand.remove_matches()
        p_hand.shuffle()
        return count

    def find_neighbor(self, player_num):
        num_players = len(self.hands)
        for next in range(1, num_players):
            neighbor = (player_num + next) % num_players
            if not self.hands[neighbor].is_empty():
                return neighbor

    def add_players_and_deal(self, names):
        for name in names:
            self.hands.append(OldMaidHand(name))
        self.deck.deal(self.hands)
        print '=======Players are here and cards have been dealt.'

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count = count + hand.remove_matches()
        print '=======Matches discarded and play begins.'
        return count

    def print_hands(self):
        for hand in self.hands:
            print hand


game = OldMaidGame()
players_list = ['trudy', 'jim', 'cindy', 'trev']
game.play(players_list)


# deck = Deck()
# h1 = Hand('a')
# h2 = Hand('b')
# h3 = Hand('c')
# the_hands = [h1, h2, h3]
# deck.deal(the_hands, 15)
# print h1
# my_card = Card(2, 2)
# another_card = Card(2, 1)
# print my_card == another_card
# my_card.suits[3] = 'Boof'  # modifying class attribute will modify for class, not just instantiated object
