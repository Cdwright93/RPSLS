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
            self.player_one_turn()
            self.player_two_turn()
            self.gesture_compare()

    def display_winner(self):
        if self.player_one.score == 3:
            print("player 1 wins!")
        else:
            print("player 2 wins!")

    def player_one_turn(self):
        response = input(" 1: " + self.player_one.gestures[0] + " 2: " + self.player_one.gestures[1] + '3: ' +
                         self.player_one.gestures[2] + ' 4: ' + self.player_one.gestures[3] + '5: ' +
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
            response = input("1: " + self.player_two.gestures[0] + "2: " + self.player_two.gestures[1] + ' 3: ' +
                             self.player_two.gestures[2] + ' 4: ' + self.player_two.gestures[3] + ' 5: ' +
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

    # rock = 0, paper = 1, scissors = 2, lizard = 3, spock = 4

    def gesture_compare(self):
        if self.player_one.chosen_gesture == 0:
            if self.player_two.chosen_gesture == 2:
                self.player_one.score = self.player_one.score + 1
                print("rock crushes scissors!")
            if self.player_two.chosen_gesture == 3:
                self.player_one.score = self.player_one.score + 1
                print("rock crushes lizard!")
            if self.player_two.chosen_gesture == 1:
                self.player_two.score = self.player_two.score + 1
                print("paper covers rock!")
            if self.player_two.chosen_gesture == 4:
                self.player_two.score = self.player_two.score + 1
                print("Spock vaporizes rock!")
            if self.player_two.chosen_gesture == 0:
                print("its a tie")
        if self.player_one.chosen_gesture == 1:
            if self.player_two.chosen_gesture == 0:
                self.player_one.score = self.player_one.score + 1
                print("paper covers rock!")
            if self.player_two.chosen_gesture == 4:
                self.player_one.score = self.player_one.score + 1
                print("paper disproves Spock!")
            if self.player_two.chosen_gesture == 2:
                self.player_two.score = self.player_two.score + 1
                print("scissors cuts paper!")
            if self.player_two.chosen_gesture == 3:
                self.player_two.score = self.player_two.score + 1
                print("lizard eats paper!")
            if self.player_two.chosen_gesture == 1:
                print("its a tie")
        if self.player_one.chosen_gesture == 2:
            if self.player_two.chosen_gesture == 1:
                self.player_one.score = self.player_one.score + 1
                print("scissors cuts paper!")
            if self.player_two.chosen_gesture == 3:
                self.player_one.score = self.player_one.score + 1
                print("scissors decapitates lizard!")
            if self.player_two.chosen_gesture == 0:
                self.player_two.score = self.player_two.score + 1
                print("rock crushes scissors!")
            if self.player_two.chosen_gesture == 4:
                self.player_two.score = self.player_two.score + 1
                print("Spock smashes scissors!")
            if self.player_two.chosen_gesture == 2:
                print("its a tie")
        if self.player_one.chosen_gesture == 3:
            if self.player_two.chosen_gesture == 1:
                self.player_one.score = self.player_one.score + 1
                print("lizard eats paper!")
            if self.player_two.chosen_gesture == 4:
                self.player_one.score = self.player_one.score + 1
                print("lizard poisons Spock!")
            if self.player_two.chosen_gesture == 0:
                self.player_two.score = self.player_two.score + 1
                print("rock crushes lizard!")
            if self.player_two.chosen_gesture == 2:
                self.player_two.score = self.player_two.score + 1
                print("scissors decapitates lizard!")
            if self.player_two.chosen_gesture == 3:
                print("its a tie")
        if self.player_one.chosen_gesture == 4:
            if self.player_two.chosen_gesture == 0:
                self.player_one.score = self.player_one.score + 1
                print("Spock vaporizes rock!")
            if self.player_two.chosen_gesture == 2:
                self.player_one.score = self.player_one.score + 1
                print("Spock smashes scissors!")
            if self.player_two.chosen_gesture == 3:
                self.player_two.score = self.player_two.score + 1
                print("lizard poison Spock!")
            if self.player_two.chosen_gesture == 1:
                self.player_two.score = self.player_two.score + 1
                print("paper disproves Spock!")
            if self.player_two.chosen_gesture == 4:
                print("its a tie")