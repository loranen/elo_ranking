import csv
from datetime import datetime

class Elo:
    def __init__(self,k,g=1,homefield = 100):
        self.playersDict     = {}	
        self.k              = k
        self.g              = g
        self.homefield      = homefield
        self.read_memory()

    def addPlayer(self,name,rating = 1000):
        self.playersDict[name] = rating

    def gameOver(self, winner, loser):
        if winner == loser:
            print("Check players! Winner = Loser")
        else:
            result = self.expectResult(self.playersDict[winner], self.playersDict[loser])

            self.playersDict[winner] = self.playersDict[winner] + (self.k*self.g)*(1 - result)  
            self.playersDict[loser] 	= self.playersDict[loser] + (self.k*self.g)*(0 - (1 -result))
            self.save_elos(winner, loser)

    def save_elos(self, winner, loser):

        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        with open('history.csv', 'a+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([timestamp, winner, round(self.playersDict[winner],7), loser, round(self.playersDict[loser], 7)])
        csv_file.close()

    def expectResult(self, p1, p2):
        exp = (p2-p1)/400.0
        return 1/((10.0**(exp))+1)

    def read_memory(self):
        print("Reading data from memory file")

        try:
            with open('history.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        pass
                    else:
                        winner = row[1]
                        loser = row[3]
                        self.playersDict[winner] = float(row[2])
                        self.playersDict[loser] = float(row[4])
                    line_count += 1
                
                for player in self.playersDict:
                    print(player,": ", self.playersDict[player])

                csv_file.close()

        except FileNotFoundError:
            print("File not found!")
            with open('history.csv', 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["time", "winner", "winnerNewElo", "loser", "loserNewElo"])
            csv_file.close()

