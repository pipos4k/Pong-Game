from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.penup()
        self.color("pink")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.lscore, align="center", font=("Courier", 40, "bold"))
        self.goto(100, 180)
        self.write(self.rscore, align="center", font=("Courier", 40, "bold"))

    def l_paddle_goal(self):
        self.lscore += 1
        self.update_score()

    def r_paddle_goal(self):
        self.rscore += 1
        self.update_score()