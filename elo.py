import csv

class Elo:
    def __init__(self,k,g=1,homefield = 100):
        self.ratingDict     = {}	
        self.k              = k
        self.g              = g
        self.homefield      = homefield
        self.read_memory()

    def addPlayer(self,name,rating = 1000):
        self.ratingDict[name] = rating
        with open('saved_elos.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([name, rating])
        csv_file.close()

    def gameOver(self, winner, loser):
        """
        if winnerHome:
            result = self.expectResult(self.ratingDict[winner] + self.homefield, self.ratingDict[loser])
        """
        #else:
        result = self.expectResult(self.ratingDict[winner], self.ratingDict[loser]+self.homefield)

        self.ratingDict[winner] = self.ratingDict[winner] + (self.k*self.g)*(1 - result)  
        self.ratingDict[loser] 	= self.ratingDict[loser] + (self.k*self.g)*(0 - (1 -result))

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
                        self.ratingDict[row[0]] = row[1]
                    line_count += 1
                csv_file.close()

        except FileNotFoundError:
            print("File not found!")
            with open('saved_elos.csv', 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["player", "elo"])
            csv_file.close()


if __name__ == "__main__":
    test = Elo(k = 20)
    test.addPlayer("Vesa")
    test.addPlayer("Leevi")

    print(test.expectResult(test.ratingDict['Leevi'],test.ratingDict['Vesa']))
    test.gameOver(winner = "Leevi", loser = "Vesa")
    print(test.expectResult(test.ratingDict['Leevi'],test.ratingDict['Vesa']))