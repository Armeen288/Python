import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300, 400)
p = turtle.Turtle()
num_sides = 6
side_legth = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    p.forward(side_legth)
    p.right(angle)
    
turtle.done()