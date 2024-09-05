from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        self.write(f"Score: {self.score}", False, "center", ("Courier", 15, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, "center", ("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ("Courier", 30, "normal"))