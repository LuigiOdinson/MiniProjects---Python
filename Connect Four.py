# CONNECT FOUR
from colorama import Fore

board = [["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""]]
rows = 6
columns = 7


def draw_board():
    print("\n")
    print("    ", end="")
    for num in range(columns):
        print(Fore.LIGHTWHITE_EX + str(num) + Fore.RESET, end="   ")
    print("\n  +___+___+___+___+___+___+___+")
    for i in range(rows):
        print(Fore.LIGHTWHITE_EX + str(i) + Fore.RESET, "|", end="")
        for k in range(columns):
            if board[i][k] == "A":
                print("", Fore.RED + "●" + Fore.RESET, "", end="|")
            elif board[i][k] == "B":
                print("", Fore.BLUE + "●" + Fore.RESET, "", end="|")
            else:
                print("", " ", "", end="|")
        print("\n  +___+___+___+___+___+___+___+")


def place(col, piece):
    # checking if the row bellow the piece is empty for it to go through
    for row in range(rows-1, 0, -1):
        if board[row][col] == "":
            board[row][col] = piece
            break


def check_winner(piece):
    # check for horizontals
    for r in range(rows):
        for c in range(columns-3):
            if (board[r][c] == piece and board[r][c+1] == piece and
                    board[r][c+2] == piece and board[r][c+3] == piece):
                print(Fore.YELLOW + f"PLAYER {piece} WON" + Fore.RESET)
                return True
    # check for verticals
    for r in range(rows-3):
        for c in range(columns):
            if (board[r][c] == piece and board[r+1][c] == piece and
                    board[r+2][c] == piece and board[r+3][c] == piece):
                print(Fore.YELLOW + f"PLAYER {piece} WON" + Fore.RESET)
                return True
    # top right to bottom left diagonal
    for i in range(rows-3):
        for k in range(3, columns):
            if (board[i][k] == piece and board[i+1][k-1] == piece and
                    board[i+2][k-2] == piece and board[i+3][k-3] == piece):
                print(Fore.YELLOW + f"PLAYER {piece} WON" + Fore.RESET)
                return True
    # top left to bottom right diagonal
    for i in range(rows-3):
        for k in range(3, columns):
            if (board[i][k] == piece and board[i+1][k+1] == piece and
                    board[i+2][k+2] == piece and board[i+3][k+3] == piece):
                print(Fore.YELLOW + f"PLAYER {piece} WON" + Fore.RESET)
                return True
    return False


turn = 1  # turn 1 is player A, turn -1 is player B
draw_board()
while True:
    if turn == 1:
        selected_col = int(input("\nPlayer A select a column: "))
        place(selected_col, "A")
        turn *= -1
    draw_board()
    winner = check_winner("A")
    if winner:
        break
    if turn == -1:
        selected_col = int(input("\nPlayer B select a column: "))
        place(selected_col, "B")
        turn *= -1
    draw_board()
    winner = check_winner("B")
    if winner:
        break
