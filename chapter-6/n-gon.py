import turtle
wn = turtle.Screen()
n = turtle.Turtle()
wow = turtle.Turtle()

def ngon(tr, x, y, w, color, S, length, angle):
  tr.penup()
  tr.goto(x,y)
  tr.width(w)
  tr.color(color)
  tr.pendown()
  for i in range(S):
      tr.forward(length)
      tr.right(angle)
  
ngon(n, 100, 100, 10, "red", 4, 100, 90)

ngon(wow, 0, 0, 10, "blue", 6, 100, 60)



wn.exitonclick()