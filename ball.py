import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.shapesize(1, 1)
        self.setheading(50)
        self.new_x = 2
        self.new_y = 2

    def move_forward(self):
        go_x = self.xcor() + self.new_x
        go_y = self.ycor() + self.new_y
        self.goto(go_x, go_y)

    def check_wall(self):
        #Check if ball hit the wall.
        if (self.xcor() > -350 and self.ycor() < -240) or (self.xcor() < 350 and self.ycor() > 240):
            self.bounce_y()

    def bounce_y(self):
        self.new_y *= -1

    def bounce_x(self):
        self.new_x *= -1
        if self.new_x > 0 and self.new_y > 0:
            self.new_x += 1
            self.new_y += 1
        elif self.new_y < 0 and self.new_x < 0:
            self.new_x -= 1

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()
        self.new_x = 2
        self.new_y = 2


    # def check_goal(self):
    #     if self.xcor() > 370:
    #         self.goto(0, 0)
    #         self.bounce_x()
    #         score.l_paddle_goal()
    #
    #     elif self.xcor() < -370:
    #         self.goto(0, 0)
    #         self.bounce_y()
    #         score.r_paddle_goal()



    # def check_wall_xoris_ton_ejento(self):
    #     if self.xcor() > -350 and self.ycor() == -230:
    #         print("Eimai edo EJENTO!")
    #         self.bounce = True
    #     elif self.xcor() < 350 and self.ycor() == 230:
    #         print("Eimai ekei EJENTO!")
    #         self.bounce = False
