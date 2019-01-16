from Deck import Deck
from Player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.player1 = Player("Jake")
        self.player2 = Player("Bob")
        self.no_winner = Player("Error")
        self.players.append(self.player1)
        self.players.append(self.player2)

    def start(self):
        self.deck.populate()
        self.deck.shuffle()
        self.deck.deal()
        self.deal_cards()

        for player in self.players:
            self.take_go(player)

        winner = self.check_winner()
        print("Congratulations, " + winner.name + " won!")

    def deal_cards(self):
        for player in self.players:
            new_card = self.deck.deal()
            new_card2 = self.deck.deal()
            player.take_card(new_card)
            player.take_card(new_card2)


    def take_go(self, player):
        while (player.is_bust() == False and player.ended_go == False):
            print( player.name + " currently has " + str(player.totalHandValue) )
            player.get_user_input(self.deck)

    def check_winner(self):
        winner = self.no_winner

        for player in self.players:
            if (21 - player.totalHandValue) < (21 - winner.totalHandValue):
                winner = player

        return winner
