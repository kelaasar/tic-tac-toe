# this is a game of tic tac toe


def main():
    board = [[0, 0, 0],
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
        board = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

    print()
    print("-------Program Terminated-------")


def game(board):
    printBoard(board)
    win = False

    while not win:
        tie = True
        x = 0
        y = 0

        move = input('Player 1, enter a coordinate in this form: "0, 1": ')
        move = move.strip()

        try:
            x = int(move[0])
            y = int(move[3])
        except:
            print()
            move = input('Invalid input. Enter the coordinates in the following format: "0, 1": ')

        move = errorChecker(move, board, x, y)

        x = int(move[0])
        y = int(move[3])

        board[x][y] = 1
        printBoard(board)
        win = winChecker(board)

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

        x = 0
        y = 0
        move = input('Player 2, enter a coordinate in this form: "0, 1": ')
        move = move.strip()

        try:
            x = int(move[0])
            y = int(move[3])
        except:
            print()
            move = input('Invalid input. Enter the coordinates in the following format: "0, 1": ')

        move = errorChecker(move, board, x, y)

        x = int(move[0])
        y = int(move[3])

        board[x][y] = 2
        printBoard(board)
        win = winChecker(board)

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


def errorChecker(move, board, x, y):
    while not len(move) == 4 or move[0] not in ["0", "1", "2"] or not move[1] == "," or not move[2] == " " or \
            move[3] not in ["0", "1", "2"] or move == "" or board[x][y] != 0:
        print()
        move = input('Invalid input. Enter the coordinates in the following format: "0, 1": ')
        try:
            x = int(move[0])
            y = int(move[3])
        except:
            move = input('Invalid input. Enter the coordinates in the following format: "0, 1": ')

    return move


def winChecker(board):
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
