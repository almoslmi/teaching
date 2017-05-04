# Turtles Cheat Sheet

This cheat sheet should help someone get started (or continue) without having to memorize a billion things about turtles all at once.  Here's a real basic turtles program.

```python
# Boring setup
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Easy One")

# Real program begins here
ned = turtle.Turtle()
ned.color("white")
ned.pensize(2)

# Program his moves!
ned.forward(20)
ned.right(90)
ned.forward(20)
ned.right(90)
ned.forward(20)
ned.right(90)
ned.forward(20)

# Make it go!
screen.mainloop()
```

## Important Commands

### Motion

forward(steps)/back(steps)
right(theta)/left(theta)
goto(x, y)
setheading(theta)
circle(radius, extent, steps)
dot()
stamp()

### Pen Control
penup()/pendown()/pensize()
color()
reset()

### Other Neat Ones
shape("arrow"|"turtle"|"circle"|"square"|"triangle"|"classic")


