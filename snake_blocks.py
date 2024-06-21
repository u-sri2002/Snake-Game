from turtle import Turtle

FORWARD_MOVES = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Creating Snake blocks 
class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            blocks = Turtle()
            blocks.penup()
            blocks.shape("square")
            blocks.color("white")
            blocks.setpos(x=-(i * 20), y=0)
            self.snake.append(blocks)

    def expand(self):
        blocks = Turtle()
        blocks.penup()
        blocks.shape("square")
        blocks.color("white")
        blocks.setpos(self.snake[-1].position())
        self.snake.append(blocks)

    def move(self):
        # catch the tail of snake
        for block in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[block - 1].xcor()
            new_y = self.snake[block - 1].ycor()
            self.snake[block].setpos(x=new_x, y=new_y)

        self.head.forward(FORWARD_MOVES)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)