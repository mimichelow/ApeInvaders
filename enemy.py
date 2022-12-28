from turtle import Turtle
import random


class Enemy(Turtle):
    def __init__(self, screen, x, y):
        super().__init__()
        screen.addshape("enemy1.gif")
        screen.addshape("enemy2.gif")
        screen.addshape("enemy3.gif")
        screen.addshape("enemy4.gif")
        screen.addshape("enemy5.gif")

        self.shape(f"enemy{random.randint(1, 5)}.gif")
        self.penup()
        self.goto(x, y)
        self.alive = True

    def rightend(self):
        return self.xcor() + 1

    def leftend(self):
        return self.xcor() - 1

    def lowend(self):
        return self.ycor() - 1

    def upend(self):
        return self.ycor() + 1

    def canmoveright(self):
        if self.xcor() >= 290:
            print("cant move right")
            return False
        return True

    def canmoveleft(self):
        if self.xcor() <= -290:
            print("cant move left")
            return False
        return True

    def hitsplayer(self, player):
        if player.xcor() + 10 > self.leftend() and player.xcor() - 10 < self.rightend() and player.ycor() + 10 > \
        self.lowend() and player.ycor() - 10 < self.upend():
            return True
        return False

    def moveleft(self):
        self.goto(self.xcor() - 10, self.ycor())

    def moveright(self):
        self.goto(self.xcor() + 10, self.ycor())

    def movedown(self):
        self.goto(self.xcor(), self.ycor() - 10)

    def die(self):
        self.alive = False
        self.hideturtle()
