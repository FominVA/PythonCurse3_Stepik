
class CardDeck:
    def __init__(self):
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
        self.suits = ["пик", "треф", "бубен", "червей"]
        self.counter = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter += 1
        return f'{self.cards[self.counter]} {self.suits[self.counter]}'


cards = CardDeck()

print(next(cards))
print(next(cards))