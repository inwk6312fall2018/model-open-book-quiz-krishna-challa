import pyCardDeck
from typing import List

class Gamer:

    def __init__(self, name: str):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name


class GamePlace:

    def __init__(self, gamers: List[Gamer]):
        self.deck = pyCardDeck.Deck(
            cards=generate_deck(),
            name='Poker deck',
            reshuffle=False)
        self.gamers = gamers
        self.table_cards = []
        print("Created a table with {} gamers".format(len(self.gamers)))

def Cantrell_Draw(self):
        """
        Basic Five card game structure
        """
        print("Starting a round of Cantrell Draw")
        self.deck.shuffle()
        self.deal_cards(5)
	#Imagine the first round of betting happened here after cards are drawn and visible to gamer
	self.draw1()
	self.fold() #gamers who folded the hands after initial cards were distributed
	self.remove()
	self.after_the_draw()
        # Imagine post-turn, pre-draw1 logic for betting here
	self.reset() #to update the gamers with hands
	self.fold() 
	self.remove()
        self.after_the_draw()
        # Imagine some more betting and winner decision here
	self.cleanup()




def deal_cards(self, number: int):
        """
        Dealer will go through all available gamers and deal them x number of cards.
        :param number:  How many cards to deal
        :type number:   int
        """
        for _ in range(0, number):
            for gamer in self.gamers:
                card = self.deck.draw()
                gamer.hand.append(card)
                print("Dealt {} to gamer {}".format(card, gamer)



def draw1(self,number):
        """
        After the first round of betting, if more than one gamer exist on the hand or table than a draw occurs where gamer selects his/her number of cards which he/she wants to replace
        """
        # Burn a card/cards
	if gamers>1:
		self.number = int(input("how many card/cards you want to replace?"))
        	burned = self.deck.draw()
        	self.deck.discard(burned)
        	print("Burned a card/cards: {}".format(burned))
        	

def fold(self, gamer_id):
        if gamer_id not in self._gamer_ids:
            raise ValueError("Unknown gamer id")
        self._folder_ids.add(gamer_id)

def remove(self, gamer_id):
        self.fold(gamer_id)
        self._dead_gamer_ids.add(gamer_id)



def after_the_draw(self):
        """
        A second "after the draw" betting round occurs beginning with the gamer to the dealer's left or else beginning with the gamer who opened the first round (the latter is common when antes are used instead of blinds). This is followed by a showdown
        """

	if gamers>1:

        	self.5card()
		#check for the highest holding

	else:
		print("only 1 gamer and the winner is declared")


def cleanup(self):
        """
        Cleans up the table to gather all the cards back
        """
        for gamer in self.gamers:
            for card in gamer.hand:
                self.deck.discard(card)
        for card in self.table_cards:
            self.deck.discard(card)
        self.deck.shuffle_back()
        print("Cleanup done")


def generate_deck() -> List[PokerCard]:
    """
    Function that generates the deck, instead of writing down 50 cards, we use iteration
    to generate the cards for use
    :return:    List with all 50 poker playing cards
    :rtype:     List[PokerCard]
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {'A': 'Ace',
             '2': 'Two',
             '3': 'Three',
             '4': 'Four',
             '5': 'Five',
             '6': 'Six',
             '7': 'Seven',
             '8': 'Eight',
             '9': 'Nine',
             '10': 'Ten',
             'J': 'Jack',
             'Q': 'Queen',
             'K': 'King'}
    cards = []
    for suit in suits:
        for rank, name in ranks.items():
            cards.append(PokerCard(suit, rank, name))
    print('Generated deck of cards for the table')
    return cards

if __name__ == '__main__':
    table = GamePlace([Gamer("Jack"), Gamer("John"), Gamer("Peter")])
    table.Cantrell_Draw()
