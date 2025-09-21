from colorama import Fore, init, Back
init(autoreset=True)

SHIP = f"{Fore.WHITE}██"
SHIPDAMAGED = "░░"
HIT = f"{Fore.RED}🞮{Fore.WHITE}  \b"
MISS = "🞅  \b"
MYSHIPHIT = "⦿  \b"
EMPTY = "  "

 
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