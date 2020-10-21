from cardClass import Card
from deckClass import Deck
from boardClass import Board
from gameClass import Game

deck = Deck()
game = Game(deck)
game.run()
