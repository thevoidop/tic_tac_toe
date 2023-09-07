import random
import time

gameList = [1, 2, 3, 4, 5, 6, 7, 8, 9] #This list stores the characters of the game board
def gameBoard(gameList):
    # This function takes gameList as an input and prints the game board and is updated with the list
    print(f"\n\t\t   {gameList[0]}   |   {gameList[1]}   |   {gameList[2]}")
    print("\t\t-----------------------")
    print(f"\t\t   {gameList[3]}   |   {gameList[4]}   |   {gameList[5]}")
    print("\t\t-----------------------")
    print(f"\t\t   {gameList[6]}   |   {gameList[7]}   |   {gameList[8]}\n")
      
def gameResult(gameList):
    #This function checks the outcome of the game
    # All possible Winning conditions for player X
    if (gameList[0] == gameList[1] == gameList[2] == "X") or (gameList[3] == gameList[4] == gameList[5] == "X") or (gameList[6] == gameList[7] == gameList[8] == "X") or (gameList[0] == gameList[3] == gameList[6] == "X") or (gameList[1] == gameList[4] == gameList[7] == "X") or (gameList[2] == gameList[5] == gameList[8] == "X") or (gameList[0] == gameList[4] == gameList[8] == "X") or (gameList[2] == gameList[4] == gameList[6] == "X"):
       print("Player X Wins!")
       exit()
    # All possible Winning conditions for player Y
    elif (gameList[0] == gameList[1] == gameList[2] == "O") or (gameList[3] == gameList[4] == gameList[5] == "O") or (gameList[6] == gameList[7] == gameList[8] == "O") or (gameList[0] == gameList[3] == gameList[6] == "O") or (gameList[1] == gameList[4] == gameList[7] == "O") or (gameList[2] == gameList[5] == gameList[8] == "O") or (gameList[0] == gameList[4] == gameList[8] == "O") or (gameList[2] == gameList[4] == gameList[6] == "O"): 
        print("Player O Wins!")
        exit()
    # checks the draw condition    
    elif (all(items == "X" or items == "O" for items in gameList)):
        print("This game is a Draw!")
        exit()
        
def singlePlayer(gameList):
    #This function is for single player game mode
    gameBoard(gameList)
    turn = random.randint(1,2) # first turn is selected randomly
    while True:
        try:
            # Player X's turn
            if turn == 1:
                xInput = int(input("Your Turn (Enter number to place X): "))
                if 0 < xInput < 10 : # checks if input is between 1 and 9
                    if xInput not in gameList: # checks if space is available at the entered position
                        print("This spot is blocked")
                        continue
                    gameList[xInput-1] = "X"
                    gameBoard(gameList)
                    gameResult(gameList)
                    turn += 1 # turn is switched
                    
            elif turn == 2:
                # CPU's Turn
                time.sleep(0.6)
                oInput = random.randint(1,9)  # CPU chooses a random spot
                if oInput not in gameList: # checks if space is available at the entered position
                    continue
                print(f"CPU has played at {oInput}")
                gameList[oInput-1] = "O"
                gameBoard(gameList)
                gameResult(gameList)
                turn -= 1 # turn is switched
        except Exception as e:
            print("Enter a valid spot")     
    
def multiPlayer(gameList):
    gameBoard(gameList)
    turn = random.randint(1,2)
    while True:
        try: # Loops till a valid option is entered
            if turn == 1:
                xInput = int(input("X's Turn (Enter number to place X): "))
                if 0 < xInput < 10 : # checks if input is between 1 and 9
                    if xInput not in gameList: # checks if space is available at the entered position
                        print("This spot is blocked")
                        continue # starts the loop again if spot is blocked
                    gameList[xInput-1] = "X"
                    gameBoard(gameList)
                    gameResult(gameList)
                    turn += 1
                    
            elif turn == 2:
                oInput = int(input("O's Turn (Enter number to place O): "))   
                if 0 < oInput < 10 : # checks if input is between 1 and 9
                    if oInput not in gameList: # checks if space is available at the entered position
                        print("This spot is blocked")
                        continue # starts the loop again if spot is blocked
                    gameList[oInput-1] = "O"
                    gameBoard(gameList)
                    gameResult(gameList)
                    turn -= 1
        except Exception as e: # Handles exception and flow is not broken
            print("Enter a valid spot")       
                
#This is the main menu
print("\t\t====== TIC-TAC-TOE by TheVoidOP ======")
print("MAIN MENU")
print("\n1. Single Player")
print("2. Two Player")
gameMode = None
while gameMode != 1 and gameMode != 2: # loops till game mode isnt single or multiplayer
    try:
        gameMode = int(input("\nEnter the mode you want to play: "))
        if gameMode == 1:
            singlePlayer(gameList)
        elif gameMode == 2:
            multiPlayer(gameList)
        else:
            print("Enter a valid choice")
    except Exception as e: # handles exception and ensures continuous flow
        print("Enter a valid choice")