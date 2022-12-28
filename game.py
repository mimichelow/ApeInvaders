from enemy import Enemy
from turtle import Screen
from player import Player
from bullet import Bullet


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.bgpic("bg.gif")
        self.screen.tracer(0)
        self.screen.listen()

        self.enemies = []
        for x in range(-260, 260, 40):
            for y in range(0, 280, 40):
                self.enemies.append(Enemy(self.screen, x, y))

        self.player = Player(self.screen)
        self.screen.update()
        self.direction = "right"
        self.screen.onkey(self.player.moveleft, "Left")
        self.screen.onkey(self.player.moveright, "Right")
        self.screen.onkey(self.shoot, "space")
        self.bulletstack = []
        self.isover = False

    def movebullets(self):
        for x in self.bulletstack:
            x.moveup()
            if x.ycor() >= 300:
                self.bulletstack.remove(x)
                x.hideturtle()
            for y in self.enemies:
                if y.hitsplayer(x) and y.alive:
                    x.hideturtle()
                    self.bulletstack.remove(x)
                    y.die()

    def shoot(self):
        self.bulletstack.append(Bullet(self.screen, self.player.xcor(), self.player.ycor() + 20))
        self.screen.update()

    def moveenemies(self):
        hit = False
        if self.direction == "left" and self.minleft() < -290:
            for x in self.enemies:
                x.movedown()
            self.direction = "right"

        elif self.direction == "right" and self.maxright() > 290:
            for x in self.enemies:
                x.movedown()
            self.direction = "left"

        else:
            for x in self.enemies:
                if self.direction == "right":
                    x.moveright()
                else:
                    x.moveleft()
        # Check if player is hit or no more enemies remain
        for x in self.enemies:
            if x.hitsplayer(self.player):
                hit = True
                break

        if not self.enemiesalive() or hit:
            self.isover = True

    def enemiesalive(self):
        for x in self.enemies:
            if x.alive:
                return True
        return False

    def minleft(self):
        tempmin = 300
        for x in self.enemies:
            if x.alive and x.xcor() < tempmin:
                tempmin = x.xcor()
        return int(tempmin)

    def maxright(self):
        tempmax = -300
        for x in self.enemies:
            if x.alive and x.xcor() > tempmax:
                tempmax = x.xcor()
        return int(tempmax)
