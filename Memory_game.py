import tkinter as tk
import random
from tkinter import messagebox


class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")

        self.tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
        random.shuffle(self.tiles)

        self.buttons = []
        self.flipped_tiles = []

        for i in range(4):
            for j in range(4):
                button = tk.Button(self.root, text=" ", font=('Arial', 24), width=4, height=2,
                                   command=lambda row=i, col=j: self.flip_tile(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def flip_tile(self, row, col):
        index = row * 4 + col
        if self.buttons[index]['text'] == ' ' and len(self.flipped_tiles) < 2:
            self.buttons[index]['text'] = self.tiles[index]
            self.flipped_tiles.append((row, col))

            if len(self.flipped_tiles) == 2:
                self.root.after(1000, self.check_match)

    def check_match(self):
        row1, col1 = self.flipped_tiles[0]
        row2, col2 = self.flipped_tiles[1]
        if self.tiles[row1 * 4 + col1] == self.tiles[row2 * 4 + col2]:
            self.flipped_tiles = []
            self.check_win()
        else:
            self.reset_tiles()

    def reset_tiles(self):
        row1, col1 = self.flipped_tiles[0]
        row2, col2 = self.flipped_tiles[1]
        self.buttons[row1 * 4 + col1]['text'] = ' '
        self.buttons[row2 * 4 + col2]['text'] = ' '
        self.flipped_tiles = []

    def check_win(self):
        revealed_symbols = {button['text'] for button in self.buttons if button['text'] != ' '}
        if len(revealed_symbols) == len(self.tiles) // 2:
            messagebox.showinfo("Congratulations!", "You win!")
            self.reset_game()

    def reset_game(self):
        self.flipped_tiles = []
        random.shuffle(self.tiles)
        for button in self.buttons:
            button['text'] = ' '


if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
