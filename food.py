from turtle import Turtle
import random

COLORS = ['red', 'green', 'white']


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color(random.choice(COLORS))
        self.speed('fastest')
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

    def refresh(self):
        self.color(random.choice(COLORS))
        rand_x = random.randint(-290, 290)
        rand_y = random.randint(-290, 290)
        self.goto(rand_x, rand_y)
