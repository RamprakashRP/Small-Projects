import turtle

n = 50
draw = turtle.Turtle()
for i in range(n):
    draw.forward(i * 5)  # Determines the length of the line to be drawn
    draw.right(144)  # Determines the direction and angle the pointer should make
turtle.done()
