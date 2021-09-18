from elo import Elo
from tkinter import *
from tkinter import Menu

class EloGui:
    def __init__(self, master, league):
        self.league = league
        self.master = master
        self.master.geometry("400x400")

        self.master.title("Pingis Elo")

        self.label = Label(self.master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(self.master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.pack()
        
        self.menu = Menu(self.master)
        self.menubar = Menu(self.menu, tearoff=0)
        self.menubar.add_command(label='New Player', command=self.new_player_window)
        #self.menubar.add_separator()
        #self.menubar.add_command(label='Edit')
        self.menu.add_cascade(label='File', menu=self.menubar)
        self.master.config(menu=self.menu)

    def new_player_window(self):
        self.newPlayerWindow = Toplevel(self.master)
        self.newPlayerWindow.title("Add New Player")
        self.newPlayerWindow.geometry("200x200")
        Label(self.newPlayerWindow, text ="Add New Player").pack()

        self.player_entry = Entry(self.newPlayerWindow,width=100)
        self.player_entry.focus()
        self.add_player_btn = Button(self.newPlayerWindow, text="Add", command=self.add_player)

        self.player_entry.pack()
        self.add_player_btn.pack()

    def add_player(self):
        self.league.addPlayer(self.player_entry.get())
        self.newPlayerWindow.destroy()

    def greet(self):
        print("moi")
