import tkinter as tk
from tkinter import \
    messagebox  # we have to import the message box as it is not aytomatically imported when we # imported tkinter.
import random
import time
import string


class MemoryGame:
    def __init__(self, main):
        self.main = main  # creating a 2 d list
        self.buttons = [[tk.Button(root,
                                   width=4,  # setting the with of the buttons
                                   height=2,  # setting the height of the buttons
                                   bg='lightblue',
                                   bd=5,
                                   command=lambda row=row, column=column: self.tile_choice(row, column)
                                   ) for column in range(4)] for row in range(
            4)]  # nested list for each row, with 4 columns in each row, also used lambda to create an anonymous in line function
        for row in range(4):  # Placing the rows and columns in a grid
            for column in range(4):
                self.buttons[row][column].grid(row=row, column=column)
        self.first = None
        self.create_board()

    def create_board(self):
        self.key = ()
        while len(self.key) < 16:
            n = 8
            string_val = "".join(set(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(n)))
            self.key = list(string_val * 2)
        else:
            random.shuffle(self.key)
            self.key = [self.key[:4],
                        self.key[4:8],
                        self.key[8:12],
                        self.key[12:]]

        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL, bg='lightblue', font=('webdings', 48, 'bold'))
        self.starting_time = time.monotonic()  # adding start timer

    def tile_choice(self, row, column):
        self.buttons[row][column].config(bg='lightgreen', text=self.key[row][column], font=('webdings', 48,
                                                                                            'bold'))  # enabling to show the the key in the button when pressed
        self.buttons[row][column].config(state=tk.DISABLED)  # disable the buttons
        if not self.first:
            self.first = (row, column)  # setting the first tiles

        else:
            a, b = self.first
            if self.key[row][column] == self.key[a][
                b]:  # if entry in self.key row and column matches the key in self.first row(a) and column(b) .
                self.key[row][column] = ''  # resetting the tile (removing the key in the tile to blank(string))
                self.key[a][b] = ''  # resetting the tile (removing the key in the tile to blank(string))
                if not any(''.join(row) for row in self.key):  # if all keys are blank(string's), the game is over
                    total_time = time.monotonic() - self.starting_time  # substracting the starting time from the time now to show how much time spent.
                    messagebox.showinfo(title='Finished!',
                                        message='You did it, congrats!, Your time was: {:.1f}\'s'  # showing the time in seconds within the message :)
                                        .format(total_time))  # shows this message box when the above statement is true.
                    self.main.after(1000, self.create_board())  # creates a new board after 5 seconds.
            else:
                self.main.after(2000, self.reset_tiles, row, column, a,
                                b)  # after method places a call in the scheduler , and says after stated time run this. not recursive, each call is seperate.
            self.first = None

    def reset_tiles(self, x1, y1, x2,
                    y2):  # Resetting the tiles after the user has chosen two tiles that did not match.
        self.buttons[x1][y1].config(text='', bg='lightblue', state=tk.NORMAL)
        self.buttons[x2][y2].config(text='', bg='lightblue', state=tk.NORMAL)


root = tk.Tk()
Memory_game = MemoryGame(root)
root.wm_title("Memory Game by Hassan Waince")
root.mainloop()
