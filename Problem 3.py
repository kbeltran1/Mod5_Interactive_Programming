import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

sides = int(input("Enter number of sides in polygon: "))
angle = 360/sides
length = int(input("Enter length of sides in polygon: "))
line_color = input("Enter color of the lines: ")
alex.color(line_color)
fill_color = input("Enter fill color of the polygon: ")
alex.fillcolor(fill_color)
alex.begin_fill()

for x in range(sides):
    alex.color(line_color, fill_color)
    alex.forward(length)
    alex.left(angle)
alex.end_fill()

wn.exitonclick()