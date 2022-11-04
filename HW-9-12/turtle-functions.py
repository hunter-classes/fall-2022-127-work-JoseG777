import turtle
wn = turtle.Screen()
wow = turtle.Turtle() #wow will be used to test program

def ngon(tr, x, y, w, color, S, length):
  tr.penup()
  tr.goto(x,y)
  tr.width(w)
  tr.color(color)
  tr.pendown()
  for i in range(S):
      tr.forward(length)
      tr.right(360/S)
  
ngon(wow, 100, 100, 10, "red", 4, 100)

ngon(wow, -100, -100, 10, "green", 3, 100)

ngon(wow, 0, 0, 10, "blue", 6, 100)

wn.exitonclick()