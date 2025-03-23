from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.move()
        self.head = self.segments[0]

    def create_snake(self):
        for p in STARTING_POSITIONS:
            self.add_segment(p)

    def add_segment(self, position):
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].seth(RIGHT)
