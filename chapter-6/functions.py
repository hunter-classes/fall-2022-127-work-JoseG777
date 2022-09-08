import turtle
wn = turtle.Screen()
wow = turtle.Turtle()


def square(t, w, x, y, color, l):
  t.penup()
  t.width(w)
  t.goto(x, y)
  t.color(color)
  t.pendown()

  for i in range(4):
    t.forward(l)
    t.right(90)
    
    
    
    

square(wow, 10, 100, 100, "red", 100 )



