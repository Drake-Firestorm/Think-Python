import random

class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    def __init__(self):
        self.cards = list()
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, hands=0, cards=0):
        h = list()
        for i in range(hands):
            hand = Hand("Hand_" + str(i))
            self.move_cards(hand, cards)
            h.append(str(hand))
        return h



class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=""):
        self.cards = list()
        self.label = label


def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty


if __name__ == "__main__":
    queen_of_diamonds = Card(1, 12)
    card1 = Card(2, 11)
    # print(card1)

    deck = Deck()
    # print(deck)

    deck.add_card(card1)
    deck.add_card(queen_of_diamonds)
    deck.sort()
    # print(deck)

    hand = Hand("new hand")
    # print(hand.cards)
    # print(hand.label)

    deck = Deck()
    card = deck.pop_card()
    hand.add_card(card)
    # print(hand)

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    hand.sort()
    # print(hand)

    print(deck.deal_hands(2, 4))
