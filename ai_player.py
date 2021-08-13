from player import Player
import random

class AI_Player(Player):
    def __init__(self):
        super().__init__("Player 2")

    def gesture(self):
        self.gesture_choice = random.choice(self.gestures)