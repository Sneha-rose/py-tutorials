from turtle import Turtle
t=Turtle()

no = int(input("Enter no of stars:"))
side = int(input("Enter the length of side:"))

t.up()
t.goto(100,0)
t.down()

def star(t,side):
    t.fillcolor("red")
    t.begin_fill()
    t.right(36)
    for count in range(5):
        t.forward(50)
        t.right(144)
        t.forward(50)
        t.left(72)
    t.end_fill()

t.up()
t.goto(90,0)
t.down()

for count in range(no):
    angle = (360/no)
    distance = side * 5
    t.down()
    star(t,side)
    t.up()
