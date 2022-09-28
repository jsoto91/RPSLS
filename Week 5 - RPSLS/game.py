from human import Human
from ai import Ai
from player import Player

class Battlefield:
    def __init__(self):
        self.player1 = Human()
        self.player2 = []
    
    def run_game(self):
        self.display_welcome()
        self.choose_ai_or_human()
        self.game_time()
        self.display_winner()
        
    def display_welcome (self):
        print("Welcome to rock, paper, scissor, lizard, Spock!")
        print("Here are the rules:")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors') 
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')

    def choose_ai_or_human(self):
        self.mulitplayer = input("Select 1 for single player mode. Select 2 for mulitplayer mode. ")
        if self.mulitplayer == '1':
            self.player2 = Ai('Computer')
        elif self.mulitplayer == '2':
            self.player2 = Human()
    
    def game_time(self):
        self.player1.


    def display_winner(self):
        if self.robot.health > 0:
            print(f"The winner is ... {self.robot.name}!")
        elif self.dinosaur > 0:
            print(f"The winner is ... {self.dinosaur.name}!")