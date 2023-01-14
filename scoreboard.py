from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highschore()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score={self.score} Highscore={self.highscore}", align="center", font=("Arial", 24, "normal"))

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            self.update_highscore()
        self.score = 0
        self.update_scoreboard()

    def update_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.highscore))

    def get_highschore(self):
        with open("data.txt", mode="r") as file:
            return file.read()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align="center",font=("Arial",24,"normal"))
