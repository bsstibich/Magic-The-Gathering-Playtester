from cardClass import Card
from deckClass import Deck
from boardClass import Board

class Game:
	def __init__(self, deck):
		self.deck = deck
		self.board = Board()
	def displayMenu(self):
		counter = 0
		print("========================================")
		print("Current Board:")
		for i in board.state:
			print(i)
		print("========================================")
		print("========================================")
		print("Current Hand:")
		for j in self.deck.hand:
			print("{}) + j.name".format(counter))
			counter += 1
		print("========================================")
	def run(self):
		running = True
		self.deck.makelist()
		self.deck.shuffle()
		self.deck.draw(7)
		board = Board()
		inp = 0
		while running:
			displayMenu()
			print("Enter the card number you wish to play\nEnter 99 to end turn\nEnter 69 to end game")
			inp = input("Enter Your Choice: ")
			if inp == 0:
				play(self.deck.hand, 0)
			elif inp == 1:
				play(self.deck.hand, 1)
			running = False
			

