from player import Player


class Human_player(Player):
   def __init__(self, name):
       super().__init__(name)

   def gesture(self):
        self.gesture_choice = input ("Enter a number to choose a gesture. 1)Rock 2)Paper 3)Scissors 4)Lizard 5)Spock")
