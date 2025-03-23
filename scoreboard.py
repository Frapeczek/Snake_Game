from turtle import Turtle

ALIGNMEMT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.speed('fastest')
        self.setposition(0, 270)
        self.score = 0

    def write_score(self):
        self.write(f"Score = {self.score}", False, align=ALIGNMEMT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMEMT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write_score()
