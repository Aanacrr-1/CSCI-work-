import turtle as n
n.begin_fill()

size= float(input("Enter the size of the sides of the rhombus: "))

color = input("Enter the color for shapes: ")
n.fillcolor(color)

n.pensize(4)


n.left(45)
n.forward(size)

n.right(90)
n.forward(size)

n.right(90)
n.forward(size)

n.right(90)
n.forward(size)
n.forward(size)

n.left(90)
n.forward(size)
n.left(90)
n.forward(size)












n.end_fill()

