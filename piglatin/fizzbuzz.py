for fb in range (0, 101):
  if fb % 5 == 0 and fb % 3 == 0:
    print(fb, "fizzbuzz")
  elif fb % 3 == 0:
    print(fb, "fizz")
  elif fb % 5 == 0:
    print(fb, "buzz")
  else:
    print(fb)
  
    