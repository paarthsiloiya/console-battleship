from utils import *
from ship import Ship

class Tile:
	def __init__(self, name):
		self.name = name
		self.hasBeenHit = False
		self.doesContainShip : Ship = False
		self.posx = int(ord(name[0]) - 65)
		self.posy = int(name[1])
		self.charValue = EMPTY
	
	def changeChar(self, newValue):
		self.charValue = newValue

	def hit(self):
		self.changeChar(HIT)
		self.hasBeenHit = True
		if self.doesContainShip:
			self.doesContainShip.currentDamage += 1
			return self.doesContainShip.checkDeath()

	def miss(self):
		self.changeChar(MISS)
		self.hasBeenHit = True