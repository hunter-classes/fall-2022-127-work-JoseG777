def piglatin(word):
    first = word[0:1].lower()
    if first[0] in "aeiou":
        if "." in word:
            x = word.replace(".", "")
            return x.capitalize() + "yay" + "."
        elif "!" in word:
            x = word.replace("!", "")
            return x.capitalize() + "yay" + "!"
        elif "?" in word:
            x = word.replace("?", "")
            return x.capitalize() + "yay" + "?"
        else:
            return word.capitalize() + "yay"
    if first[0] in "bcdfghjklmnpqrstvwxyz":
        if "." in word:
            x1 = word[0:1]
            x2 = word.replace(word[0:1], "")
            x = x2.replace(".", "") + word[0:1] + "ay" + "."
            return x.capitalize()
        elif "!" in word:
            x1 = word[0:1]
            x2 = word.replace(word[0:1], "")
            x = x2.replace("!", "") + word[0:1] + "ay" + "!"
            return x.capitalize()
        elif "?" in word:
            x1 = word[0:1]
            x2 = word.replace(word[0:1], "")
            x = x2.replace("?", "") + word[0:1] + "ay" + "?"
            return x.capitalize()
        else:
            new = word.replace(word[0:1], "") + word[0:1] + "ay"
        return new.capitalize()
      
    

        

print(piglatin("Apple."))
print(piglatin("Apple!"))
print(piglatin("Apple?"))
print(piglatin("BIKE."))
print(piglatin("BIKE!"))
print(piglatin("BIKE?"))
print(piglatin("BIKE"))


#Bond
def bondify(name):
  loc = name.find(" ")
  return name[loc + 1:] + ", " + name[0:loc] + name[loc:]
  
print(bondify("Jose Guzman"))