import turtle
import paddle
import time
import ball
import player

#Screen setup
screen = turtle.Screen()
screen.setup(width=750, height=500)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Show score
score = player.Player()

#Create paddles
left_paddle = paddle.Paddle(-340)
right_paddle = paddle.Paddle(340)

#Create a ball
ball = ball.Ball()

#Move paddles
screen.listen()
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")
screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")

#Start game
game_is_on = True
# score = 1

while game_is_on:
    time.sleep(0.01)
    screen.update()

    ball.move_forward()
    ball.check_wall()

    #Detect collision with right paddle
    if ball.xcor() > right_paddle.xcor() - 8:
        if ball.ycor() < right_paddle.ycor() + 55 and ball.ycor() > right_paddle.ycor() - 55:
            ball.bounce_x()

    #Detect collision with left paddle
    if ball.xcor() < left_paddle.xcor() + 8:
        if ball.ycor() < left_paddle.ycor() + 55 and ball.ycor() > left_paddle.ycor() - 55:
            ball.bounce_x()

    #Detect who score a goal.
    if ball.xcor() > 370:
        ball.reset_pos()
        score.l_paddle_goal()

    if ball.xcor() < -370:
        ball.reset_pos()
        score.r_paddle_goal()

screen.exitonclick()
