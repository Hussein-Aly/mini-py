from turtle import Turtle

FONT = ("Arial", 20, "normal")
GAMEOVERFONT = ("Arial", 30, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.high_score = self.get_high_score()
        self.score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, align="Left", font=FONT)
        self.write(f"High Score: {self.high_score}", False, align="Right", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", False, align="center", font=GAMEOVERFONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        with open("../../Python projects/day-20/data.txt", "w") as file:
            file.write(str(self.high_score))

    def get_high_score(self):
        file = open("../../Python projects/day-20/data.txt", "r")
        content = file.read()
        file.close()
        return int(content)
