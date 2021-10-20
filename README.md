# Elo Ranking 

Elo ranking system with GUI

## Description

This project was made for tracing the progress of the players in ping pong. However, it can be used on almost any 1vs1 game.

## Getting Started

### Dependencies

* Python 3
* Install Tkinter: sudo apt-get install python3-tk (Linux Command)

### Executing program

* Run the program command
```
python main.py
```
* On first start:
    * Program will create to files:
 saved_elos.csv and history.csv. These files will save the results if the program is closed. When the program is started again these files are read automatically.
    * The user is asked to add the first player on commad line. Write the name an press ENTER

* Add players by clicking File -> New Player
* Submit game
    * Select the winner from the left side Dropdown menu
    * Select the loser from the right side Dropdown menu
    * Click submit
    * New elos are updated to ranking window and saved_elos.csv file. More information about the game is saved in the history.csv file.

## Troubleshooting

* Check Python version
```
$ python --version
Python 3.8.10
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

The elo class is modified from [here](https://github.com/ddm7018/Elo/tree/master/elosports).
