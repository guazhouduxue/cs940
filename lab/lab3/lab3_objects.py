import numpy as np

class Card():
    def __init__(self, suit, value):
        if suit in ["Hearts", "Clubs", "Spades", "Diamonds"]:
            self.suit = suit
        else:
            raise ValueError(f"{suit} is not a valid suit.")
        
        if value in range(1, 14):
            self.value = value
        else:
            raise ValueError(f"{value} is not a valid value.")
        
    def print_card(self):
        if self.value > 1 and self.value <=10:
            print(f"This is the {self.value} of {self.suit}")
        elif self.value == 1:
            print(f"This is the Ace of {self.suit}")
        elif self.value == 11:
            print(f"This is the Jack of {self.suit}")
        elif self.value == 12:
            print(f"This is the Queen of {self.suit}")
        elif self.value == 13:
            print(f"This is the King of {self.suit}")


    def __str__(self):
        if self.value > 1 and self.value <=10:
            return f"{self.value} of {self.suit}"
        elif self.value == 1:
            return f"Ace of {self.suit}"
        elif self.value == 11:
            return f"Jack of {self.suit}"
        elif self.value == 12:
            return f"Queen of {self.suit}"
        elif self.value == 13:
            return f"King of {self.suit}"
         
    
    def __repr__(self):
         return f'CARD("{self.suit}", {self.value})'

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __dict__(self):
        return {
            "suit": self.suit,
            "value": self.value
        }

        
class Deck:
    def __init__(self):
        self.cards = []

        for s in ["Hearts", "Clubs", "Spades", "Diamonds"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def shuffle(self):
        np.random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def restartGame(self):
        self.cards = []
        for s in ["Hearts", "Clubs", "Spades", "Diamonds"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
        
        np.random.shuffle(self.cards)

class Hand:
    def __init__(self, cards=None):
        if cards is not None:
            self.cards = cards
        else:
            self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def play_card(self, index):
        return self.cards.pop(index)

    def hand_total(self):
        total = 0
        numberOfCards = len(self.cards)
        for card in self.cards:
            total += card.value
        return {"numberOfCards": numberOfCards, "totalValue": total}
    
    def __dict__(self):
        return {
            "cards" : [card.__dict__() for card in self.cards]
        }
