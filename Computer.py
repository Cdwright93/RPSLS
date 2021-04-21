from Player import player


class computer(player):
    def __init__(self):
        self.name = 'computer'
        self.score = 0
        self.chosen_gesture = ''