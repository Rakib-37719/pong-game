from turtle import Turtle, Screen
from paddle import Paddle
import time

SCREENWIDTH = 800
SCREENHEIGHT = 600

screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
screen.tracer(0)

left = Paddle()

screen.listen()
time.sleep(0.1)

if left.ycor() < 300 and left.ycor() > -300:
    screen.onkeypress(left.move_up, 'Up')
    print(left.ycor())
    screen.onkeypress(left.move_down, 'Down')


screen.exitonclick()
