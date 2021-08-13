from human_player import Human_player


class Battlefield:
    def __init__(self):
        self.player_one = Human_player(input ("Please enter your name."))

        pass

    def run_game(self):
        print (f"Welcome {self.player_one.name}")

        pass