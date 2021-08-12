from player import Player


class Human_player(Player):
   super().__init__()

    def create_player(self):
        self.name = input ("Enter players name.")

    def gesture(self):
        self.gesture_choice = input ("Enter a number to choose a gesture. 1)Rock 2)Paper 3)Scissors 4)Lizard 5)Spock")
        
