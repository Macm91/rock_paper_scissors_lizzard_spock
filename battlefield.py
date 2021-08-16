from _typeshed import Self
from ai_player import AI_Player
from human_player import Human_player
from player import Player


class Battlefield:
    def __init__(self):
        self.player_one = Human_player(input ("Please enter your name."))
        self.player_two = []
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
        


#calls player 1 and player 2 choices and compares them.
    def battle(self):
        while len(self.player_one.score) < 3 and len(self.player_two.score) < 3:
            self.player_1_turn
            self.player_2_turn
            self.compare_gestures
        
        self.display_winner
        pass

#Initiates the gesture choice in human_player method function. 
    def player_1_turn(self):
        self.player_one_choice 
        pass

#either initiates gesture choice in human or ai player method functions. 
    def player_2_turn(self):
        if (self.player_two == AI_Player):
            self.player_two_choice = AI_Player.gesture_choice
        else:
            self.player_two_choice = Human_player.gesture_choice
        pass



    def compare_gestures(self):
        if (self.player_one.gesture == self.rock or self.player_two.gesture == self.rock):
            self.rock_gesture
        elif (self.player_one.gesture == self.scissors or self.player_two.gesture == self.scissors):
            self.scissors_gesture
        elif (self.player_one.gesture == self.paper or self.player_two.gesture == self.paper):
            self.paper_gesture
        elif (self.player_one.gesture == self.lizard or self.player_two.gesture == self.lizard):
            self.lizard_gestures
        elif (self.player_one.gesture == self.spock or self.player_two.gesture == self.spock):
            self.spock_gestures
        pass

#gesture functions
    def rock_gesture(self):
        if (self.player_1_turn == self.rock and (self.player_2_turn == self.scissors or self.player_2_turn == self.lizard)):
            self.player_one.score += 1
        
        elif (self.player_2_turn == self.rock and (self.player_1_turn == self.scissors or self.player_1_turn == self.lizard)):
            self.player_two.score += 1

        pass

    def scissors_gesture(self):
        if (self.player_1_turn == self.scissors and (self.player_2_turn == self.paper or self.player_2_turn == self.lizard)):
            self.player_one.score += 1
            print (f"{self.player_one} wins this round")
        elif (self.player_2_turn == self.scissors and (self.player_1_turn == self.paper or self.player_1_turn == self.lizard)):
            self.player_two.score += 1
            print (f"{self.player_two} wins this round")
        pass

    def paper_gesture(self):
        if (self.player_1_turn == self.paper and (self.player_2_turn == self.rock or self.player_2_turn == self.spock)):
            self.player_one.score += 1
            print (f"{self.player_one} wins this round")
        elif (self.player_2_turn == self.paper and (self.player_2_turn == self.rock or self.player_2_turn == self.spock)):
            self.player_two.score += 1
            print (f"{self.player_two} wins this round")
        pass

    def lizard_gestures(self):
        if (self.player_1_turn == self.lizard and (self.player_2_turn == self.spock or self.player_2_turn == self.paper)):
            self.player_one.score += 1
            print (f"{self.player_one} wins this round")
        elif (self.player_2_turn == self.lizard and (self.player_2_turn == self.spock or self.player_2_turn == self.paper)):
            self.player_two.score += 1
            print (f"{self.player_two} wins this round")

    def spock_gestures(self):
        if (self.player_1_turn == self.spock and (self.player_2_turn == self.scissors or self.player_2_turn == self.rock)):
            self.player_one.score += 1
            print (f"{self.player_one} wins this round")
        elif (self.player_2_turn == self.spock and (self.player_2_turn == self.scissors or self.player_2_turn == self.rock)):
            self.player_two.score += 1
            print (f"{self.player_two} wins this round")


    def display_winner(self):
        if (self.player_one.score == 3):
            print (f"{self.player_one.name} Wins!")
        elif (self.player_two.score ==3):
            print (f"{self.player_two.name} Wins!")
        


        #rock > scissors
        #rock > lizard 

        #scissors > paper
        #scissors > lizard 

        #paper > rock
        #paper >spock

        #lizard > spock
        #lizard > paper

        #spock > scissors
        #spock > rock 
