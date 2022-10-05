from human import Human
from ai import Ai

class Game:
    def __init__(self):
        self.player1 = Human("Player 1")
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
        mulitplayer = input("Select 1 for single player mode. Select 2 for mulitplayer mode. ")
        if mulitplayer == '1':
            self.player2 = Ai('Computer')
            print("Single Player Mode Selected")
        elif mulitplayer == '2':
            self.player2 = Human("Player 2")
            print('Multiplayer Mode Selected')

    def game_time(self):
        winner = True
        while winner == True:

            self.player1.pick_gesture()
            self.player2.pick_gesture()
                    
            if self.player1.active_gestures == 'rock' and (self.player2.active_gestures == ):
                if self.player2.active_gestures == 'scissors':
                    self.player1.win_counter += 1
                    print('Rock crushes Scissors, player 1 wins!')
                elif self.player2.active_gestures == 'lizard':
                    self.player1.win_counter += 1
                    print('Rock crushes Lizard, player 1 wins!')
                    
                
            elif self.player2.active_gestures == 'rock':
                if self.player1.active_gestures == 'scissors':
                    self.player2.win_counter += 1
                    print('Rock crushes Scissors, player 2 wins!')
                elif self.player1.active_gestures == 'lizard':
                    self.player2.win_counter += 1
                    print('Rock crushes Lizard, player 2 wins!')
                
            elif self.player1.active_gestures == 'scissors':
                if self.player2.active_gestures == 'paper':
                    self.player1.win_counter += 1
                    print('Scissors cuts paper, player 1 wins!')
                elif self.player2.active_gestures == 'lizard':
                    self.player1.win_counter += 1
                    print('Scissors decapitates Lizard, player 1 wins!')
                
            elif self.player2.active_gestures == 'scissors':
                if self.player1.active_gestures == 'paper':
                    self.player2.win_counter += 1
                    print('Scissors cuts paper, player 2 wins!')
                elif self.player1.active_gestures == 'lizard':
                    self.player2.win_counter += 1
                    print('Scissors decapitates Lizard, player 2 wins!')

            elif self.player1.active_gestures == 'paper':
                if self.player2.active_gestures == 'rock':
                    self.player1.win_counter += 1
                    print('Paper covers Rock, player 1 wins!')
                elif self.player2.active_gestures == 'Spock':
                    self.player1.win_counter += 1
                    print('Paper disproves Spock, player 1 wins!')

            elif self.player2.active_gestures == 'paper':
                if self.player1.active_gestures == 'rock':
                    self.player2.win_counter += 1
                    print('Paper covers Rock, player 2 wins!')
                elif self.player1.active_gestures == 'Spock':
                    self.player2.win_counter += 1
                    print('Paper disproves Spock, player 2 wins!')

            elif self.player1.active_gestures == 'lizard':
                if self.player2.active_gestures == 'Spock':
                    self.player1.win_counter += 1
                    print('Lizard poisons Spock, player 1 wins!')
                elif self.player2.active_gestures == 'paper':
                    self.player1.win_counter += 1
                    print('Lizard eats Paper, player 1 wins!')

            elif self.player2.active_gestures == 'lizard':
                if self.player1.active_gestures == 'Spock':
                    self.player2.win_counter += 1
                    print('Lizard poisons Spock, player 2 wins!')
                elif self.player1.active_gestures == 'paper':
                    self.player2.win_counter += 1
                    print('Lizard eats Paper, player 2 wins!')

            elif self.player1.active_gestures == 'Spock':
                if self.player2.active_gestures == 'scissors':
                    self.player1.win_counter += 1
                    print('Spock smashes scissors, player 1 wins!')
                elif self.player2.active_gestures == 'rock':
                    self.player1.win_counter += 1
                    print('Spock vaporizers rock, player 1 wins!')

            elif self.player2.active_gestures == 'Spock':
                if self.player1.active_gestures == 'scissors':
                    self.player2.win_counter += 1
                    print('Spock smashes scissors, player 2 wins!')
                elif self.player1.active_gestures == 'rock':
                    self.player2.win_counter += 1
                    print('Spock vaporizes Rock, player 2 wins!')

            if self.player1.win_counter == 2 or self.player2.win_counter == 2:    
                winner = False


    def display_winner(self):
        if self.player1.win_counter == 2:
            print(f"The winner is ... {self.player1.name}!")
        elif self.player2.win_counter == 2:
            print(f"The winner is ... {self.player2.name}!")