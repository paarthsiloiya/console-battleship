from colorama import init
from player import Player, Computer
from board import Tile
from display import *
from utils import *

init(autoreset=True)

print(INTRO)
print(HELPMENUE)
print("█"*200, end="\n\n")
input("Press Enter to start the game...")

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

turn_number = 1

def PlayGame():
    global turn_number
    print(f"{Fore.CYAN}Turn {turn_number}")
    turnConfirmation = True
    player_message = ""
    while turnConfirmation:
        turnConfirmation, player_message = player.playTurn(computer)
    computer_message = computer.playTurn()
    display_game(player, computer)
    if player_message:
        print(player_message)
    if computer_message:
        print(computer_message)
    turn_number += 1
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
