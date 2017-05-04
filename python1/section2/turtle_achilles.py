"""Simulate the achilles problem with turtles"""

import turtle
import time

screen = turtle.Screen()
ach = turtle.Turtle()
ach.speed(1)

ach.dot()
ach.penup()
ach.forward(200)
ach.dot()
ach.back(200)

# Go!
step = 100
time.sleep(1)
ach.forward(step)
step = step * .5
time.sleep(1)
ach.forward(step)
step = step * .5
time.sleep(1)
ach.forward(step)
step = step * .5
time.sleep(1)
ach.forward(step)
step = step * .5
time.sleep(1)
ach.forward(step)
step = step * .5
time.sleep(1)
ach.forward(step)
step = step * .5
time.sleep(1)
ach.forward(step)
step = step * .5
time.sleep(1)
ach.forward(step)
step = step * .5
time.sleep(1)
ach.forward(step)
step = step * .5
time.sleep(1)
ach.forward(step)
step = step * .5
time.sleep(1)
ach.forward(step)

screen.mainloop()
