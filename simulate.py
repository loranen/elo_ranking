import csv
k = 30
g = 1

line_count = 0
playersDict = {}
history_list = []

def expectResult(p1, p2):
    exp = (p2-p1)/400.0
    return 1/((10.0**(exp))+1)

def gameOver(winner, loser):
    if winner == loser:
        print("Check players! Winner = Loser")
    else:
        result = expectResult(playersDict[winner], playersDict[loser])

        playersDict[winner] = playersDict[winner] + (k*g)*(1 - result)  
        playersDict[loser] 	= playersDict[loser] + (k*g)*(0 - (1 -result))

with open('history.csv') as history_file:
    csv_reader = csv.reader(history_file, delimiter=',')
    counter = 0
    for row in csv_reader:
        if counter != 0:
            time = row[0]
            winner = row[1]
            loser = row[3]

            if winner not in playersDict:
                playersDict[winner] = 1000

            if loser not in playersDict:
                playersDict[loser] = 1000

            gameOver(winner, loser)
            history_list.append([time, winner, playersDict[winner], loser, playersDict[loser]])
        counter += 1

    for rivi in history_list:
        print(rivi)

    history_file.close()

with open('simulated_history.csv', 'w', newline='') as simu_file:
    writer = csv.writer(simu_file)
    writer.writerow(["time", "winner", "winnerNewElo", "loser", "loserNewElo"])
simu_file.close()

with open('simulated_history.csv', 'a+', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for i in range(len(history_list)):
        writer.writerow(history_list[i])
csv_file.close()
