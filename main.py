from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

player_1_score = 0
player_2_score = 0

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision wal
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #detect collistion with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330  :
        ball.paddle_hit()

    # Detect R paddle misses
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()










screen.exitonclick()