class Player:
    def __init__(self,name):
        self.name = name
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
        self.active_gestures = ""
        self.win_counter = 0 

    def pick_gesture(self):
        user_decision = True
        while user_decision == True:
            user_choice = input("Select 1 for rock, 2 for paper, 3 for scissors, 4 for lizard, 5 for spock: ")
            if user_choice == "1":
                self.active_gestures = self.gestures[0]
                user_decision = False
            elif user_choice == "2":
                self.active_gestures = self.gestures[1]
                user_decision = False
            elif user_choice == "3":
                self.active_gestures = self.gestures[2]
                user_decision = False
            elif user_choice == "4":
                self.active_gestures = self.gestures[3]
                user_decision = False
            elif user_choice == "5":
                self.active_gestures = self.gestures[4]
                user_decision = False


