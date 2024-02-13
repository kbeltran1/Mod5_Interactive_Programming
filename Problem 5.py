import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

sides = int(8)
angle = 360/sides
length = int(input("Enter length size: "))
line_color = "white"
fill_color = "red"
alex.fillcolor(fill_color)
alex.begin_fill()

for x in range(sides):
    alex.color(line_color, fill_color)
    alex.forward(length)
    alex.left(angle)
alex.end_fill()

wn.exitonclick()