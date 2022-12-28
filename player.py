from turtle import Turtle


class Player(Turtle):
    def __init__(self, screen):
        super().__init__()
        screen.addshape("hero1.gif")
        screen.addshape("hero2.gif")
        self.stepcount = 0
        self.shape("hero1.gif")
        self.penup()
        self.goto(0, -260)
        self.state = 1

    def moveright(self):
        if self.xcor() <= 290:
            self.goto(self.xcor()+10, self.ycor())
            self.state = self.state % 2 + 1
            self.shape(f"hero{self.state}.gif")

    def moveleft(self):
        if self.xcor() >= -290:
            self.goto(self.xcor()-10, self.ycor())
            self.state = self.state % 2 + 1
            self.shape(f"hero{self.state}.gif")
