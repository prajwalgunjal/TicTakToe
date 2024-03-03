def sum( a , b , c ):
    return a + b + c

def checkisWinner(xAxis,YAxis):
    wins = [ [ 0 , 1 , 2 ] , [ 3, 4, 5 ] , [ 6 , 7, 8 ] , [ 0 , 3 , 6 ] , [ 1 , 4 , 7 ] , [ 2 , 5 , 8 ] , [ 0 , 4 , 8 ] , [ 2, 4, 6 ] ] # all Winning Possible combination 
    for i in wins:
        if(sum(xAxis[i [ 0 ] ] , xAxis[i[ 1 ] ],xAxis[i[ 2 ] ])==3):
            print("x Win")
            return 1 
        if(sum(YAxis[i [ 0 ] ] , YAxis[i[ 1 ] ],YAxis[i[ 2 ] ])==3):
            print("y wins")
            return 0
    return -1



def printBoard(xAxis,yAxis):
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



if __name__ == "__main__":
    xAxis = [0,0,0,0,0,0,0,0,0]
    yAxis = [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for X and 0 for O
    print("Welcome to TicTakToe Game")
    p1 = input("Enter the name of the player 1 : you will get X : ")
    p2 = input("Enter the name of the player 2 : You will get O : ")
    while True:
        printBoard(xAxis,yAxis)
        if turn == 1:
            print(f"{p1}'s Chance")
            value = int(input("Enter the Position where you want to place your X "))
            xAxis[value] =1
        else:
            print(f"{p2}'s Chance")
            value = int(input("Enter the Position where you want to place your O "))
            yAxis[value] =1

        winnercheck = checkisWinner(xAxis,yAxis)
        if winnercheck != -1:
            print("match over ")
            break
        turn = 1 - turn 