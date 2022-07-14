import random
from turtle import Turtle

t = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]
t.pensize(15)
t.shape("classic")
t.color("#228B22")
t.speed("fastest")

for n in range(300):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(direction))
