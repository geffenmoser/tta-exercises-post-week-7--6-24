import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(suit, value) for suit in self.suits for value in
                      self.values]
        self.shuffle()

    def shuffle(self):
        if len(self.cards) != 52:
            self.cards = [Card(suit, value) for suit in self.suits for value in
                          self.values]
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

deck = Deck()
print(deck.cards)
card = deck.deal()
print(f"Dealt card: {card}")
print(deck.cards)

# A class is a blueprint and grouping for creating objects and defining their
# attributes and functions.

#An instance is an individual object is created from a class.

#Encapsulation is the concept of associating data and methods that operate in
# a class, and allowing for restriction  of access to some of the objects
# features.

#Abstraction is the process of hiding complex implementation details showing
# only the essential features of the object

#Inheritance is a mechansim where one class can derive attributes and
# functions from another.

#Multiple inheritance is inheritance of features from more than one parent
# class.

#Polymorphism allows objects of different classes to be treated as objects of
# a common superclass.

#MRO is the order that python looks for a method in a heirarchy of classes,
# like an order of operations.










