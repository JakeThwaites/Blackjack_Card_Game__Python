from Dealer import Dealer
from Deck import Deck
from Player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.player = Player("Jake")
        self.dealer = Dealer("Dealer")
        self.no_winner = Player("Error")
        self.players.append(self.player)
        self.players.append(self.dealer)

    def start(self):
        self.deck.populate()
        self.deck.shuffle()
        self.deal_cards()

        print("You have " + str(self.player.totalHandValue))
        self.take_go(self.player)
        self.dealer.play(self.deck, self.player)

        # winner = self.check_winner()
        print(self.check_winner())

    def deal_cards(self):
        for player in self.players:
            new_card = self.deck.deal()
            new_card2 = self.deck.deal()
            player.take_card(new_card)
            player.take_card(new_card2)

    def take_go(self, player):
        while player.is_bust() == False and player.ended_go is False:
            print( player.name + " currently has " + str(player.totalHandValue) )
            player.get_user_input(self.deck)

    def check_winner(self):
        winner = self.dealer

        if (21 - self.player.totalHandValue) < (21 - winner.totalHandValue) and self.player.is_bust() is False:
            winner = self.player
        elif self.dealer.is_bust() and self.player.is_bust() is False:
            winner = self.player

        if winner == self.player:
            return "Congratulations, you won!"
        else:
            return "Unlucky, the dealer won!"
