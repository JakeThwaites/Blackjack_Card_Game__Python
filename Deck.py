from Suit import Suit
from CardValue import CardValue
from Card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []

    def populate(self):
        all_suits = Suit()
        all_values = CardValue()
        all_cards = []

        for value in all_values.symbols:
            for suit in all_suits.suits:
                new_card = Card(suit, value)
                all_cards.append(new_card)

        self.cards = all_cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)
