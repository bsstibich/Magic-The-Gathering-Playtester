from cardClass import Card
from deckClass import Deck
from boardClass import Board
from os import system, name
class Game:
	def __init__(self, deck):
		self.deck = deck
		self.board = Board()

	def clear(self): 						 
	    if name == 'nt': # for windows
	        _ = system('cls')  
	    else: # for mac and linux
	        _ = system('clear') 
  
	def displayMenu(self, turn):
		counter = 0
		print("Turn {}".format(turn))
		print("========================================")
		print("Current Board:\n")
		for i in self.board.state:
			print(i.name)
		print("========================================")
		print("Land:\n")
		for z in self.board.land:
			print(z.name)
		print("========================================")
		print("Current Hand:\n")
		for j in self.deck.hand:
			name = j.name
			if j.land == True:
				name = name + " (L)" 
			print("{}) {}".format(counter, name))
			counter += 1
		print("========================================")
		
	def run(self):
		running = True
		turn = 1
		self.deck.makelist()
		self.deck.shuffle()
		self.deck.draw(7)
		board = Board()
		inp = 0
		while running:
			self.clear()
			self.displayMenu(turn)
			print("Enter the card number you wish to play\nHit Enter to end turn\nEnter 99 to end game")
			try:
				inp = input("Enter Your Choice: ")
				if inp == str(0):
					self.board.play(self.deck.hand, 0)
				elif inp == str(1):
					self.board.play(self.deck.hand, 1)
				elif inp == str(2):
					self.board.play(self.deck.hand, 2)
				elif inp == str(3):
					self.board.play(self.deck.hand, 3)
				elif inp == str(4):
					self.board.play(self.deck.hand, 4)
				elif inp == str(5):
					self.board.play(self.deck.hand, 5)
				elif inp == str(6):
					self.board.play(self.deck.hand, 6)
				elif inp == str(7):
					self.board.play(self.deck.hand, 7)
				elif inp == str(8):
					self.board.play(self.deck.hand, 8)
				elif inp == "":
					self.deck.draw(1)
					self.board.checkSpells()
					turn += 1
				elif inp == str(99):
					running = False
			except IndexError:
				print("Invalid Input")



			

