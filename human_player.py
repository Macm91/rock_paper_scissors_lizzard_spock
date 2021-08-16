from random import choice
from player import Player


class Human_player(Player):
   def __init__(self, name):
       super().__init__(name)

   def gesture(self):
        choice = input ("Enter a number to choose a gesture. 1)Rock 2)Paper 3)Scissors 4)Lizard 5)Spock.")
        self.gesture_choice = int(choice)
