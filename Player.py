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

    def take_a_hit(self, deck):
        new_card = deck.deal()
        self.take_card(new_card)
        print("Your total is " + self.totalHandValue)


    def get_user_input(self, deck):
        input("What would you like to do? [S] = Stick, [T] = Take a hit")
        if input.upper() == "T":
            self.take_a_hit(deck)
        elif input.upper() == "S":
            return
        else:
            print("Please choose a valid option.")

