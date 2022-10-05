from random import choice
from player import Player

class Ai(Player):
    def __init__(self, name):
        super().__init__(name)

    def pick_gesture(self):
        self.active_gestures = choice(self.gestures)
        print(f'Computer has selected {self.active_gestures}')