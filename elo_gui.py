from elo import Elo
from tkinter import *
from tkinter import Menu

class EloGui:
    def __init__(self, master, league):
        self.league = league
        self.master = master
        self.master.geometry("350x200")

        self.master.title("Pingis Elo")

        self.selectw = Label(self.master, text="Select winner")
        self.selectw.grid(row = 0, column = 0, sticky = W, pady = 10, padx=20)

        self.selectl = Label(self.master, text="Select loser")
        self.selectl.grid(row = 0, column = 50, sticky = W, pady = 10, padx=20)
        
        self.menu = Menu(self.master)
        self.menubar = Menu(self.menu, tearoff=0)
        self.menubar.add_command(label='New Player', command=self.new_player_window)
        #self.menubar.add_separator()
        #self.menubar.add_command(label='Edit')
        self.menu.add_cascade(label='File', menu=self.menubar)
        self.master.config(menu=self.menu)

        # datatype of menu text
        self.playerw_var = StringVar()
        self.playerl_var = StringVar()
        # Create Dropdown menu
        self.dropw = OptionMenu(self.master , self.playerw_var , *self.league.playersDict)
        self.dropl = OptionMenu(self.master , self.playerl_var , *self.league.playersDict)
        self.dropw.grid(row = 1, column = 0, sticky = W, padx=20)
        self.dropl.grid(row = 1, column = 50, sticky = W, padx=20)

        self.submit_button = Button(self.master, text="Submit", command=self.submit_game)
        self.submit_button.grid(row = 2, column = 1, sticky = W, pady = 2)

        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.grid(row = 3, column = 1, sticky = W, pady = 2)

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
        menu = self.dropw["menu"]
        menu.delete(0, "end")
        for string in self.league.playersDict:
            menu.add_command(label=string, 
                             command=lambda value=string: self.playerw_var.set(value))


    def submit_game(self):
        print(self.league.playersDict)
        win = self.playerw_var.get()
        los = self.playerl_var.get()
        self.league.gameOver(winner = win, loser = los)
