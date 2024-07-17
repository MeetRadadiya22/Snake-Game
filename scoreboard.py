from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
  score = 0
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("white")
    self.teleport(0, 260)
    self.score_update()
    
  def game_over(self):
    self.teleport(0, 0)
    self.write(arg = f"GAME OVER", move = False, align = ALIGNMENT, font = FONT)

  def score_update(self):
    self.clear()
    self.write(arg = f"Score: {self.score}", move = False, align = ALIGNMENT, font = FONT)
    self.score += 1  


  

  