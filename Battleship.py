from os import system, name as os_name
import random
from colorama import Fore, init, Back
init(autoreset=True)

SHIP = f"{Fore.WHITE}██"
SHIPDAMAGED = "░░"
HIT = f"{Fore.RED}🞮{Fore.WHITE}  \b"
MISS = "🞅  \b"
MYSHIPHIT = "⦿  \b"
EMPTY = "  "
ComputerTurn = False

 
INTRO = f'''
 __          __  _                            _______       ____        _   _   _           _     _        
 \ \        / / | |                          |__   __|     |  _ \      | | | | | |         | |   (_)       
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___    | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __   
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \   |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \  
    \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) |  | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) | 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/   |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/  
                                                                                                   | |     
                                                                                                   |_|     
                                                                                                           

By Paarth Siloiya
'''


HELPMENUE = '''

Cell Position is typed out as ROW first then COLUMN without space in between. E.g. a3, f5

Game starts with placing your ships. There are all the five standard ships Carrier, Battleship, Cruiser, Submarine, Destroyer
The game firsts ask you the orientation of the ship, then the starting tile of the ship
Here are a few examples:

    CRUISER - with orentation right                          SUBMARINE - with orentation down       
              and starting position d4                                   and starting point e6      

         4    5    6    7    8    9                                    5    6    7                  
     ──┼────┼────┼────┼────┼────┼───                                   ───┼────┼──                  
   C   │    │    │    │    │    │                                    D    │    │                    
     ──┼────┼────┼────┼────┼────┼───                                   ───┼────┼──                  
   D   │ ██████████████████████ │                                    E    │ ██ │                    
     ──┼────┼────┼────┼────┼────┼───                                   ───┼─██─┼──                  
   E   │    │    │    │    │    │                                    F    │ ██ │                    
     ──┼────┼────┼────┼────┼────┼───                                   ───┼─██─┼──                  
                                                                     G    │ ██ │                    
                                                                       ───┼────┼──                  
                                                                     H    │    │                    



After placing all the ship if you are satisfied with your placements you can confirm it, or you can reset the board and start fresh.

You Always start first, to play your move type out the cell position then if you guessed correctly or incorrectly a corresponding message will appear.

You can keep track of the ships you destroyed by the visual Indicator at the top.

                    ⦿     🞅     🞅     🞅     🞅


Now the standard rules of battleship applies.

'''


print(INTRO)
print(HELPMENUE)
print("█"*200,end="\n\n\n")


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
        orentation = input(f"Enter Orentation for {name} (Up/Right/Down/Left) : ").lower().strip()
        startingPoint = input(f"Enter Starting Point for {name} : ").upper().strip()
        if not (("up" == orentation) or ("right" == orentation) or ("down" == orentation) or ("left" == orentation)):
            print(f"{Fore.BLUE}Use only Up, Right, Down, Left in orentation")
            raise Exception("Use only Top, Right, Down, Left in orentation")
        return orentation, startingPoint

    def createShip(self):
        while True:
            try:
                CarrierData = self.getShipDataForCreation("Carrier")
                Carrier = Ship("Carrier", 5, CarrierData[0], CarrierData[1])
                Carrier.placeShip()
                self.ships.append(Carrier)
                display_game()
                break
            except:
                pass

        while True:
            try:
                BattelshipData = self.getShipDataForCreation("Battelship")
                Battelship = Ship("Battelship", 4, BattelshipData[0], BattelshipData[1])
                Battelship.placeShip()
                self.ships.append(Battelship)
                display_game()
                break
            except:
                pass

        while True:
            try:
                CruiserData = self.getShipDataForCreation("Cruiser")
                Cruiser = Ship("Cruiser", 3, CruiserData[0], CruiserData[1])
                Cruiser.placeShip()
                self.ships.append(Cruiser)
                display_game()
                break
            except:
                pass

        while True:
            try:
                SubmarineData = self.getShipDataForCreation("Submarine")
                Submarine = Ship("Submarine", 3, SubmarineData[0], SubmarineData[1])
                Submarine.placeShip()
                self.ships.append(Submarine)
                display_game()
                break
            except:
                pass

        while True:
            try:
                DestroyerData = self.getShipDataForCreation("Destroyer")
                Destroyer = Ship("Destroyer", 2, DestroyerData[0], DestroyerData[1])
                Destroyer.placeShip()
                self.ships.append(Destroyer)
                display_game()
                break
            except:
                pass

        return input("CONFIRM POSITION (Yes - lock the board / No - clear the entire board) : ")


    def playTurn(self):
        global ComputerTurn
        cellToBeHit = input("Your Turn : ").upper()
        try:
            if not self.pegBoard[ord(cellToBeHit[0]) - 65][int(cellToBeHit[1:]) - 1].hasBeenHit:
                if computer.shipBoard[ord(cellToBeHit[0]) - 65][int(cellToBeHit[1:]) - 1].doesContainShip:
                    self.pegBoard[ord(cellToBeHit[0]) - 65][int(cellToBeHit[1:]) - 1].hit()
                    shipThatWasDestroyed = computer.shipBoard[ord(cellToBeHit[0]) - 65][int(cellToBeHit[1:]) - 1].hit()
                    computer.shipBoard[ord(cellToBeHit[0]) - 65][int(cellToBeHit[1:]) - 1].changeChar(SHIPDAMAGED)
                    print(f"{Fore.YELLOW}{cellToBeHit} was a HIT!")

                    if shipThatWasDestroyed:
                        print(f"{Fore.LIGHTBLUE_EX}YOU DESTROYED {shipThatWasDestroyed.name} !!!", )
                        computer.ships.remove(shipThatWasDestroyed)


                    ComputerTurn = True

                else:
                    self.pegBoard[ord(cellToBeHit[0]) - 65][int(cellToBeHit[1:]) - 1].miss()
                    print(f"{Fore.YELLOW}{cellToBeHit} was a MISS!")

                    ComputerTurn = True
                
                return False

            else:
                print(f"{Fore.RED}YOU PLAYED THAT TURN ALREADY PLAY ANOTHER ONE")
                return "re-turn"
        except:
            print(f"{Fore.RED}TRY AGAIN")
            return "re-turn"



class Computer:
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

        self.prevHitMoveMemory = {"prevMoveHitCell": None, "Ship":False}

    
    def getShipDataForCreationByComputer(self):
        startingPos= chr(random.randint(65, 74)) + str(random.randint(0,9))
        orentation = random.choice(["up", "right", "down", "left"])
        return (orentation, startingPos)
            

    def createShip(self):
        global ComputerTurn

        ComputerTurn = True

        while True:
            try:
                CarrierData = self.getShipDataForCreationByComputer()
                Carrier = Ship("Carrier", 5, CarrierData[0], CarrierData[1])
                Carrier.placeShip()
                self.ships.append(Carrier)
                break
            except:
                pass

        while True:
            try:
                BattelshipData = self.getShipDataForCreationByComputer()
                Battelship = Ship("Battelship", 4, BattelshipData[0], BattelshipData[1])
                Battelship.placeShip()
                self.ships.append(Battelship)
                break
            except:
                pass

        while True:
            try:
                CruiserData = self.getShipDataForCreationByComputer()
                Cruiser = Ship("Cruiser", 3, CruiserData[0], CruiserData[1])
                Cruiser.placeShip()
                self.ships.append(Cruiser)
                break
            except:
                pass

        while True:
            try:
                SubmarineData = self.getShipDataForCreationByComputer()
                Submarine = Ship("Submarine", 3, SubmarineData[0], SubmarineData[1])
                Submarine.placeShip()
                self.ships.append(Submarine)
                break
            except:
                pass

        while True:
            try:
                DestroyerData = self.getShipDataForCreationByComputer()
                Destroyer = Ship("Destroyer", 2, DestroyerData[0], DestroyerData[1])
                Destroyer.placeShip()
                self.ships.append(Destroyer)
                break
            except:
                pass

        # display_game()

        ComputerTurn = False
        return "yes"
    

    def CalculateProbabilityMap(self):
        # c = 0
        probabilityMap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # print(len(playersShips))
        for ship in player.ships:
            for i in range(len(self.pegBoard)):
                for j in range(len(self.pegBoard[i])):
                    if not self.pegBoard[i][j].hasBeenHit:
                        shipSize = ship.getShipSize()
                        # Check horizontal placement
                        if j + shipSize <= len(self.pegBoard[i]) and all(
                            not self.pegBoard[i][j + tileCountHor].hasBeenHit for tileCountHor in range(shipSize)
                        ):
                            for tileCount in range(shipSize):
                                # c+=1
                                probabilityMap[i][j + tileCount] += 1

                        # Check vertical placement
                        if i + shipSize <= len(self.pegBoard) and all(
                            not self.pegBoard[i + tileCountVert][j].hasBeenHit for tileCountVert in range(shipSize)
                        ):
                            for tileCount in range(shipSize):
                                # c+=1
                                probabilityMap[i + tileCount][j] += 1
                            
        heighestProbaility = 0
        heighestProbailityCell = (0, 0) 
        for i in range(len(probabilityMap)):
            for j in range(len(probabilityMap[i])):
                # print(probabilityMap[i][j], end=' ')
                if probabilityMap[i][j] > heighestProbaility:
                    heighestProbaility = probabilityMap[i][j]
                    heighestProbailityCell = (i,j)
            # print()

        
        # print(c, heighestProbailityCell, heighestProbaility, probabilityMap[0][0])
        return probabilityMap, heighestProbailityCell, heighestProbaility
    

    def seekShip(self):
        currentHeigestProbability = 0
        cellToAttack = (0,0)

        map, cell, probability = self.CalculateProbabilityMap()
        map[self.prevHitMoveMemory["prevMoveHitCell"][0]][self.prevHitMoveMemory["prevMoveHitCell"][1]] = 0

        # for i in map:
        #     print(i)
        
        for i in range(len(map)):
            for j in range(len(map[i])):
                distance_sq = ((self.prevHitMoveMemory["prevMoveHitCell"][0] - i)**2 + (self.prevHitMoveMemory["prevMoveHitCell"][1] - j)**2)
                if distance_sq != 0 and player.pegBoard[i][j].hasBeenHit == False:
                    map[i][j] *= abs((1/distance_sq))
                    # map[i][j] = round(map[i][j])
                    if map[i][j] > currentHeigestProbability:
                        currentHeigestProbability = map[i][j]
                        cellToAttack = (i,j)
                

        # for i in map:
        #     print(i)
        
        return cellToAttack



    def ComputerPlayTurn(self, cell):
        if player.shipBoard[cell[0]][cell[1]].doesContainShip:
            self.pegBoard[cell[0]][cell[1]].hit()
            shipThatWasDestroyed =  player.shipBoard[cell[0]][cell[1]].hit()
            player.shipBoard[cell[0]][cell[1]].changeChar(SHIPDAMAGED)

            return True, shipThatWasDestroyed

        else:
            self.pegBoard[cell[0]][cell[1]].miss()
            return False, None


    def playTurn(self):
        global ComputerTurn

        if self.prevHitMoveMemory["prevMoveHitCell"]:
        # Preveous Move was a Hit
            cell = self.seekShip()
            turn, shipThatWasDestroyed = self.ComputerPlayTurn(cell)
            if self.prevHitMoveMemory["Ship"] == shipThatWasDestroyed:
                if turn:
                    print(f"{Fore.YELLOW}COMPUTER PLAYED {chr(cell[0] + 65) + str(cell[1] + 1)} and it is a HIT!")
                    self.prevHitMoveMemory["prevMoveHitCell"] = cell
                    if shipThatWasDestroyed:
                        print(f"{Fore.LIGHTBLUE_EX}YOUR {shipThatWasDestroyed.name} WAS DESTROYED !!!", )
                        player.ships.remove(shipThatWasDestroyed)
                        self.prevHitMoveMemory["prevMoveHitCell"] = None
                else:
                    print(f"{Fore.YELLOW}COMPUTER PLAYED {chr(cell[0] + 65) + str(cell[1] + 1)} and it is a MISS!")
            else:
                pass
                #Computer found another ship while destroying the current one
        else:
            map, cell, probability = self.CalculateProbabilityMap()
            
            turn, shipThatWasDestroyed = self.ComputerPlayTurn(cell)
            if turn:
                print(f"{Fore.YELLOW}COMPUTER PLAYED {chr(cell[0] + 65) + str(cell[1] + 1)} and it is a HIT!")
                self.prevHitMoveMemory["prevMoveHitCell"] = cell
                self.prevHitMoveMemory["Ship"] = player.shipBoard[cell[0]][cell[1]].doesContainShip
                if shipThatWasDestroyed:
                    print(f"{Fore.LIGHTBLUE_EX}YOUR {shipThatWasDestroyed.name} WAS DESTROYED !!!", )
                    player.ships.remove(shipThatWasDestroyed)
            else:
                print(f"{Fore.YELLOW}COMPUTER PLAYED {chr(cell[0] + 65) + str(cell[1] + 1)} and it is a MISS!")
        
        
        # for i in map:
        #     print(i)

        # print(cell, "-->", probability)
                
        ComputerTurn = False
            


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



class Ship:
    def __init__(self, name: str, size: int, orentation, startingPoint):
        self.name = name.upper()
        self.size = size
        self.orentation = orentation
        self.tilesCovered = self.getTilesForPlacements(startingPoint)
        self.isDestroyed = False
        self.currentDamage = 0

    def getTilesForPlacements(self, startingPoint) -> list[Tile]:
        tilesCovered = []
        try:
            if self.orentation == "up":
                for i in range(self.size):
                    if int(ord(startingPoint[0]) - i - 65) < 0 or (int(startingPoint[1:]) - 1) < 0:
                        raise Exception
                    if ComputerTurn:
                        tile = computer.shipBoard[int(ord(startingPoint[0]) - i - 65)][int(startingPoint[1:]) - 1]
                    else:
                        tile = player.shipBoard[int(ord(startingPoint[0]) - i - 65)][int(startingPoint[1:]) - 1]
                    if tile.charValue != EMPTY:
                        raise TypeError(tile.name)
                    tilesCovered.append(tile)
            elif self.orentation == "right":
                for i in range(self.size):
                    if int(ord(startingPoint[0]) - 65) < 0 or (int(startingPoint[1:]) - 1 + i) < 0:
                        raise Exception
                    if ComputerTurn:
                        tile = computer.shipBoard[int(ord(startingPoint[0]) - 65)][int(startingPoint[1:]) - 1 + i]
                    else:
                        tile = player.shipBoard[int(ord(startingPoint[0]) - 65)][int(startingPoint[1:]) - 1 + i]
                    if tile.charValue != EMPTY:
                        raise TypeError(tile.name)
                    tilesCovered.append(tile)
            elif self.orentation == "down":
                for i in range(self.size):
                    if int(ord(startingPoint[0]) + i - 65) < 0 or (int(startingPoint[1:]) - 1) < 0:
                        raise Exception
                    if ComputerTurn:
                        tile = computer.shipBoard[int(ord(startingPoint[0]) + i - 65)][int(startingPoint[1:]) - 1]
                    else:
                        tile = player.shipBoard[int(ord(startingPoint[0]) + i - 65)][int(startingPoint[1:]) - 1]
                    if tile.charValue != EMPTY:
                        raise TypeError(tile.name)
                    tilesCovered.append(tile)
            elif self.orentation == "left":
                for i in range(self.size):
                    if int(ord(startingPoint[0]) - 65) < 0 or (int(startingPoint[1:]) - 1 - i) < 0:
                        raise Exception
                    if ComputerTurn:
                        tile = computer.shipBoard[int(ord(startingPoint[0]) - 65)][int(startingPoint[1:]) - 1 - i]
                    else:
                        tile = player.shipBoard[int(ord(startingPoint[0]) - 65)][int(startingPoint[1:]) - 1 - i]
                    if tile.charValue != EMPTY:
                        raise TypeError(tile.name)
                    tilesCovered.append(tile)
            # print(tilesCovered)
            return tilesCovered
        except TypeError as err:
            if not ComputerTurn:
                print(f"{Fore.LIGHTBLUE_EX}Another Ship Already Placed on {err.args[0]}")
        except:
            if not ComputerTurn:
                print(f"{Fore.LIGHTBLUE_EX}Check The Orentation Again Or Starting Point Again The Ship May Be Out Of Bounds")

    def placeShip(self):
        for tile in self.tilesCovered:
            tile.changeChar(SHIP)
            tile.doesContainShip = self

    def checkDeath(self):
        if self.size == self.currentDamage:
            self.isDestroyed = True
            return self
        else:
            return False
        
    def getShipSize(self):
        return self.size


player = Player()
computer = Computer()


def displayPlayerShipBar():
    print(" "*13 ,end="")
    for _ in range(5 - len(computer.ships)):
        print(f"  {MYSHIPHIT}  " ,end="")
    
    for _ in computer.ships:
        print(f"  {MISS}  " ,end="")
    
    print()
    print()


def displayPlayersPegBoard():
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


def displayPlayesShipBoard():
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


def showComputerShipBoard():
    grid_size = len(computer.shipBoard)
    for j in range(grid_size):
        print("    " + str(j+1), end="")
    print()
    print("  ┌"+ ((("─"*4)+"┬")*grid_size) + "\b┐")
    for i in range(grid_size):
        print(chr(i+ 65), end=(" │ "))
        for j in range(grid_size):
            if computer.shipBoard[i][j].doesContainShip:
                if j < grid_size - 1:
                    if computer.shipBoard[i][j+1].doesContainShip == computer.shipBoard[i][j].doesContainShip:
                        if computer.shipBoard[i][j].hasBeenHit:
                            print(computer.shipBoard[i][j].charValue + "░░░", end="")
                        else:
                            print(computer.shipBoard[i][j].charValue + f"{Fore.WHITE}███", end="")
                    else:
                        print(computer.shipBoard[i][j].charValue + " │ ",end="")
                else:
                    print(computer.shipBoard[i][j].charValue + " │ ",end="")
            else:
                print(computer.shipBoard[i][j].charValue + " │ ", end="")
        print()
        if i < grid_size-1:
            print("  ├─", end="")
            for j in range(grid_size):
                if computer.shipBoard[i][j].doesContainShip:
                    if computer.shipBoard[i+1][j].doesContainShip == computer.shipBoard[i][j].doesContainShip:
                        print(computer.shipBoard[i][j].charValue + "─" + "┼" + "─", end="")
                    else:
                        print("─"*2 + "─" + "┼" + "─", end="")
                else:
                    print("─"*2 + "─" + "┼" + "─", end="")
            print("\b\b┤ ")
    print("  └"+ ((("─"*4)+"┴")*grid_size) + "\b┘")


def displayVomputerPegBoard():
    grid_size = len(computer.pegBoard)
    for j in range(grid_size):
        print("    " + str(j+1), end="")
    print()
    print("  ┌"+ ((("─"*4)+"┬")*grid_size) + "\b┐")
    for i in range(grid_size):
        print(chr(i+ 65), end=(" │ "))
        for j in range(grid_size):
            print(computer.pegBoard[i][j].charValue + " │ ", end="")
        print()
        if i < grid_size-1:
            print("  ├─", end="")
            for j in range(grid_size):
                print("─"*2 + "─" + "┼" + "─", end="")
            print("\b\b┤ ")
    print("  └"+ ((("─"*4)+"┴")*grid_size) + "\b┘")


def display_game():
    system('cls' if os_name == 'nt' else 'clear') # clears the screen

    # print("PLAYER")
    displayPlayerShipBar()
    displayPlayersPegBoard()
    print("─"*55)
    displayPlayesShipBoard()
    print(f"{Back.WHITE}{Fore.WHITE}─"*120)
    print()
    # print("COMPUTER")
    # displayVomputerPegBoard()
    # print("─"*55)
    # showComputerShipBoard()
    # print(f"{Back.MAGENTA}{Fore.MAGENTA}─"*120)



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
        turnConfirmation =  player.playTurn()
    display_game()
    computer.playTurn()
    return checkWin()



def startGame():
    computer.createShip()
    display_game()

    while True:
        confimation = player.createShip()
        if confimation.lower().strip() == "yes":
            break
        else:
            player.ships = []
            player.shipBoard = [[Tile("A1"),Tile("A2"),Tile("A3"),Tile("A4"),Tile("A5"),Tile("A6"),Tile("A7"),Tile("A8"),Tile("A9"),Tile("A10")],
                                [Tile("B1"),Tile("B2"),Tile("B3"),Tile("B4"),Tile("B5"),Tile("B6"),Tile("B7"),Tile("B8"),Tile("B9"),Tile("B10")],
                                [Tile("C1"),Tile("C2"),Tile("C3"),Tile("C4"),Tile("C5"),Tile("C6"),Tile("C7"),Tile("C8"),Tile("C9"),Tile("C10")],
                                [Tile("D1"),Tile("D2"),Tile("D3"),Tile("D4"),Tile("D5"),Tile("D6"),Tile("D7"),Tile("D8"),Tile("D9"),Tile("D10")],
                                [Tile("E1"),Tile("E2"),Tile("E3"),Tile("E4"),Tile("E5"),Tile("E6"),Tile("E7"),Tile("E8"),Tile("E9"),Tile("E10")],
                                [Tile("F1"),Tile("F2"),Tile("F3"),Tile("F4"),Tile("F5"),Tile("F6"),Tile("F7"),Tile("F8"),Tile("F9"),Tile("F10")],
                                [Tile("G1"),Tile("G2"),Tile("G3"),Tile("G4"),Tile("G5"),Tile("G6"),Tile("G7"),Tile("G8"),Tile("G9"),Tile("G10")],
                                [Tile("H1"),Tile("H2"),Tile("H3"),Tile("H4"),Tile("H5"),Tile("H6"),Tile("H7"),Tile("H8"),Tile("H9"),Tile("H10")],
                                [Tile("I1"),Tile("I2"),Tile("I3"),Tile("I4"),Tile("I5"),Tile("I6"),Tile("I7"),Tile("I8"),Tile("I9"),Tile("I10")],
                                [Tile("J1"),Tile("J2"),Tile("J3"),Tile("J4"),Tile("J5"),Tile("J6"),Tile("J7"),Tile("J8"),Tile("J9"),Tile("J10")]]
        
    
    
    while True:
        win_confimation = PlayGame()
        if win_confimation:
            break


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