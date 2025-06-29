from utils import *
from ship import Ship
from board import Tile
from display import *
import random

class Player:
	def __init__(self):
		self.shipBoard = [[Tile("A1"),Tile("A2"),Tile("A3"),Tile("A4"),Tile("A5"),Tile("A6"),Tile("A7"),Tile("A8"),Tile("A9"),Tile("A10")],
						  [Tile("B1"),Tile("B2"),Tile("B3"),Tile("B4"),Tile("B5"),Tile("B6"),Tile("B7"),Tile("B8"),Tile("B9"),Tile("B10")],
						  [Tile("C1"),Tile("C2"),Tile("C3"),Tile("C4"),Tile("C5"),Tile("C6"),Tile("C7"),Tile("C8"),Tile("C9"),Tile("C10")],
						  [Tile("D1"),Tile("D2"),Tile("D3"),Tile("D4"),Tile("D5"),Tile("D6"),Tile("D7"),Tile("D8"),Tile("D9"),Tile("D10")],
						  [Tile("E1"),Tile("E2"),Tile("E3"),Tile("E4"),Tile("E5"),Tile("E6"),Tile("E7"),Tile("E8"),Tile("E9"),Tile("E10")],
						  [Tile("F1"),Tile("F2"),Tile("F3"),Tile("F4"),Tile("F5"),Tile("F6"),Tile("F7"),Tile("F8"),Tile("F9"),Tile("F10")],
						  [Tile("G1"),Tile("G2"),Tile("G3"),Tile("G4"),Tile("G5"),Tile("G6"),Tile("G7"),Tile("G8"),Tile("G9"),Tile("G10")],
						  [Tile("H1"),Tile("H2"),Tile("H3"),Tile("H4"),Tile("H5"),Tile("H6"),Tile("H7"),Tile("H8"),Tile("H9"),Tile("H10")],
						  [Tile("I1"),Tile("I2"),Tile("I3"),Tile("I4"),Tile("I5"),Tile("I6"),Tile("I7"),Tile("I8"),Tile("I9"),Tile("I10")],
						  [Tile("J1"),Tile("J2"),Tile("J3"),Tile("J4"),Tile("J5"),Tile("J6"),Tile("J7"),Tile("J8"),Tile("J9"),Tile("J10")]]

		self.pegBoard = [[Tile("A1"),Tile("A2"),Tile("A3"),Tile("A4"),Tile("A5"),Tile("A6"),Tile("A7"),Tile("A8"),Tile("A9"),Tile("A10")],
						 [Tile("B1"),Tile("B2"),Tile("B3"),Tile("B4"),Tile("B5"),Tile("B6"),Tile("B7"),Tile("B8"),Tile("B9"),Tile("B10")],
						 [Tile("C1"),Tile("C2"),Tile("C3"),Tile("C4"),Tile("C5"),Tile("C6"),Tile("C7"),Tile("C8"),Tile("C9"),Tile("C10")],
						 [Tile("D1"),Tile("D2"),Tile("D3"),Tile("D4"),Tile("D5"),Tile("D6"),Tile("D7"),Tile("D8"),Tile("D9"),Tile("D10")],
						 [Tile("E1"),Tile("E2"),Tile("E3"),Tile("E4"),Tile("E5"),Tile("E6"),Tile("E7"),Tile("E8"),Tile("E9"),Tile("E10")],
						 [Tile("F1"),Tile("F2"),Tile("F3"),Tile("F4"),Tile("F5"),Tile("F6"),Tile("F7"),Tile("F8"),Tile("F9"),Tile("F10")],
						 [Tile("G1"),Tile("G2"),Tile("G3"),Tile("G4"),Tile("G5"),Tile("G6"),Tile("G7"),Tile("G8"),Tile("G9"),Tile("G10")],
						 [Tile("H1"),Tile("H2"),Tile("H3"),Tile("H4"),Tile("H5"),Tile("H6"),Tile("H7"),Tile("H8"),Tile("H9"),Tile("H10")],
						 [Tile("I1"),Tile("I2"),Tile("I3"),Tile("I4"),Tile("I5"),Tile("I6"),Tile("I7"),Tile("I8"),Tile("I9"),Tile("I10")],
						 [Tile("J1"),Tile("J2"),Tile("J3"),Tile("J4"),Tile("J5"),Tile("J6"),Tile("J7"),Tile("J8"),Tile("J9"),Tile("J10")]]
		
		self.ships : list[Ship] = []


	def getShipDataForCreation(self, name):
		while True:
			orentation = input(f"Enter Orientation for {name} (Up/Right/Down/Left): ").lower().strip()
			if orentation not in ("up", "right", "down", "left"):
				print(f"{Fore.BLUE}Invalid orientation! Please use only Up, Right, Down, or Left.")
				continue
			startingPoint = input(f"Enter Starting Point for {name} (e.g., A1): ").upper().strip()
			if len(startingPoint) < 2 or not startingPoint[0].isalpha() or not startingPoint[1:].isdigit():
				print(f"{Fore.BLUE}Invalid starting point! Please enter a letter followed by a number, e.g., A1.")
				continue
			row = ord(startingPoint[0]) - 65
			col = int(startingPoint[1:]) - 1
			if row < 0 or row >= 10 or col < 0 or col >= 10:
				print(f"{Fore.BLUE}Starting point out of bounds! Please enter a valid cell (A1-J10).")
				continue
			return orentation, startingPoint

	def createShip(self, computer):
		ships_info = [
			("Carrier", 5),
			("Battelship", 4),
			("Cruiser", 3),
			("Submarine", 3),
			("Destroyer", 2)
		]
		for name, size in ships_info:
			while True:
				try:
					orientation, starting_point = self.getShipDataForCreation(name)
					ship = Ship(name, size, orientation, starting_point, self.shipBoard, EMPTY, SHIP, Fore)
					ship.placeShip()
					self.ships.append(ship)
					display_game(self, computer)
					break
				except TypeError as te:
					print(f"{Fore.RED}Ship placement error: {te}")
				except Exception as e:
					print(f"{Fore.RED}Error: {e}")
		while True:
			confirm = input("CONFIRM POSITION (Yes - lock the board / No - clear the entire board): ").strip().lower()
			if confirm in ("yes", "no"):
				return confirm
			else:
				print(f"{Fore.BLUE}Please enter 'Yes' to lock the board or 'No' to clear and restart ship placement.")

	def playTurn(self, computer):
		global ComputerTurn
		while True:
			cellToBeHit = input("Your Turn (e.g., A1): ").upper().strip()
			if len(cellToBeHit) < 2 or not cellToBeHit[0].isalpha() or not cellToBeHit[1:].isdigit():
				print(f"{Fore.RED}Invalid input! Please enter a letter followed by a number, e.g., A1.")
				continue
			row = ord(cellToBeHit[0]) - 65
			col = int(cellToBeHit[1:]) - 1
			if row < 0 or row >= 10 or col < 0 or col >= 10:
				print(f"{Fore.RED}Cell out of bounds! Please enter a valid cell (A1-J10).")
				continue
			if self.pegBoard[row][col].hasBeenHit:
				print(f"{Fore.RED}You have already played that turn. Please choose another cell.")
				continue
			if computer.shipBoard[row][col].doesContainShip:
				self.pegBoard[row][col].hit()
				shipThatWasDestroyed = computer.shipBoard[row][col].hit()
				computer.shipBoard[row][col].changeChar(SHIPDAMAGED)
				print(f"{Fore.YELLOW}{cellToBeHit} was a HIT!")
				if shipThatWasDestroyed:
					print(f"{Fore.LIGHTBLUE_EX}YOU DESTROYED {shipThatWasDestroyed.name} !!!")
					computer.ships.remove(shipThatWasDestroyed)


				ComputerTurn = True

			else:
				self.pegBoard[row][col].miss()
				print(f"{Fore.YELLOW}{cellToBeHit} was a MISS!")

				ComputerTurn = True
			
			return False

class Computer(Player):
	def __init__(self, player):
		super().__init__()
		self.prevHits = []  # List of (row, col) tuples where hits have occurred but ship not yet sunk
		self.player = player

	def getShipDataForCreationByComputer(self, size):
		# Try to find a valid random placement for the ship
		attempts = 0
		while attempts < 100:
			orientation = random.choice(["up", "right", "down", "left"])
			if orientation in ("up", "down"):
				row = random.randint(0, 9 - (size - 1) if orientation == "down" else size - 1)
				col = random.randint(0, 9)
			else:
				row = random.randint(0, 9)
				col = random.randint(0, 9 - (size - 1) if orientation == "right" else size - 1)
			startingPos = f"{chr(65 + row)}{col + 1}"
			if self._can_place_ship(row, col, orientation, size):
				return orientation, startingPos
			attempts += 1
		# Fallback to completely random if no valid found
		return random.choice(["up", "right", "down", "left"]), f"{chr(65 + random.randint(0,9))}{random.randint(1,10)}"

	def _can_place_ship(self, row, col, orientation, size):
		try:
			for i in range(size):
				r, c = row, col
				if orientation == "up":
					r -= i
				elif orientation == "down":
					r += i
				elif orientation == "left":
					c -= i
				elif orientation == "right":
					c += i
				if r < 0 or r >= 10 or c < 0 or c >= 10:
					return False
				if self.shipBoard[r][c].doesContainShip:
					return False
			return True
		except Exception:
			return False

	def createShip(self, computer=None):
		global ComputerTurn
		ComputerTurn = True
		ships_info = [
			("Carrier", 5),
			("Battelship", 4),
			("Cruiser", 3),
			("Submarine", 3),
			("Destroyer", 2)
		]
		for name, size in ships_info:
			while True:
				try:
					orientation, starting_point = self.getShipDataForCreationByComputer(size)
					ship = Ship(name, size, orientation, starting_point, self.shipBoard, EMPTY, SHIP, Fore)
					ship.placeShip()
					self.ships.append(ship)
					break
				except Exception:
					pass
		ComputerTurn = False
		return "yes"

	def get_adjacent_cells(self, row, col):
		# Returns list of valid adjacent (row, col) tuples
		directions = [(-1,0), (1,0), (0,-1), (0,1)]
		adj = []
		for dr, dc in directions:
			r, c = row + dr, col + dc
			if 0 <= r < 10 and 0 <= c < 10 and not self.pegBoard[r][c].hasBeenHit:
				adj.append((r, c))
		return adj

	def find_best_target(self):
		# If there are previous hits, try to finish the ship by targeting adjacent cells
		if self.prevHits:
			# Try to extend in a line if more than one hit in a row/col
			if len(self.prevHits) > 1:
				# Check if hits are aligned horizontally or vertically
				rows = [r for r, c in self.prevHits]
				cols = [c for r, c in self.prevHits]
				if all(r == rows[0] for r in rows):  # Horizontal
					min_c, max_c = min(cols), max(cols)
					row = rows[0]
					# Try to extend left
					if min_c - 1 >= 0 and not self.pegBoard[row][min_c - 1].hasBeenHit:
						return (row, min_c - 1)
					# Try to extend right
					if max_c + 1 < 10 and not self.pegBoard[row][max_c + 1].hasBeenHit:
						return (row, max_c + 1)
				elif all(c == cols[0] for c in cols):  # Vertical
					min_r, max_r = min(rows), max(rows)
					col = cols[0]
					# Try to extend up
					if min_r - 1 >= 0 and not self.pegBoard[min_r - 1][col].hasBeenHit:
						return (min_r - 1, col)
					# Try to extend down
					if max_r + 1 < 10 and not self.pegBoard[max_r + 1][col].hasBeenHit:
						return (max_r + 1, col)
			# Otherwise, pick any adjacent cell to a hit
			random.shuffle(self.prevHits)
			for r, c in self.prevHits:
				adj = self.get_adjacent_cells(r, c)
				if adj:
					return random.choice(adj)
		# If no hits to follow up, use probability map
		return self.highest_probability_cell()

	def highest_probability_cell(self):
		# Build a probability map for all remaining ships
		probability = [[0 for _ in range(10)] for _ in range(10)]
		remaining_ship_sizes = [ship.getShipSize() for ship in self.player.ships if not ship.isDestroyed]
		for ship_size in remaining_ship_sizes:
			# Horizontal
			for i in range(10):
				for j in range(11 - ship_size):
					if all(not self.pegBoard[i][j + k].hasBeenHit for k in range(ship_size)):
						for k in range(ship_size):
							probability[i][j + k] += 1
			# Vertical
			for i in range(11 - ship_size):
				for j in range(10):
					if all(not self.pegBoard[i + k][j].hasBeenHit for k in range(ship_size)):
						for k in range(ship_size):
							probability[i + k][j] += 1
		# Find the cell with the highest probability
		max_prob = -1
		candidates = []
		for i in range(10):
			for j in range(10):
				if not self.pegBoard[i][j].hasBeenHit:
					if probability[i][j] > max_prob:
						max_prob = probability[i][j]
						candidates = [(i, j)]
					elif probability[i][j] == max_prob:
						candidates.append((i, j))
		return random.choice(candidates) if candidates else (random.randint(0, 9), random.randint(0, 9))

	def ComputerPlayTurn(self, cell):
		r, c = cell
		if self.player.shipBoard[r][c].doesContainShip:
			self.pegBoard[r][c].hit()
			shipThatWasDestroyed = self.player.shipBoard[r][c].hit()
			self.player.shipBoard[r][c].changeChar(SHIPDAMAGED)
			return True, shipThatWasDestroyed
		else:
			self.pegBoard[r][c].miss()
			return False, None

	def playTurn(self, computer=None):
		global ComputerTurn
		cell = self.find_best_target()
		hit, shipThatWasDestroyed = self.ComputerPlayTurn(cell)
		cell_str = f"{chr(cell[0] + 65)}{cell[1] + 1}"
		if hit:
			print(f"{Fore.YELLOW}COMPUTER PLAYED {cell_str} and it is a HIT!")
			if cell not in self.prevHits:
				self.prevHits.append(cell)
			if shipThatWasDestroyed:
				print(f"{Fore.LIGHTBLUE_EX}YOUR {shipThatWasDestroyed.name} WAS DESTROYED !!!")
				self.player.ships.remove(shipThatWasDestroyed)
				# Remove all hit cells for this ship from prevHits
				self.prevHits = [pos for pos in self.prevHits if self.player.shipBoard[pos[0]][pos[1]].doesContainShip != shipThatWasDestroyed]
		else:
			print(f"{Fore.YELLOW}COMPUTER PLAYED {cell_str} and it is a MISS!")
		ComputerTurn = False