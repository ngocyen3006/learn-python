import random


class Card:
    '''
    Represents a standard playing card.
    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    '''

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        '''Returns a human-readable string representation.'''
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __eq__(self, other):
        '''Checks whether self and other have the same rank and suit.
        returns: boolean
        '''
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        '''Compares this card to other, first by suit, then rank.
        returns: boolean
        '''
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    '''
    Represents a deck of cards.
    Attributes:
      cards: list of Card objects.
    '''

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there.

        card: Card
        """
        self.cards.remove(card)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    queen_of_diamonds = Card(1, 12)
    card1 = Card(2, 11)
    print(card1)
    res = card1 < queen_of_diamonds
    print(res)
    print("------------------------------")
    deck = Deck()
    print(deck)
    print("------------------------------")
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    hand.sort()
    print(hand)
