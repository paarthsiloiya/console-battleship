from colorama import init
from player import Player, Computer
from board import Tile
from display import *
from utils import *

init(autoreset=True)

ComputerTurn = False

print(INTRO)
print(HELPMENUE)
print("█"*200, end="\n\n\n")

player = Player()
computer = Computer(player)

def checkWin():
	for ship in computer.ships:
		if not ship.isDestroyed:
			break
	else:
		print()
		print("PLAYER WON !!!")
		return True

	for ship in player.ships:
		if not ship.isDestroyed:
			break
	else:
		print()
		print("COMPUTER WON !!!")
		return True

	return False

def PlayGame():
	turnConfirmation = True
	while turnConfirmation:
		turnConfirmation = player.playTurn(computer)
	display_game(player, computer)
	computer.playTurn()
	return checkWin()

def startGame():
	computer.createShip()
	display_game(player, computer)

	while True:
		confimation = player.createShip(computer)
		if confimation.lower().strip() == "yes":
			break
		else:
			player.ships = []
			player.shipBoard = [
				[Tile(f"{chr(65 + i)}{j+1}") for j in range(10)]
				for i in range(10)
			]

	while True:
		win_confimation = PlayGame()
		if win_confimation:
			break

if __name__ == "__main__":
	startGame()

'''

			   🞅     🞅     🞅     🞅     🞅   

	1    2    3    4    5    6    7    8    9    10
  ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
A │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
B │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
C │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
D │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
E │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
F │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
G │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
H │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
I │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
J │    │    │    │    │    │    │    │    │    │    │ 
  └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
───────────────────────────────────────────────────────
	1    2    3    4    5    6    7    8    9    10
  ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
A │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
B │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
C │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
D │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
E │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
F │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
G │    │    │    │    │    │    │    │    │    │    │ 
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
H │    │    │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
I │    │    │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤ 
J │    │    │    │    │    │    │    │    │    │    │
  └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

'''