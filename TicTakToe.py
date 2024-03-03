def sum( a , b , c ):
    return a + b + c

def checkisWinner(xAxis,YAxis,p1,p2):
    try:
        wins = [ [ 0 , 1 , 2 ] , [ 3, 4, 5 ] , [ 6 , 7, 8 ] , [ 0 , 3 , 6 ] , [ 1 , 4 , 7 ] , [ 2 , 5 , 8 ] , [ 0 , 4 , 8 ] , [ 2, 4, 6 ] ] # all Winning Possible combination 
        for i in wins:
            if(sum(xAxis[i [ 0 ] ] , xAxis[i[ 1 ] ],xAxis[i[ 2 ] ])==3):
                print(f"congratulations")
                print(f"{p1} is the winner ")
                return 1 
            if(sum(YAxis[i [ 0 ] ] , YAxis[i[ 1 ] ],YAxis[i[ 2 ] ])==3):
                print(f"congratulations")
                print(f"{p2} is the Winner ")
                return 0
        return -1
    except Exception as e:
        print(f"Exception while checking Winner : - {e}")

def printBoard(xAxis,yAxis):
    try:
        Zero = 'X' if xAxis[0] else ('O' if yAxis[0] else 0)
        One = 'X' if xAxis[1] else ('O' if yAxis[1] else 1)
        Two = 'X' if xAxis[2] else ('O' if yAxis[2] else 2)
        Three = 'X' if xAxis[3] else ('O' if yAxis[3] else 3)
        Four = 'X' if xAxis[4] else ('O' if yAxis[4] else 4)
        Five = 'X' if xAxis[5] else ('O' if yAxis[5] else 5)
        Six = 'X' if xAxis[6] else ('O' if yAxis[6] else 6)
        Seven = 'X' if xAxis[7] else ('O' if yAxis[7] else 7)
        Eight = 'X' if xAxis[8] else ('O' if yAxis[8] else 8)
        print(f" {Zero} | {One} | {Two} ")
        print("---|---|---")
        print(f" {Three} | {Four} | {Five} ")
        print("---|---|---")
        print(f" {Six} | {Seven} | {Eight} ")
    except Exception as e:
        print(f"Exception While printing board : - {e}")

if __name__ == "__main__":
    try:
        xAxis = [0,0,0,0,0,0,0,0,0]
        yAxis = [0,0,0,0,0,0,0,0,0]
        turn = 1 # 1 for X and 0 for O
        restart = False
        print("Welcome to TicTakToe Game")
        p1 = input("Enter the name of the player 1 : you will get X : ")
        p2 = input("Enter the name of the player 2 : You will get O : ")
        while True:
            if restart == True:
                turn =1
            restart = False
            printBoard(xAxis,yAxis)
            if turn == 1:
                print(f"{p1}'s Chance")
                try:
                    value = int(input("Enter the Position where you want to place your X "))
                    if value >= 0 or value <= 8:
                        xAxis[value] =1
                        
                    else:
                        print("Invalid move. Try again.")
                        continue
                except Exception as e:
                    print("Invalid Value please Enter Correct Number")
                    continue
            else:
                print(f"{p2}'s Chance")
                try:
                    value = int(input("Enter the Position where you want to place your O "))
                    if value >= 0 or value <= 8:
                        yAxis[value] =1
                        
                    else:
                        print("Invalid move. Try again.")
                        continue
                except Exception as e:
                    print("Invalid Value please Enter Correct Number")
                    continue

            winnercheck = checkisWinner(xAxis,yAxis,p1,p2)
            if winnercheck != -1:
                print("match over ")
                playagain = input("Press y if you want to play again ")
                if playagain.lower() == "y":
                    xAxis = [0,0,0,0,0,0,0,0,0]
                    yAxis = [0,0,0,0,0,0,0,0,0]
                    restart = True
                    continue
                else:
                    print("Thanks for playing! Goodbye.")
                    break
            turn = 1 - turn 

    except Exception as e:
        print(f"Excpetion in main {e}")