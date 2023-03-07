from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_Scoreboard()

    def update_Scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align='center', font=('Courier', 20, 'bold'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER.", align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_Scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_Scoreboard()


