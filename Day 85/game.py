import math
import random
import time
from turtle import *

import keyboard

screen = Screen()
screen.setup(1200, 800)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.tracer(0)

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Paddle():

    def __init__(self):
        self.x = 0
        self.y = -300
        self.create_paddle(self.x, self.y)
    def create_paddle(self, x, y):
        self.position = [-40, -20, 0, 20, 40]
        self.paddles = []
        for sub_x in self.position:
            self.paddle = Turtle()
            self.paddle.goto(x-sub_x, y)
            self.paddle.color("white")
            self.paddle.shape("square")
            self.paddle.penup()
            self.paddle.subtract = sub_x
            self.paddles.append(self.paddle)


    def left(self):
        if self.paddles[0].xcor() >= -550:
            self.x -= 12

    def right(self):
        if self.paddles[-1].xcor() <= 550:
            self.x += 12

    def move(self):
        for paddle_s in self.paddles:
            paddle_s.goto(self.x - paddle_s.subtract, -300)

class Brick():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice(["red", "yellow", "blue"])
        self.brick = Turtle()
        self.brick.goto(self.x, self.y)
        self.brick.shape("square")
        self.brick.shapesize(1, 3)
        self.brick.color(self.color)

class Ball():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 6
        self.dy = 6
        self.ball = Turtle()
        self.ball.penup()
        self.ball.goto(self.x, self.y)
        self.ball.shape("circle")
        self.ball.color("white")

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.ball.goto(self.x, self.y)

        if self.y > 380:
            self.dy *= -1

        if self.x < -580 or self.x > 580 :
            self.dx *= -1

def IsCollision(a, b, distance):
    Distance = (((a.xcor() - b.xcor()) ** 2) + ((a.ycor() - b.ycor()) ** 2) ** 0.5)
    if Distance < distance:
        return True
    else:
        return False

bricks = []
for y in range(300, 100, -20):
    for x in range(-580, 580, 60):
        bricks.append(Brick(x, y))
        bricks[-1].color = color
paddle = Paddle()
ball = Ball()
screen.update()
game = True

while game:
    screen.update()
    time.sleep(0.000001)
    paddle.move()
    ball.move()
    if keyboard.is_pressed("Right"):
        paddle.right()
    if keyboard.is_pressed("left"):
        paddle.left()
    dead_bricks = []
    for paddle_d in paddle.paddles:
        if IsCollision(ball.ball, paddle_d, 30):
            ball.dy *= -1

    for brick in bricks:
        if IsCollision(ball.ball, brick.brick, 40):
            ball.dy *= -1
            dead_bricks.append(brick.brick)
            bricks.remove(brick)

    for brick_dead in dead_bricks:
        brick_dead.clear()
        brick_dead.goto(1000000000000000000,10000000000000000000)


    if ball.ball.ycor() < -400:
        print("Game Over")
        game = False

    if len(bricks) == 0:
        print("You won")
        game=False





screen.exitonclick()