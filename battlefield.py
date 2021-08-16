from _typeshed import Self
from ai_player import AI_Player
from human_player import Human_player
from player import Player


class Battlefield:
    def __init__(self):
        self.player_one = Human_player(input ("Please enter your name."))
        self.player_two = AI_Player()

        self.player_one_choice = Human_player.gesture_choice 
        self.player_two_choice = ""
        self.rock = 1
        self.paper = 2
        self.scissors = 3
        self.lizard = 4
        self.spock = 5
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
        


