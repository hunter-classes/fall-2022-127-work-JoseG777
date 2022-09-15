import turtle

wn = turtle.Screen()

crush = turtle.Turtle()
for i in [0, 1, 2, 3]:
  crush.forward(100)
  crush.right(90)


squirt = turtle.Turtle()
squirt.up()
squirt.goto(50, 50)
squirt.down()
for i in [0, 1, 2]:
    squirt.forward(100)
    squirt.left(120)


wn.exitonclick()
wn.mainloop()
