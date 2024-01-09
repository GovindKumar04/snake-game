from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(0,270)
        # with open("D:/Project/PYTHON/OOPS/DAY-20-21/data.txt") as file:
        #     self.highscore = int(file.read())
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(align='center',font=("Arial", 18, "normal"),move=False,arg=f"score :{self.score} High Score:{self.score}")
        
    
    def refresh(self):
        # if self.score > self.highscore:
            # self.highscore = self.score
            # with open("D:/Project/PYTHON/OOPS/DAY-20-21/data.txt", mode="w") as data:
            #     self.highscore = data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
    def increasescore(self):
        self.score += 1
        self.update_scoreboard()

       
        
        
    