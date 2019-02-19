import unittest

from Models.Deck import Deck
from Models.Game import Game
from Models.Player import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.player = Player("Jake")
        self.deck = Deck()
        self.deck.populate()



if __name__ == '__main__':
    unittest.main()
