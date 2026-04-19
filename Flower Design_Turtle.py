import turtle

t = turtle.Turtle()
t.speed(0)
t.color("red")

for i in range(40):
    t.circle(100, 60)  
    t.left(120)
    t.circle(100, 60)
    t.left(120)
    t.left(10)          

t.penup()
t.goto(0, -20)
t.pendown()
t.begin_fill()
t.end_fill()

turtle.done()
