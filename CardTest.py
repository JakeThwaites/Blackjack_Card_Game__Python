import unittest
from Card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card("Spades", "Ten")

    def test_has_suit(self):
        self.assertEqual("Spades", self.card.suit)

    def test_has_symbol(self):
        self.assertEqual("Ten", self.card.symbol)

    def test_can_add_value(self):
        self.card.add_value()
        self.assertEqual(10, self.card.value)


if __name__ == '__main__':
    unittest.main()
