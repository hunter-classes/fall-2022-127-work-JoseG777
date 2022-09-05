import turtle
wn = turtle.Screen()
tr = turtle.Turtle()
tr.shape("turtle")
for angle in ["160", "-43", "270", "-97", "-43", "200", "-940", "17", "-86"]:
  tr.left(int(angle))
  tr.forward(100)

print("Pirate current heading:", tr.heading())


wn.exitonclick()
wn.mainloop()