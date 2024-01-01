from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor((0,0,0))
screen.title("PONG")
screen.tracer(0)

p1 = Paddle()
p2 = Paddle()
ball = Ball()
p1.goto(350, 0)
p2.goto(-350, 0)
screen.listen()
scoreboard = Scoreboard()

screen.onkeypress(p1.move_up, "Up")
screen.onkeypress(p1.move_down, "Down")
screen.onkeypress(p2.move_up, "w")
screen.onkeypress(p2.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(p1) < 50 and ball.xcor() > 320 or ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed(+1)

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()











screen.exitonclick()