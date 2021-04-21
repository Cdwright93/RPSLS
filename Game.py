from Computer import computer
from Human import human


class game:
    player_one = human()
    player_one.name = 'player 1'
    response = input("add player? y or n ")
    if response == 'y':
        player_two = human()
        player_two.name = 'player 2'
    if response == 'n':
        player_two = computer()
    print(player_one.score)

    def get_welcome(self):
        print('Welcome to rock,paper,scissors,lizard,spock')