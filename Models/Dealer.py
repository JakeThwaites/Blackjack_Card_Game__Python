from Models.Player import Player


class Dealer(Player):

    def play(self, deck, player):
        print("The dealer has " + str(self.totalHandValue))
        if player.is_bust():
            self.end_go()

        if self.totalHandValue < 17:
            self.take_a_hit(deck)
            print("The dealer takes a hit.")
        else:
            self.end_go

    def end_go(self):
        self.ended_go = True
        print("The dealer sticks.")
