class player:
    def __init__(self):
        self.gesture_list = ''
        self.name = ''
        self.chosen_gesture = ''
        self.score = 0
        self.type = ''

    def set_name(self):
        if self.name == "Computer":
            return
        if self.name == '':
            self.name = raw_input("Please type your name.")