import turtle
t = turtle.Turtle()
t.speed(0)

#Pole
t.penup()
t.goto(-220, -250)
t.setheading(90)
t.pendown()
t.width(15)
t.color("gold")
t.forward(500)

#Stand
t.penup()
t.goto(-230, -250)
t.setheading(0)
t.pendown()

t.color("brown")
t.begin_fill()

t.forward(20)
t.right(90)
t.forward(60)
t.right(90)
t.forward(20)
t.right(90)
t.forward(60)

t.end_fill()

# 🇧🇩 Flag
t.penup()
t.goto(-200, 0)
t.setheading(0)
t.pendown()

width = 400
height = 240

t.color("green")
t.begin_fill()
for i in range(2):
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
t.end_fill()

#Red color
t.penup()
t.goto(-50, 60)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(80)
t.end_fill()

turtle.done()
