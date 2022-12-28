from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, screen, x, y):
        super().__init__()
        screen.addshape("bullet1.gif")
        screen.addshape("bullet2.gif")
        screen.addshape("bullet3.gif")
        screen.addshape("bullet4.gif")
        self.penup()
        self.shape("bullet1.gif")
        self.goto(x, y)
        self.imgcount = 1

    def moveup(self):
        self.goto(self.xcor(), self.ycor()+10)
        self.imgcount = (self.imgcount % 3)+1
        self.shape(f"bullet{self.imgcount}.gif")
