from utils import *
from colorama import init, Fore, Back
init(autoreset=True)


def displayPlayerShipBar(computer):
	print(" "*13 ,end="")
	for _ in range(5 - len(computer.ships)):
		print(f"  {MYSHIPHIT}  " ,end="")
	for _ in computer.ships:
		print(f"  {MISS}  " ,end="")
	print()
	print()


def displayPlayersPegBoard(player):
	grid_size = len(player.pegBoard)
	for j in range(grid_size):
		print("    " + str(j+1), end="")
	print()
	print("  ┌"+ ((("─"*4)+"┬")*grid_size) + "\b┐")
	for i in range(grid_size):
		print(chr(i+ 65), end=(" │ "))
		for j in range(grid_size):
			print(player.pegBoard[i][j].charValue + " │ ", end="")
		print()
		if i < grid_size-1:
			print("  ├─", end="")
			for j in range(grid_size):
				print("─"*2 + "─" + "┼" + "─", end="")
			print("\b\b┤ ")
	print("  └"+ ((("─"*4)+"┴")*grid_size) + "\b┘")


def displayPlayesShipBoard(player):
	grid_size = len(player.shipBoard)
	for j in range(grid_size):
		print("    " + str(j+1), end="")
	print()
	print("  ┌"+ ((("─"*4)+"┬")*grid_size) + "\b┐")
	for i in range(grid_size):
		print(chr(i+ 65), end=(" │ "))
		for j in range(grid_size):
			if player.shipBoard[i][j].doesContainShip:
				if j < grid_size - 1:
					if player.shipBoard[i][j+1].doesContainShip == player.shipBoard[i][j].doesContainShip:
						if player.shipBoard[i][j].hasBeenHit:
							print(player.shipBoard[i][j].charValue + "░░░", end="")
						else:
							print(player.shipBoard[i][j].charValue + f"{Fore.WHITE}███", end="")
					else:
						print(player.shipBoard[i][j].charValue + " │ ",end="")
				else:
					print(player.shipBoard[i][j].charValue + " │ ",end="")
			else:
				print(player.shipBoard[i][j].charValue + " │ ", end="")
		print()
		if i < grid_size-1:
			print("  ├─", end="")
			for j in range(grid_size):
				if player.shipBoard[i][j].doesContainShip:
					if player.shipBoard[i+1][j].doesContainShip == player.shipBoard[i][j].doesContainShip:
						print(player.shipBoard[i][j].charValue + "─" + "┼" + "─", end="")
					else:
						print("─"*2 + "─" + "┼" + "─", end="")
				else:
					print("─"*2 + "─" + "┼" + "─", end="")
			print("\b\b┤ ")
	print("  └"+ ((("─"*4)+"┴")*grid_size) + "\b┘")


def display_game(player, computer):
	from os import system, name as os_name
	system('cls' if os_name == 'nt' else 'clear')
	displayPlayerShipBar(computer)
	displayPlayersPegBoard(player)
	print("─"*55)
	displayPlayesShipBoard(player)
	print(f"{Back.WHITE}{Fore.WHITE}─"*120)
	print()



