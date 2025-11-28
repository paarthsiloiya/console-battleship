class Ship:
	def __init__(self, name: str, size: int, orientation: str, starting_point: str, board, EMPTY, SHIP):
		self.name = name.upper()
		self.size = size
		self.orientation = orientation
		self.starting_point = starting_point
		self.board = board
		self.EMPTY = EMPTY
		self.SHIP = SHIP
		self.tilesCovered = self.getTilesForPlacements()
		self.isDestroyed = False
		self.currentDamage = 0

	def getTilesForPlacements(self) -> list:
		tilesCovered = []
		row = ord(self.starting_point[0].upper()) - 65
		col = int(self.starting_point[1:]) - 1
		for i in range(self.size):
			if self.orientation == "up":
				r, c = row - i, col
			elif self.orientation == "right":
				r, c = row, col + i
			elif self.orientation == "down":
				r, c = row + i, col
			elif self.orientation == "left":
				r, c = row, col - i
			else:
				raise Exception("Invalid orientation")

			if r < 0 or r >= len(self.board) or c < 0 or c >= len(self.board[0]):
				raise Exception("Ship out of bounds")
			tile = self.board[r][c]
			if tile.charValue != self.EMPTY:
				raise TypeError(tile.name)
			tilesCovered.append(tile)
		return tilesCovered

	def placeShip(self):
		for tile in self.tilesCovered:
			tile.changeChar(self.SHIP)
			tile.doesContainShip = self

	def checkDeath(self):
		if self.size == self.currentDamage:
			self.isDestroyed = True
			return self
		else:
			return False

	def getShipSize(self):
		return self.size
