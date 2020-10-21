import random
from cardClass import Card
import xml.etree.ElementTree as ET

class Deck:
	def __init__(self):
		self.list = []
		self.hand = []

	def printCurrentList(self): #May remove
		limitCounter = 0

		print("\nCurrent top 10 cards:\n")
		for card in self.list:
			if limitCounter != 10:
				print(card.name)
				limitCounter += 1

	def draw(self, drawAmount):
		for i in range(drawAmount):
			self.hand.append(self.list[0])
			self.list.pop(0)

	#def play(self, card): #make board object to move card to


	def shuffle(self):
		random.shuffle(self.list)
		random.shuffle(self.list) #Do it twice for twice the shuffling :^)
		
		
	def makelist(self): #takes MTGA exported decklist from decklist.txt and formats it into a functional decklist
		deckCompact = []
		deck = []
		temp = []
		counter = 0
		cardname = ""
		cardquant = 0
		tree = ET.parse('cards.xml')
		root = tree.find('cards')
		deckTxt = open('decklist.txt', 'r')
		deckRaw = deckTxt.readlines() 

		for line in deckRaw:
			deckRaw[counter] = line[:line.rfind("(")]
			counter += 1
		counter2 = 0
		
		for line in deckRaw:
			temp = line.split()
			if len(temp[0]) > 0 and len(temp[0]) < 3:
				for theo in temp:
					if len(temp[0]) > 0 and len(temp[0]) < 3:
						cardquant = int(theo)
						temp[counter2] = ''
						for betty in temp:
							cardname += (betty + " ") 
						cardname = cardname[1:-1] #cuts out extra spaces at begining and end
						deckCompact.append(Card(cardname, cardquant, False, False))
						cardname = ""
						cardquant = 0
				counter += 1


		for card in deckCompact: 
			for cardFull in root.iter('card'): #checks land type
				for cardFull2 in cardFull.iter('name'):
					for cardFull3 in cardFull.iter('maintype'):
						if cardFull3.text == "Land" and cardFull2.text == card.name:
							card.land = True
						elif (cardFull3.text == "Instant")  and (cardFull2.text == card.name):
							card.instsorc = True
						elif (cardFull3.text == "Sorcery")  and (cardFull2.text == card.name):
							card.instsorc = True  
							 

			for quant in range(card.quantity):
				deck.append(Card(card.name, card.quantity, card.land, card.instsorc))
				#print(card.name + "   " + str(card.instsorc))
	
		print("Deck List Loaded...")
		self.list = deck
		