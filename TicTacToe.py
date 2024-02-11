# implementing a tic tac toe game using tkinter
 
import tkinter as tk
from tkinter import messagebox
import numpy as np

class TicTacToe:
    def __init__(self):
        #   MAKING THE WINDOW
        self.window = tk.Tk()
        self.window.geometry("600x600")
        self.window.title("Tic Tac Toe")
        self.turn = 1

        #   MAKING THE GAME BOARD
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.window, text=" ", font=("Arial", 20))
                btn.grid(row=row, column=col, sticky="nsew")
                btn.config(command=lambda b=btn, r=row, c=col: self.button_pressed(b, r, c))
        for i in range(3):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

        #   NUMPY BOARD
        self.np_board = np.zeros((3, 3))

        self.window.mainloop()

    def button_pressed(self, button, row, col):
        self.change_turn(button, row, col)
        self.check_win()

    def change_turn(self, button, row, col):
        if button["text"] == " ":
            if self.turn == 1:
                button["text"] = "X"
                self.np_board[row][col] = 1
            else:
                button["text"] = "O"
                self.np_board[row][col] = -1
            self.turn = -self.turn
        else:
            messagebox.showinfo(title="!", message="spot already taken")
    

    def check_win(self):
        # Check rows, columns, and diagonals
        if np.any(np.sum(self.np_board, axis=1) ==  3) or \
           np.any(np.sum(self.np_board, axis=0) ==  3) or \
           np.sum(np.diagonal(self.np_board))==  3 or \
           np.sum(np.diagonal(np.fliplr(self.np_board)))==  3:
            messagebox.showinfo(title="GAME ENDED", message="Player X won")
            return True
        elif np.any(np.sum(self.np_board, axis=1) == -3) or \
             np.any(np.sum(self.np_board, axis=0) == -3) or \
             np.sum(np.diagonal(self.np_board))== -3 or \
             np.sum(np.diagonal(np.fliplr(self.np_board)))== -3:
            messagebox.showinfo(title="GAME ENDED", message="Player O won")
            return True
        # Check for a draw
        elif np.count_nonzero(self.np_board) ==  9:
            messagebox.showinfo(title="GAME ENDED", message="It's a draw")
            return True
        return False

if __name__ == "__main__":
    TicTacToe()
