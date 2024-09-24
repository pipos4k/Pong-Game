import turtle

MOVE_DISTANCE = 20


class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 5)
        self.right(90)
        self.color("pink")
        self.penup()
        self.speed("fastest")
        self.setx(position)

    def up(self):
        self.backward(MOVE_DISTANCE)

    def down(self):
        self.forward(MOVE_DISTANCE)
