from turtle import Turtle
import time

class Snake:


    def __init__(self):
        self.snake_length = []
        self.create_snake()
        self.heading = 0
        self.head = self.snake_length[0]


    def create_snake(self):
        initial_snake_length = [1, 2, 3]
        x = 0
        for length in initial_snake_length:
            new_turtle = Turtle(shape='square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(x=x, y=0)
            x -= 20
            self.snake_length.append(new_turtle)

    def add_segment(self,position):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake_length.append(new_turtle)

    def extend(self):
        self.add_segment(self.snake_length[-1].position())

    def move(self):
        initial_snake_length = [1, 2, 3]
        for seg in range(len(self.snake_length) - 1, 0, -1):
            new_x = self.snake_length[seg - 1].xcor()
            new_y = self.snake_length[seg - 1].ycor()
            self.snake_length[seg].goto(new_x, new_y)
        self.snake_length[0].forward(20)

    def up(self):
        if self.heading != 270:
            self.snake_length[0].setheading(90)
            self.heading = 90


    def down(self):
        if self.heading != 90:
            self.snake_length[0].setheading(270)
            self.heading = 270

    def left(self):
        if self.heading != 0:
            self.snake_length[0].setheading(180)
            self.heading = 180

    def right(self):
        if self.heading != 180:
            self.snake_length[0].setheading(0)
            self.heading = 0

    def reset(self):
        for body in self.snake_length:
            body.goto(1000,1000)
        self.snake_length.clear()
        self.create_snake()
        self.head = self.snake_length[0]