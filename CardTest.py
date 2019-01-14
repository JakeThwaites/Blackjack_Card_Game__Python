import unittest
from Card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card("Spades", 10)

    def test_has_suit(self):
        self.assertEqual("Spades", self.card.suit)

    def test_has_value(self):
        self.assertEqual(10, self.card.value)


if __name__ == '__main__':
    unittest.main()
