def piglatin(word):
    first = word[0:1].lower()
    if first == "a" or first == "e" or first == "i" or first == "o" or first == "u" or first == "y":
        return word.capitalize() + "yay"
    else:
        new = word.replace(word[0:1], "") + word[0:1] + "ay"
        return new.capitalize()
        
    
        
print(piglatin("apple"))
print(piglatin("bike"))
print(piglatin("your"))
print(piglatin("hello"))

#Bond
def bondify(name):
  loc = name.find(" ")
  return name[loc + 1:] + ", " + name[0:loc] + name[loc:]
  
print(bondify("Jose Guzman"))