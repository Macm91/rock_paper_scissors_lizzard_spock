from ai_player import AI_Player
from human_player import Human_player
from player import Player


class Battlefield:
    def __init__(self):
        self.player_one = Human_player(input ("Please enter your name."))
        self.player_two = AI_Player()
        pass

    def run_game(self):
        print (f"Welcome {self.player_one.name}")
    #print rules

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
        while self.player_one.score < 3 and self.player_two.score < 3:
            self.player_1_turn()
            self.player_2_turn()
            self.compare_gestures()
            pass
        self.display_winner()
    

#Initiates the gesture choice in human_player method function. 
    def player_1_turn(self):
       self.player_one.gesture()
        

#either initiates gesture choice in human or ai player method functions. 
    def player_2_turn(self):
        self.player_two.gesture()



    def compare_gestures(self):
        if self.player_one.gesture_choice == 1:
            self.rock_gesture()
        elif self.player_one.gesture_choice == 3:
            self.scissors_gesture()
        elif self.player_one.gesture_choice == 2:
            self.paper_gesture()
        elif self.player_one.gesture_choice == 4:
            self.lizard_gestures()
        else:
            self.spock_gestures()
        pass

#gesture functions
    def rock_gesture(self):
        if (self.player_two.gesture_choice == 3 or self.player_two.gesture_choice == 4): #What player two needs to lose
            self.player_one.score += 1
            print(f'{self.player_one.name} has won!')
        elif (self.player_two.gesture_choice == 2 or self.player_two.gesture_choice == 5): #what player 2 needs to win
            self.player_two.score += 1
        
        else:
            print ("It's a tie!")
        pass

    def scissors_gesture(self):
        if (self.player_two.gesture_choice == 2 or self.player_two.gesture_choice == 4):
            self.player_one.score += 1
            print (f"{self.player_one} wins this round.")
        elif (self.player_two.gesture_choice == 1 or self.player_two.gesture_choice == 5):
            self.player_two.score += 1
        else:
            print("It's a tie.")
        pass

    def paper_gesture(self):
        if (self.player_two.gesture_choice == 1 or self.player_two.gesture_choice == 5):
            self.player_one.score += 1
            print (f"{self.player_one} wins this round.")
        elif (self.player_two.gesture_choice == 3 or self.player_two.gesture_choice == 4):
            self.player_two.score += 1
            print (f'{self.player_two} wins this round.')
        else:
            print("It's a tie")
        pass

    def lizard_gestures(self):
        if (self.player_two.gesture_choice== 2 or self.player_two.gesture_choice == 5):
            self.player_one.score += 1
            print (f"{self.player_one} wins this round.")
        elif (self.player_two.gesture_choice == 3 or self.player_two.gesture_choice == 1):
            self.player_two.score += 1
            print (f'{self.player_two} wins this round.')
        else:
            print("It's a tie")
        pass

    def spock_gestures(self):
        if (self.player_two.gesture_choice == 1 or self.player_two.gesture_choice == 3):
            self.player_one.score += 1
            print (f"{self.player_one} wins this round.")

        elif (self.player_two.gesture_choice == 2 or self.player_two.gesture_choice == 4):
            self.player_two.score += 1
            print (f'{self.player_two} wins this round.')
        else:
            print("It's a tie")
        pass

##gesture functions end 

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
