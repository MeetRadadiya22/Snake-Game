from turtle import Turtle, Screen



STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
  def __init__(self):
    self.snake_body = []
    self.create_snake()
    self.head = self.snake_body[0]

  def create_snake(self):
    for i in STARTING_POSITION:
      self.add_body_object(i)
      
  def add_body_object(self, position):
    body_object = Turtle("square")
    body_object.penup()
    body_object.color("white")
    body_object.goto(position)
    self.snake_body.append(body_object)
  
  def extend_snake(self):
    self.add_body_object(self.snake_body[-1].position())

  def move(self):
    for i in range(len(self.snake_body) - 1, 0, -1):
    
      x = self.snake_body[i - 1].xcor()
      y = self.snake_body[i - 1].ycor()
      self.snake_body[i].goto(x, y)
    self.head.forward(MOVE_DISTANCE)
    screen = Screen()
    screen.listen()
    screen.onkey(fun = self.up, key = "Up")
    screen.onkey(fun = self.down, key = "Down")
    screen.onkey(fun = self.left, key = "Left")
    screen.onkey(fun = self.right, key = "Right")
  
  
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
      
  
  
  


