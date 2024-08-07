import turtle as t
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.backward(200)
#timmy_the_turtle.right(90)
#timmy_the_turtle.left(180)
#timmy_the_turtle.setheading(0)


######## Challenge 1 - Draw a Square ############
for i in range(4):
  timmy_the_turtle.forward(100)
  timmy_the_turtle.left(90)


######## Challenge 2 - Draw a Dashed Line ############
for i in range(15):
  timmy_the_turtle.forward(10)
  timmy_the_turtle.penup()
  timmy_the_turtle.forward(10)
  timmy_the_turtle.pendown()

######## Challenge 3 - Different shapes

tim = t.Turtle()
def draw_shapes(num_sides):
  for _ in range(num_sides):
    angle = 360/num_sides
    tim.forward(100)
    tim.right(angle)

colours = ["red", "blue", "green", "yellow", "orange", "purple", "black"]

for shape_side_n in range(3,11):
  tim.color(random.choice(colours))
  draw_shapes(shape_side_n)


####### Challenge 4 - Generate Random Walk

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue" , "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(20000):
  tim.color(random.choice(colours))
  tim.forward(30)
  tim.setheading(random.choice(direction))
