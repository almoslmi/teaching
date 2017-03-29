"""Another cool turtle example. Credit: Al Sweigart"""

import turtle as t
import random

for n in range(60):
    t. penup()
    t.goto(random.randint(-400, 400), random.randint(-400, 400))
    t.pendown()

    red_amount = random.randint(0, 30)/100
    blue_amount = random.randint(50, 100)/100
    green_amount = random.randint(0, 30)/100
    t.pencolor((red_amount, green_amount, blue_amount))

    circle_size = random.randint(10, 40)
    t.pensize(random.randint(1, 5))

    for i in range(6):
        t.circle(circle_size)
        t.left(60)

