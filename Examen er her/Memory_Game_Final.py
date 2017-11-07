import tkinter as tk
from tkinter import messagebox
import random
import time
import string
#Examen innlevering Hassan Waince Memory Game

class MemoryGame:
    def __init__(self, main):
        self.main = main
        self.buttons = [[tk.Button(root,
                                   width=4,
                                   height=2,
                                   bg='lightblue',
                                   bd=15,
                                   command=lambda row=row, column=column: self.tile_choice(row, column)
                                   ) for column in range(4)] for row in range(4)]
        for row in range(4):
            for column in range(4):
                self.buttons[row][column].grid(row=row, column=column)
        self.first = None
        self.create_board()

    def create_board(self):
        self.key = ()
        while len(self.key) < 16:
            n = 8
            key_gen = "".join(set(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(n)))
            self.key = list(key_gen * 2)
        else:
            random.shuffle(self.key)
            self.key = [self.key[:4],
                        self.key[4:8],
                        self.key[8:12],
                        self.key[12:]]

        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL, bg='purple', font=('webdings', 48, 'bold'))
        self.starting_time = time.monotonic()

    def tile_choice(self, row, column):
        self.buttons[row][column].config(bg='aqua', text=self.key[row][column], font=('webdings', 48,
                                                                                            'bold'))
        self.buttons[row][column].config(state=tk.DISABLED)
        if not self.first:
            self.first = (row, column)

        else:
            a, b = self.first
            if self.key[row][column] == self.key[a][b]:
                self.key[row][column] = ''
                self.key[a][b] = ''
                self.buttons[row][column].config(bg='yellow')
                self.buttons[a][b].config(bg='yellow')
                if not any(''.join(row) for row in self.key):
                    total_time = time.monotonic() - self.starting_time
                    messagebox.showinfo(title='Finished!', message='You did it, congrats!, Your time was: {:.1f}\'s'
                                                                   '\nClick OK to go again, with a new board!'
                                        .format(total_time))
                    self.main.after(1000, self.create_board())
            else:
                self.main.after(2000, self.reset_tiles, row, column, a, b)
            self.first = None

    def reset_tiles(self, x1, y1, x2, y2):
        self.buttons[x1][y1].config(text='', bg='purple', state=tk.NORMAL)
        self.buttons[x2][y2].config(text='', bg='purple', state=tk.NORMAL)


root = tk.Tk()
Memory_game = MemoryGame(root)
root.wm_title("Memory Game by Hassan Waince")
root.mainloop()
