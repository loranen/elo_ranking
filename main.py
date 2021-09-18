from elo import Elo
from tkinter import *
from tkinter import Menu
from elo_gui import EloGui


if __name__ == "__main__":
    league = Elo(k = 20)
    root = Tk()
    my_gui = EloGui(root, league)
    root.mainloop()