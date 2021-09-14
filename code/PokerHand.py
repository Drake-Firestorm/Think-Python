"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card_Allen import Hand, Deck

from Card_Allen import Card


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = dict()
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def rank_count_hist(self):
        """Builds a histogram of the counts of ranks that appear in the hand.

        Stores the result in attribute count_ranks.
        """
        self.rank_hist()
        self.count_ranks = dict()
        for val in self.ranks.values():
            self.count_ranks[val] = self.count_ranks.get(val, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_count_hist()
        if self.count_ranks.get(2, 0) == 1:
            return True
        return False

    def has_twopair(self):
        """Returns True if the hand has two pairs, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_count_hist()
        if self.count_ranks.get(2, 0) == 2:
            return True
        return False

    def has_three(self):
        """Returns True if the hand has three of a kind, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_count_hist()
        if self.count_ranks.get(3, 0) == 1:
            return True
        return False

    def has_four(self):
        """Returns True if the hand has four of a kind, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_count_hist()
        if self.count_ranks.get(4, 0) == 1:
            return True
        return False

    def has_full(self):
        """Returns True if the hand has full house, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        if self.has_three() and self.has_pair():
            return True
        return False

    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        min_rank = 13
        max_rank = 1
        card_ranks = sorted(self.ranks.keys())
        cards_count = len(card_ranks)
        for i in range(cards_count - 5 + 1):
            ranks = card_ranks[i:i+5]
            for rank in ranks:
                min_rank = min(min_rank, rank)
                max_rank = max(max_rank, rank)
            if max_rank - min_rank == 4:
                return True
        return False

    def has_straightflush(self):
        """Returns True if the hand has a straight flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        cards_count = len(self.cards)
        for i in range(cards_count - 5 + 1):
            ranks = PokerHand()
            for j in range(i, i+5):
                ranks.add_card(self.cards[j])
            if ranks.has_straight() and ranks.has_flush():
                return True
        return False

    def classify(self):
        if self.has_straightflush():
            self.label = "Straight Flush"
        elif self.has_four():
            self.label = "Four of a kind"
        elif self.has_full():
            self.label = "Full House"
        elif self.has_flush():
            self.label = "Flush"
        elif self.has_straight():
            self.label = "Straight"
        elif self.has_three():
            self.label = "Three of a kind"
        elif self.has_twopair():
            self.label = "Two Pair"
        elif self.has_pair():
            self.label = "Pair"
        else:
            self.label = "Highest Card"


def PokerDeck(Deck):

    def deal_hands(self, hands=7, cards=5):
        h = list()
        for i in range(hands):
            hand = PokerHand()
            self.move_cards(hand, cards)
            hand.classify()
            h.append(hand)
        return h


def hand_probablity():
    prob = dict()
    n = 10000
    hands = 10
    cards = 5

    for i in range(n):
        if i % 1000 == 0:
            print(i)

        deck = Deck()
        deck.shuffle()

        for j in range(hands):
            hand = PokerHand()
            deck.move_cards(hand, cards)
            hand.classify()
            classification = hand.label
            prob[classification] = prob.get(classification, 0) + 1

    total = sum(prob.values())
    print("Probability Percent")
    for key in sorted(prob, key=prob.get, reverse=True):
        print("%s: %.3f" % (key, prob.get(key) / total * 100))


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # # deal the cards and classify the hands
    # for i in range(7):
    #     hand = PokerHand()
    #     deck.move_cards(hand, 7)
    #     hand.sort()
    #     print(hand)
    #     print(hand.has_flush())
    #     print('')

    hand_probablity()
