class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.totalHandValue = 0

    def take_card(self, card):
        self.hand.append(card)
        self.totalHandValue += card.value

    def is_bust(self):
        if self.totalHandValue > 21:
            return True
        else:
            return False

