#Q7
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
print(is_even(2022))
print(is_even(2023))

#Q8
def is_even(n):
    if n % 2 == 1:
        return True
    else:
        return False
    
print(is_even(2022))
print(is_even(2023))

#Q10 & 11
def is_rightangled(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


print(is_rightangled(3, 4, 5))
print(is_rightangled(3, 4, 10))

#CodingBat:

#hello_name
def hello_name(name):
  return "Hello " + name + "!"
print (hello_name('Bob'))

#make_out_word
def make_out_word(out, word):
  return out[0:2] + word + out[2:4]
print(make_out_word("1111", "que"))

#first_two
def first_two(str):
  return str[0:2]
print(first_two("Pneumonoultramicroscopicsilicovolcanoconiosis"))
  


