"""Draws my name via turtles!"""

import turtle

screen = turtle.Screen()
ryan = turtle.Turtle()
ryan.shape("turtle")

# Get situated
ryan.penup()
ryan.setpos(-300, -100)
ryan.setheading(90)
ryan.pendown()

# R
ryan.forward(200)
ryan.right(90)
ryan.forward(100)
ryan.right(90)
ryan.forward(100)
ryan.right(90)
ryan.forward(100)
ryan.left(135)
ryan.forward(100*(2**.5))
ryan.left(45)

# Move To Y
ryan.penup()
ryan.forward(100)
ryan.left(90)
ryan.pendown()

# Y
ryan.forward(100)
ryan.left(30)
ryan.forward(100*2/(3**.5))
ryan.back(100*2/(3**.5))
ryan.right(60)
ryan.forward(100*2/(3**.5))
ryan.back(100*2/(3**.5))
ryan.right(60)

# Move to A

ryan.penup()
ryan.forward(100)
ryan.right(90)
ryan.forward(100)
ryan.left(180)
ryan.pendown()

# A
ryan.setpos(ryan.xcor() + 50, ryan.ycor() + 200)
ryan.setpos(ryan.xcor() + 50, ryan.ycor() - 200)
ryan.setpos(ryan.xcor() - 25, ryan.ycor() + 100)
ryan.setx(ryan.xcor() - 50)

# Move to N

ryan.penup()
ryan.setpos(ryan.xcor() + 125, ryan.ycor() - 100)
ryan.setheading(90)
ryan.pendown()

# N
ryan.forward(200)
ryan.setpos(ryan.xcor() + 100, ryan.ycor() - 200)
ryan.forward(200)

# Cleanup
ryan.penup()
ryan.home()
ryan.setheading(90)
ryan.forward(50)
ryan.left(90)
ryan.circle(50)
ryan.left(90)
ryan.forward(50)

# Underline
ryan.setpos(-300, -110)
ryan.setheading(0)
ryan.pendown()
ryan.forward(550)

# Go
screen.mainloop()

