POSITIONS = [(-350,-40),(-350,-20),(-350,0), (-350,20)]
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = Turtle('square')
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(350,0)

    def move_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def move_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

