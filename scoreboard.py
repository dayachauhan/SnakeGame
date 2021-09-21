from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, ' normal'))

    def score_record(self):
        self.score = self.score + 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('Oh!! Game Over', align='center', font=('Arial', 24, ' normal'))
