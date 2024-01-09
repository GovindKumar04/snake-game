from turtle import Turtle

STARTING_POSTION = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        
        
    def create_snake(self):
        for position in STARTING_POSTION:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
            
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            x_cor = self.segments[seg_num-1].xcor()
            y_cor = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x_cor,y_cor)
        self.segments[0].forward(20)
    def right(self):
        if self.segments[0].heading()==270 or self.segments[0].heading()== 90:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading()==270 or self.segments[0].heading()== 90:
            self.segments[0].setheading(180)
    def up(self):
        if self.segments[0].heading()==0 or self.segments[0].heading()== 180:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading()==0 or self.segments[0].heading()== 180:
            self.segments[0].setheading(270)
    def game_end(self):
        if self.segments[0].xcor() > 300 and self.segments[0].xcor() > 0   or self.segments[0].ycor() > 300 and self.segments[0].ycor() > 0 or self.segments[0].xcor() < -300 and self.segments[0].xcor() < 0 or self.segments[0].ycor() < -300 and self.segments[0].ycor() < 00:
            return True
    def append(self):
        x = self.segments[len(self.segments)-1].xcor()
        y = self.segments[len(self.segments)-1].ycor()
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(x,y)
        self.segments.append(segment)
    def resetgame(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
    



    
    