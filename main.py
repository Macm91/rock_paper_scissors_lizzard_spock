from ai_player import AI_Player

from battlefield import Battlefield

game = Battlefield() 

game.game_mode()
game.prompt_gesture()

print(game.player_one.gesture_choice)
print(game.player_two.gesture_choice)

game.validate_rock()