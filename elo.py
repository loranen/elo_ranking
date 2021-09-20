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
        with open('saved_elos.csv', 'a+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([name, rating])
        csv_file.close()

    def gameOver(self, winner, loser):
        if winner == loser:
            print("Check players! Winner = Loser")
        else:
            result = self.expectResult(self.playersDict[winner], self.playersDict[loser])

            self.playersDict[winner] = self.playersDict[winner] + (self.k*self.g)*(1 - result)  
            self.playersDict[loser] 	= self.playersDict[loser] + (self.k*self.g)*(0 - (1 -result))
            self.save_elos(winner, loser)

    def save_elos(self, winner, loser):
        with open('saved_elos.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["player", "elo"])
            for player in self.playersDict:
                writer.writerow([player, self.playersDict[player]])
        csv_file.close()

        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        with open('history.csv', 'a+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([timestamp, winner, round(self.playersDict[winner]), loser, round(self.playersDict[loser], 2)])
        csv_file.close()

    def expectResult(self, p1, p2):
        exp = (p2-p1)/400.0
        return 1/((10.0**(exp))+1)

    def read_memory(self):
        print("Reading data from memory file")
        try:
            with open('saved_elos.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        pass
                    else:
                        print(row)
                        self.playersDict[row[0]] = float(row[1])
                    line_count += 1
                csv_file.close()

        except FileNotFoundError:
            print("File not found!")
            with open('saved_elos.csv', 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["player", "elo"])
            csv_file.close()

        try:
            with open('history.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    print(row)

                csv_file.close()

        except FileNotFoundError:
            print("File not found!")
            with open('history.csv', 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["time", "winner", "winnerNewElo", "loser", "loserNewElo"])
            csv_file.close()


if __name__ == "__main__":
    test = Elo(k = 20)
    test.addPlayer("Vesa")
    test.addPlayer("Leevi")

    print(test.expectResult(test.playersDict['Leevi'],test.playersDict['Vesa']))
    test.gameOver(winner = "Leevi", loser = "Vesa")
    print(test.expectResult(test.playersDict['Leevi'],test.playersDict['Vesa']))