#5
list = [39, 3929, 448, 10, 20, 22, 23]
def max(list):
    top = 0
    for i in list:
        if i > top:
            top = i
            
    return top

print(max(list))


#7

def odd(list):
  odd = 0
  for i in list:
    if i % 2 != 0:
      odd = odd + 1

  return odd

print(odd(list))

#8
def even(list):
  even = 0
  for i in list:
    if i % 2 != 1:
      even = even + 1

  return even

print(even(list))


