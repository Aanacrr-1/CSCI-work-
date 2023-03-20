
#polygon drawer 

import turtle

#tutle 


def draw_polygon(num_sides, fill_color):
    angle = 360 / num_sides
    side_length = 100
    turtle.color(fill_color)
    turtle.begin_fill()
    for i in range(num_sides):
        turtle.forward(side_length)
        turtle.left(angle)
    turtle.end_fill()
    turtle.hideturtle()
#polygon
while True:
    num_sides = int(input("Enter the number of sides of the polygon: "))
    while num_sides < 3:
        num_sides = int(input("Invalid input! Enter the number of sides of the polygon: "))
    fill_color = input("Enter the color of the polygon: ")
    draw_polygon(num_sides, fill_color)
    repeat = input("Do you want to draw another shape? (yes or no): ")
    turtle.clear()
    turtle.home()
    if repeat.lower() != "yes":
        break

turtle.done()