
def printBoard():
    print(f" 0 | 1 | 2 ")
    print("---|---|---")
    print(f" 3 | 4 | 5 ")
    print("---|---|---")
    print(f" 6 | 7 | 8 ")




if __name__ == "__main__":
    xAxis = [0,0,0,0,0,0,0,0]
    yAxis = [0,0,0,0,0,0,0,0]
    turn = 1 # 1 for X and 0 for O
    print("Welcome to TicTakToe Game")
    p1 = input("Enter the name of the player 1 : you will get X : ")
    p2 = input("Enter the name of the player 2 : You will get O : ")
    while True:
        printBoard()
        if turn == 1:
            print(f"{p1}'s Chance")
        else:
            print(f"{p2}'s Chance")
        break