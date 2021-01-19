# this is a game of tic tac toe


def main():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    reset = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    end = False

    while not end:
        game(board)

        print()
        finished = input("Would you like to exit (Y/N)? ")
        print()
        if finished == "Yes" or finished == "YES" or finished == "y" or finished == "Y" or finished == "yes":
            end = True
        board = reset
    print()
    print("-------Program Terminated-------")


def game(board):
    printBoard(board)
    player1_move = 0
    player2_move = 0
    win = False

    while not win:
        tie = True
        x = 0
        y = 0
        move = input('Player 1, enter a coordinate in this form: "0, 1": ')
        # if len(move) != 4 or move[0] != 0 and
        x = int(move[0])
        y = int(move[3])

        while board[x][y] != 0:
            print()
            move = input('That spot is already taken. Enter another coordinate: ')
            x = int(move[0])
            y = int(move[3])
        board[x][y] = 1
        printBoard(board)
        win = winChecker(board, player1_move)

        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == 0:
                    tie = False
        if tie:
            print("===========")
            print("It's a tie.")
            print("===========")
            return

        tie = True

        if win:
            print("=======================")
            print("Player 1 is the winner!")
            print("=======================")
            return

        move = input('Player 2, enter a coordinate in this form: "0, 1": ')
        x = int(move[0])
        y = int(move[3])

        while board[x][y] != 0:
            print()
            move = input('That spot is already taken. Enter another coordinate: ')
            x = int(move[0])
            y = int(move[3])
        board[x][y] = 2
        printBoard(board)
        win = winChecker(board, player2_move)

        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == 0:
                    tie = False
        if tie:
            print("===========")
            print("It's a tie.")
            print("===========")
            return

        if win:
            print("=======================")
            print("Player 2 is the winner!")
            print("=======================")
            return


def printBoard(board):
    print()
    print("     0  1  2")
    print("   ——————————-")
    for i in range(0, len(board)):
        print(str(i) + " | " + str(board[i]))
        print("  |")
    print()
    print()


def winChecker(board, player):
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != 0:
        return True

    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != 0:
        return True

    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != 0:
        return True

    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != 0:
        return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return True

    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != 0:
        return True

    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != 0:
        return True

    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != 0:
        return True


main()
