from CardValue import CardValue

class Card:
    def __init__(self, suit, symbol):
        self.suit = suit
        self.value = 0
        self.symbol = symbol

    def add_value(self):
        card_value = CardValue()
        for symbol, value in card_value.value_to_symbol.items():
            if self.symbol == symbol:
                self.value = value
