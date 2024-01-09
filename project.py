
from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

snake = Snake()
food = Food()
score = Scoreboard()
screen = Screen()



screen.bgcolor("black")
screen.tracer(0)
screen.title("My snake game")
screen.setup(600,600)
screen.listen()

##########  GAME END FUNCTION   ##########
def q():
    global game_is_on
    game_is_on = False
    
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(q, "q")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food)<18:
        score.increasescore()
        food.refresh()
        snake.append()
       
    if snake.game_end() == True :
        score.refresh()
        snake.resetgame()
    for segment in snake.segments[1:len(snake.segments)]:
        if snake.segments[0].distance(segment)<18:
            score.refresh()
            snake.resetgame()
            

screen.exitonclick()

