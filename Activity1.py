import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
num_of_sides=6
side_Lengh=70
angle=360.0/num_of_sides
for i in range(num_of_sides):
    polygon.forward(side_Lengh)
    polygon.right(angle)
turtle.done()