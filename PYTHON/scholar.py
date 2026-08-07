boarde = ['☐', '☐', '☐', '☐', '☐', '☐', '☐', '☐', '☐']
winning_lines = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

def print_board(board):
    print("---BOARD---")
    print("--", board[0], board[1], board[2], "--")
    print("--", board[3], board[4], board[5], "--")
    print("--", board[6], board[7], board[8], "--")
    print("-----------")

def check_winner(b):
    returna = False
    for line in winning_lines:
        if all(b[i] == "X" for i in line):
            print("X wins!")
            returna = True
        elif all(b[i] == "y" for i in line):
            print("Y wins!")
            returna = True
    return returna


def make_move(boardf, current_player):
    while True:
        if current_player == "X":
            gridask = int(input("X goes, (1-9 l-r, t-b): "))
            gridask -= 1
            if boardf[gridask] == "☐":
                boardf[gridask] = "X"
                break
            else:
                print("Already something there.")
        elif current_player == "O":
            gridask = int(input("O goes, (1-9 l-r, t-b): "))
            gridask -= 1
            if boardf[gridask] == "☐":
                boardf[gridask] = "O"
                break
            else:
                print("Already something there.")
def main():
    current_playe = 'X'
    print("Welcome to tic tac toe game.")
    while True:
        if check_winner(boarde):
            break
        print_board(boarde)
        make_move(boarde, current_playe)
        if current_playe == "X":
            current_playe = "O"
        elif current_playe == "O":
            current_playe = "X"


main()