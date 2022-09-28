from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = input("what is your name?")
        
    
    
