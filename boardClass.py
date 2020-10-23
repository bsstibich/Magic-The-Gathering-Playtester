from cardClass import Card
from deckClass import Deck
class Board():
	def __init__(self):
		self.state = []
		self.land = []

	def play(self, hand, position):
		if hand[position].land == False:
			self.state.append(hand[position])
		else:
			self.land.append(hand[position])
		hand.pop(position)
	def checkSpells(self): #Does two loops because 1 loop was causing some spells to not get properly popped
		counter = 0
		for card in self.state:
			if card.instsorc == True:
				self.state.pop(counter)
			counter += 1
		counter = 0
		for card in self.state:
			if card.instsorc == True:
				self.state.pop(counter)
			counter += 1
		counter = 0
#compainon and side board don't work


