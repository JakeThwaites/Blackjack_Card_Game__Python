import unittest
from Card import Card
from Deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_starts_empty(self):
        self.assertEqual(0, len(self.deck.cards))

    def test_can_populate_cards(self):
        self.deck.populate()
        self.assertEqual(52, len(self.deck.cards))

    def test_can_deal_card(self):
        self.deck.populate()
        self.assertEqual(52, len(self.deck.cards))
        new_card = self.deck.deal()
        self.assertEqual(51, len(self.deck.cards))




if __name__ == '__main__':
    unittest.main()
