import unittest
from Deck import Deck
from Player import Player
from Card import Card


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.deck.populate()
        self.player = Player("Jake")
        self.card = Card("Spades", 10)
        self.card2 = Card("Spades", 10)
        self.card3 = Card("Spades", 5)

    def test_has_name(self):
        self.assertEqual("Jake", self.player.name)

    def test_hand_starts_empty(self):
        self.assertEqual(0, len(self.player.hand))

    def test_can_take_card(self):
        self.assertEqual(0, len(self.player.hand))
        new_card = self.deck.deal()
        self.player.take_card(new_card)
        self.assertEqual(1, len(self.player.hand))

    def test_take_card_updates_hand_value(self):
        self.assertEqual(0, self.player.totalHandValue)
        self.player.take_card(self.card)
        self.assertEqual(10, self.player.totalHandValue)

    def test_shows_if_bust(self):
        self.assertEqual(False, self.player.is_bust())
        self.player.take_card(self.card)
        self.player.take_card(self.card2)
        self.player.take_card(self.card3)
        self.assertEqual(True, self.player.is_bust())


if __name__ == '__main__':
    unittest.main()
