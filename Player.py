class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.totalHandValue = 0
        self.ended_go = False
        self.aces = 0

    def take_card(self, card):
        self.hand.append(card)
        self.totalHandValue += card.value

    def is_bust(self):
        return self.totalHandValue > 21

    def has_won(self):
        return self.totalHandValue == 21

    def take_a_hit(self, deck):
        new_card = deck.deal()
        self.take_card(new_card)


    def get_user_input(self, deck):
        user_go = input("What would you like to do? [S] = Stick, [T] = Take a hit")
        if user_go == "T":
            self.take_a_hit(deck)
        elif user_go == "S":
            self.ended_go = True
        else:
            print("Please choose a valid option.")

    def has_ace(self):
        self.aces += 1



