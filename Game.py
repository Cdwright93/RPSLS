from Computer import computer
from Human import human
from Player import player


class game:
    player_one = human()
    player_one.name = 'player 1'
    response = raw_input("add player? y or n ")
    if response == 'y\r':
        player_two = human()
        player_two.name = 'player 2'
    if response == 'n\r':
        player_two = computer()
