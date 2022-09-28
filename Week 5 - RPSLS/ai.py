from random import choice
from player import Player

class Ai(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.active_gesture = choice(self.pick_gesture)
