from elo import Elo
from tkinter import *
from tkinter import Menu
from tkinter import ttk

class EloGui:
    def __init__(self, master, league):
        self.league = league
        self.master = master
        self.master.geometry("350x200")
        self.master.title("Pingis Elo")
        self.master.attributes('-topmost', 1)

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
        if not self.league.playersDict:
            fisrt_player = input("Please enter first player's name:\n")
            self.league.addPlayer(fisrt_player)

        # datatype of menu text
        self.playerw_var = StringVar()
        self.playerl_var = StringVar()
        # Create Dropdown menu
        self.dropw = OptionMenu(self.master , self.playerw_var , *self.league.playersDict)
        self.dropl = OptionMenu(self.master , self.playerl_var , *self.league.playersDict)
        self.dropw.grid(row = 1, column = 0, sticky = W, padx=20)
        self.dropl.grid(row = 1, column = 50, sticky = W, padx=20)

        self.submit_button = Button(self.master, text="Swap", command=self.swap_players)
        self.submit_button.grid(row = 1, column = 1, sticky = W, pady = 2)

        self.submit_button = Button(self.master, text="Submit", command=self.submit_game)
        self.submit_button.grid(row = 2, column = 1, sticky = W, pady = 2)

        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.grid(row = 3, column = 1, sticky = W, pady = 2)

        self.ranking_window()

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

    def ranking_window(self):
        self.rankingWindow = Toplevel(self.master)
        self.rankingWindow.title("Rankings")
        self.rankingWindow.geometry("{0}x{1}+0+0".format(self.rankingWindow.winfo_screenwidth(), self.rankingWindow.winfo_screenheight()))
        self.rankingWindow['bg']='#fb0'

        style = ttk.Style()

        style.configure("Treeview", font=(None, 50))
        style.configure('Treeview', background="white")

        style.configure("Treeview.Heading", font=(None, 70))
        style.configure('Treeview.Heading', background="white")
        style.configure('Treeview', rowheight=80) # repace 40 with whatever you need

        tv = ttk.Treeview(self.rankingWindow)
        tv['columns']=('Pos', 'Name', 'Elo')
        tv.column('#0', width=0, stretch=NO)
        tv.column('Pos', anchor=CENTER, width=300)
        tv.column('Name', anchor=CENTER, width=300)
        tv.column('Elo', anchor=CENTER, width=300)

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('Pos', text='Pos.', anchor=CENTER)
        tv.heading('Name', text='Name', anchor=CENTER)
        tv.heading('Elo', text='Elo', anchor=CENTER)

        sorted_rankings = sorted(self.league.playersDict.items(), key = lambda kv: kv[1], reverse=True)
        counter = 1
        for player in sorted_rankings:
            tv.insert(parent='', index=counter-1, iid=counter-1, text='',\
                values=(str(counter), player[0], round(player[1])))
            counter += 1
        tv.pack()

    def add_player(self):
        new_player = self.player_entry.get()

        if new_player in self.league.playersDict:
            print("Player already exists")
        else:
            self.league.addPlayer(new_player)
            menuw = self.dropw["menu"]
            menuw.delete(0, "end")
            for string in self.league.playersDict:
                menuw.add_command(label=string, 
                                command=lambda value=string: self.playerw_var.set(value))
            
            menul = self.dropl["menu"]
            menul.delete(0, "end")
            for string in self.league.playersDict:
                menul.add_command(label=string, 
                                command=lambda value=string: self.playerl_var.set(value))

        self.newPlayerWindow.destroy()

    def submit_game(self):
        win = self.playerw_var.get()
        los = self.playerl_var.get()
        self.league.gameOver(winner = win, loser = los)
        self.rankingWindow.destroy()
        self.ranking_window()
        print(self.league.playersDict)

    def swap_players(self):
        win = self.playerw_var.get()
        los = self.playerl_var.get()
        self.playerw_var.set(los)
        self.playerl_var.set(win)



