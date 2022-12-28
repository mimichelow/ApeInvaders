from game import Game
import time

game=Game()
game.screen.listen()
game.screen.onkey(game.player.moveleft, "Left")
game.screen.onkey(game.player.moveright, "Right")
game.screen.onkey(game.shoot, "space")

while not game.isover:
    game.movebullets()
    game.moveenemies()
    time.sleep(0.05)
    game.screen.update()

game.screen.exitonclick()

