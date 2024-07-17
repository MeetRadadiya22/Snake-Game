from turtle import Turtle
import random

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
    self.color("#2ECC71")
    self.speed("fastest")
    self.refresh()

  def refresh(self):
    randomX = random.randint(-270, 270)
    randomY = random.randint(-270, 260)
    self.goto(randomX, randomY)