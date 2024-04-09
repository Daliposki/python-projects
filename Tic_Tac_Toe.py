import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")

        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('Arial', 24), width=4, height=2,
                command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Winner", f"Player {winner} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != ' ':
                return row[0]

        # Check columns
        for col in range(len(self.board)):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]

        return None

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
        self.current_player = 'X'

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
