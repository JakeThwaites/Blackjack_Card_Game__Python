from Deck import Deck
from Player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.player1 = Player()
        self.player2 = Player()
        self.players.append(self.player1)
        self.players.append(self.player2)

    def start(self):
        self.deck.populate()
        for player in self.players:
            player.get_user_input()

    def takeGo(self, player):
        while (player.is_bust() == False):
            player.get_user_input(self.deck)

