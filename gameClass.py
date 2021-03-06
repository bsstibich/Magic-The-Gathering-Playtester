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
		for j in self.deck.hand: #checks each card for land status in order to display the lands on their own section of the board
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
				if inp == "": #Ends turn. Draw a card and call checkSpells() to pop all instants and sorceries from the board 
					self.deck.draw(1)
					self.board.checkSpells()
					turn += 1
				else: #if the input isn't empty then its either a number or invalid
					inp = int(inp)
					if inp == 99: #stops program
						running = False
					else:
						self.board.play(self.deck.hand, inp) #plays the card that the user wishes to play
			except IndexError:
				print("Invalid Input")



			

