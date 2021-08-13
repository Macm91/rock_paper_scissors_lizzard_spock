from ai_player import AI_Player
from human_player import Human_player


class Battlefield:
    def __init__(self):
        self.player_one = Human_player(input ("Please enter your name."))
        self.player_two = []
        pass

    def run_game(self):
        print (f"Welcome {self.player_one.name}")
        #Put the rules and other welcome messages here
        pass
    
    def game_mode(self):
        answer = ""
        while answer == "":
            answer = input("How many players? Please enter '1' or '2' :: ")
            if answer == "1":
                self.player_two = AI_Player()
                print("Solo Quest selected.")
            elif answer == "2":
                self.player_two = Human_player(input("Please enter Player 2's name :: "))
                print("A match among pals!")
            else:
                print("This is not a valid answer.")
                answer = ""




    def battle(self):
        pass

    def player_1_turn(self):
        # playe_one . gesture_choice 
        player_
        pass

    def player_2_turn(self):
        #player_two.gesture_choice
        pass

    def compare_gestures(self):
        

        pass
    #if else --> assign points 
