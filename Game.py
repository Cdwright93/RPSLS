import random
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
        player_two.name = 'computer'

    def __init__(self):
        pass

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock')

    def battle(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            pass

    def display_winner(self):
        if self.player_one.score == 3:
            print("player 1 wins!")
        else:
            print("player 2 wins!")

    def player_one_turn(self):
        response = input("1: " + self.player_one.gestures[0] + "2: " + self.player_one.gestures[1] + '3: ' +
                         self.player_one.gestures[2] + '4: ' + self.player_one.gestures[3] + '5: ' +
                         self.player_two.gestures[4])
        if response == "1":
            self.player_one.chosen_gesture = 0
        if response == "2":
            self.player_one.chosen_gesture = 1
        if response == "3":
            self.player_one.chosen_gesture = 2
        if response == '4':
            self.player_one.chosen_gesture = 3
        if response == '5':
            self.player_one.chosen_gesture = 4

    def player_two_turn(self):
        if self.player_two.name == 'player 2':
            response = input("1: " + self.player_two.gestures[0] + "2: " + self.player_two.gestures[1] + '3: ' +
                             self.player_two.gestures[2] + '4: ' + self.player_two.gestures[3] + '5: ' +
                             self.player_two.gestures[4])
            if response == "1":
                self.player_two.chosen_gesture = 0
            if response == "2":
                self.player_two.chosen_gesture = 1
            if response == "3":
                self.player_two.chosen_gesture = 2
            if response == '4':
                self.player_two.chosen_gesture = 3
            if response == '5':
                self.player_two.chosen_gesture = 4
        if self.player_two.name == 'computer':
            self.player_two.chosen_gesture = random.randint(0, 4)

    def gesture_compare(self):
        if self.player_one.chosen_gesture == 0:
            